.. _lua_scripting:

Lua scripting
=============

Starting with version 4.7, Ardour supports Lua scripts to automate
routine tasks and create new plugins.

.. important::
   
   This documentation is work in progress and far from complete.
   The documented API is subject to change.

.. _lua_scripting_preface:

Preface
-------

There are cases that Ardour cannot reasonably cater to with core
functionality alone, either because they're session-specific or
user-specific edge cases.

Examples for these include voice-activate (record-arm specific tracks
and roll transport depending on signal levels), rename all regions after
a specific timecode, launch an external application when a certain track
is soloed, generate automation curves or simply provide a quick shortcut
for a custom batch operation.

Handling cases like these requires extending the DAW without actually
changing the DAW itself. This is where scripting comes in.

"Scripting" refers to automating tasks that would normally be done
interactively by a human operator.

Lua is a tiny and simple language which is easy to learn, yet allows for
comprehensive solutions. Lua also allows tying existing Ardour
components together in unprecedented ways, and most importantly Lua is
one of the few scripting languages which can be safely used in a
real-time environment.

A good introduction to Lua is the book `Programming in
Lua <http://www.lua.org/pil/>`__. The first edition is available online
for free, but if you have the means we recommend you buy a copy of the
book - it helps support the Lua project and provides a much nicer
reading and learning experience.

.. _lua_scripting_overview:

Overview
--------

The core of Ardour is a real-time audio engine that runs and processes
audio. One interfaces with an engine by sending it commands. Scripting
can be used to interact with or modify the active Ardour session, just
like a user uses the Editor/Mixer GUI to modify the state or parameters
of the session.

Doing this programmatically requires some knowledge about the objects
used internally. Most Ardour C++ objects and their methods are directly
exposed to Lua and one can call functions or modify variables:

=== =======================================
C++ ``session->set_transport_speed (1.0);``
Lua ``Session:set_transport_speed (1.0)``
=== =======================================

You may notice that there is only a small syntactic difference in this
case. While C++ requires recompiling the application for every change,
Lua script can be loaded, written or modified while the application is
running. Lua also abstracts away many of the C++ complexities such as
object lifetime, type conversion and null-pointer checks.

Close ties with the underlying C++ components is where the power of
scripting comes from. A script can orchestrate interaction of
lower-level components which take the bulk of the CPU time of the final
program.

At the time of writing Ardour integrates Lua 5.3.5: `Lua 5.3 reference
manual <http://www.lua.org/manual/5.3/manual.html>`__.

.. _lua_scripting_integration:

Integration
-----------

Like Control surfaces and the GUI, Lua Scripts are confined to certain
aspects of the program. Ardour provides the framework and runs Lua (not
the other way around).

In Ardour's case Lua is available:


Editor Action Scripts
   User initiated actions (menu, shortcuts) for batch processing

Editor Hooks/Callbacks
   Event triggered actions for the Editor/Mixer GUI

Session Scripts
   Scripts called at the start of every audio cycle (session, real-time)

DSP Scripts
   Audio/Midi processor - plugins with access to the Ardour session
   (per track/bus, real-time)

Script Console
   Action Script commandline

There are is also a special mode:

Commandline Tool
   Replaces the complete Editor GUI, direct access to libardour (no GUI)
   from the commandline. *Be aware that the vast majority of complex
   functionality is provided by the Editor UI.*

.. _lua_scripting_managing_scripts:

Managing scripts
----------------

Ardour searches for Lua scripts in the ``scripts`` folder in
``$ARDOUR_DATA_PATH``, Apart from scripts included directly with Ardour,
this includes

GNU/Linux
   ``$HOME/.config/ardour8/scripts``

macOS
   ``$HOME/Library/Preferences/Ardour8/scripts``

Windows
   ``%localappdata%\ardour8\scripts``

Files must end with ``.lua`` file extension.

Scripts are managed via the GUI:

Editor Action Scripts
   Menu: **Edit > Scripted Actions > Manage**; or alternatively
   right-click on an action-script button top-right in the toolbar

Editor Hooks/Callbacks
   Menu: **Edit > Scripted Actions > Manage**

Session Scripts
   Menu: **Session > Scripting > Add/Remove Script**

DSP Scripts
   Are added like other plugins to a mixer-strip's processor box

Script Console
   Menu: **Window > Scripting**

.. _lua_scripting_script_layout:

Script layout
-------------

-  Every script must include an ``ardour`` descriptor table. Required
   fields are "Name" and "Type".
-  A script must provide a *Factory method*: A function with optional
   instantiation parameters which returns the actual script.
-  [optional]: list of parameters for the "factory".
-  in case of DSP scripts, an optional list of automatable parameters
   and possible audio/midi port configurations, and a ``dsp_run``
   function, more on that later.

A minimal example script looks like:

.. code-block:: lua

   ardour {
     ["type"]    = "EditorAction",
     name        = "Rewind",
   }

   function factory (unused_params)
     return function ()
      Session:goto_start()  -- rewind the transport
     end
   end

The common part for all scripts is the "Descriptor". It's a Lua function
which returns a table (key/values) with the following keys (the keys are
case-sensitive):


type [required]
   one of "``DSP``", "``Session``", "``EditorHook``", "``EditorAction``"
   (the type is not case-sensitive)                               |

name [required]
   Name/Title of the script

author
   Your Name

license
   The license of the script (e.g. "GPL" or "MIT")

description
   A longer text explaining to the user what the script does

Scripts that come with Ardour (currently mostly examples) can be found
in the `Source
Tree <https://github.com/Ardour/ardour/tree/master/share/scripts>`__.

.. _lua_scripting_action_scripts:

Action scripts
~~~~~~~~~~~~~~

Action scripts are the simplest form. An anonymous Lua function is
called whenever the action is triggered. A simple action script is shown
above.

There are 10 action script slots available, each of which is a standard
GUI action available from the menu and hence can be bound to a keyboard
shortcut.

.. _lua_scripting_session_scripts:

Session scripts
~~~~~~~~~~~~~~~

Session scripts similar to Actions Scripts, except the anonymous
function is called periodically every process cycle. The function
receives a single parameter - the number of audio samples which are
processed in the given cycle

.. code-block:: lua

   ardour {
     ["type"]    = "session",
     name        = "Example Session Script",
     description = [[
     An Example Ardour Session Script.
     This example stops the transport after rolling for a specific time.]]
   }

   -- instantiation options, these are passed to the "factory" method below
   function sess_params ()
     return
     {
       ["print"]  = { title = "Debug Print (yes/no)", default = "no", optional = true },
       ["time"] = { title = "Timeout (sec)", default = "90", optional = false },
     }
   end

   function factory (params)
     return function (n_samples)
       local p = params["print"] or "no"
       local timeout = params["time"] or 90
       a = a or 0
       if p ~= "no" then print (a, n_samples, Session:frame_rate (), Session:transport_rolling ()) end -- debug output (not rt safe)
       if (not Session:transport_rolling()) then
         a = 0
         return
       end
       a = a + n_samples
       if (a > timeout * Session:frame_rate()) then
         Session:request_transport_speed (0.0, true, ARDOUR.TransportRequestSource.TRS_UI)
       end
     end
   end

.. _lua_scripting_action_hooks:

Action hooks
~~~~~~~~~~~~

Action hook scripts must define an additional function which returns a
*Set* of Signal that which trigger the callback (documenting available
slots and their parameters remains to be done).

.. code-block:: lua

   ardour {
     ["type"]    = "EditorHook",
     name        = "Hook Example",
     description = "Rewind On Solo Change, Write a file when regions are moved.",
   }

   function signals ()
     s = LuaSignal.Set()
     s:add (
       {
         [LuaSignal.SoloActive] = true,
         [LuaSignal.RegionPropertyChanged] = true
       }
     )
     return s
   end

   function factory (params)
     return function (signal, ref, ...)
       -- print (signal, ref, ...)
       if (signal == LuaSignal.SoloActive) then
         Session:goto_start()
       end

       if (signal == LuaSignal.RegionPropertyChanged) then
         obj,pch = ...
         file = io.open ("/tmp/test" ,"a")
         io.output (file
         io.write (string.format ("Region: '%s' pos-changed: %s, length-changed: %s\n",
           obj:name (),
           tostring (pch:containsFramePos (ARDOUR.Properties.Start)),
           tostring (pch:containsFramePos (ARDOUR.Properties.Length))
           ))
         io.close (file)
       end
     end
   end

.. _lua_scripting_dsp_scripts:

DSP scripts
~~~~~~~~~~~

See the scripts folder for examples for now.

Some notes for further doc:

-  required function: ``dsp_ioconfig ()``: return a list of possible
   audio I/O configurations - follows Audio Unit conventions.
-  optional function: ``dsp_dsp_midi_input ()``: return true if the
   plugin can receive midi input
-  optional function: ``dsp_params ()``: return a table of possible
   parameters (automatable)
-  optional function: ``dsp_init (samplerate)``: called when
   instantiation the plugin with given samplerate.
-  optional function: ``dsp_configure (in, out)``: called after
   instantiation with configured plugin i/o.
-  required function: ``dsp_run (ins, outs, n_samples)`` OR
   ``dsp_runmap (bufs, in_map, out_map, n_samples, offset)``: DSP
   process callback. The former is a convenient abstraction that passes
   mapped buffers (as table). The latter is a direct pass-through
   matching Ardour's internal ``::connect_and_run()`` API, which
   requires the caller to map and offset raw buffers.
-  plugin parameters are handled via the global variable ``CtrlPorts``.
-  midi data is passed via the global variable ``mididata`` which is
   valid during ``dsp_run`` only. (dsp_runmap requires the script to
   pass raw data from the buffers according to in_map)
-  The script has access to the current session via the global variable
   Session, but access to the session methods are limited to realtime
   safe functions

.. _lua_scripting_accessing_ardour_objects:

Accessing Ardour objects
------------------------

The top most object in Ardour is the ``ARDOUR::Session``. Fundamentally,
a session is just a collection of other things: Routes (tracks, busses),
Sources (Audio/Midi), Regions, Playlists, Locations, Tempo map,
Undo/Redo history, Ports, Transport state and controls, etc.

Every Lua interpreter can access it via the global variable ``Session``.

GUI context interpreters also have an additional object in the global
environment: The Ardour ``Editor``. The Editor provides access to high
level functionality which is otherwise triggered via GUI interaction
such as undo/redo, open/close windows, select objects, drag/move
regions. It also holds the current UI state: snap-mode, zoom-range, etc.
The Editor also provides complex operations such as "import audio" which
under the hood, creates a new Track, adds a new Source Objects (for
every channel) with optional resampling, creates both playlist and
regions and loads the region onto the Track all the while displaying a
progress information to the user.

Documenting the bound C++ methods and class hierarchy is somewhere on
the ToDo list. Meanwhile
`luabindings.cc <https://github.com/Ardour/ardour/blob/master/libs/ardour/luabindings.cc>`__
is the best we can offer.

.. _lua_scripting_concepts:

Concepts
--------

-  There are no bound constructors: Lua asks Ardour to create objects
   (e.g. add a new track), then receives a reference to the object to
   modify it.
-  Scripts, once loaded, are saved with the Session (no reference to
   external files). This provides for portable Sessions.
-  Lua Scripts are never executed directly. They provide a "factory"
   method which can have optional instantiation parameters, which
   returns a Lua closure.
-  No external Lua modules/libraries can be used, scripts need to be
   self contained (portable across different systems (libs written in
   Lua can be used, and important c-libs/functions can be included with
   Ardour if needed).

Ardour is a highly multithreaded application and interaction between the
different threads, particularly real-time threads, needs to to be done
with care. This part has been abstracted away by providing separate Lua
interpreters in different contexts and restricting available
interaction:

-  Editor Actions run in a single instance interpreter in the GUI
   thread.
-  Editor Hooks connect to libardour signals. Every Callback uses a
   dedicated Lua interpreter which is in the GUI thread context.
-  All Session scripts run in a single instance in the main real-time
   thread (audio callback)
-  DSP scripts have a separate instance per script and run in one of the
   DSP threads.

The available interfaces differ between contexts. For example, it is not
possible to create new tracks or import audio from real-time context;
while it is not possible to modify audio buffers from the GUI thread.

.. _lua_scripting_current_state:

Current state
-------------

Fully functional, yet still in a prototyping stage:

-  The GUI to add/configure scripts is rather minimalistic.
-  The interfaces may change (particularly DSP, and Session script
   ``run()``.
-  Further planned work includes:

   -  Built-in Script editor (customize/modify Scripts in-place).
   -  convenience methods (wrap more complex Ardour actions into a
      library). e.g set plugin parameters, write automation lists from a
      Lua table.
   -  Add some useful scripts and more examples.
   -  Documentation (Ardour API), also usable for tab-expansion, syntax
      highlighting.
   -  Bindings for GUI Widgets (plugin UIs, message boxes, etc.).

.. _lua_scripting_examples:

Examples
--------

Please see the example `scripts included with the
source-code <https://github.com/Ardour/ardour/tree/master/share/scripts>`__.
All the files that start with a leading underscore are not included with
releases, but are intended as example snippets.

.. _lua_scripting_commandline_session:

Commandline session
-------------------

The standalone tool ``luasession`` allows one to access an Ardour
session directly from the commandline. It can also be used as #!
interpreter for scripted sessions. Interaction is limited by the fact
that most actions in Ardour are provided by the Editor GUI.

``luasession`` provides only two special functions ``load_session`` and
``close_session`` and exposes the ``AudioEngine`` instance as global
variable.

.. code-block:: lua

   for i,_ in AudioEngine:available_backends():iter() do print (i.name) end

   -- pick one --
   if false then
       backend = AudioEngine:set_backend("JACK", "", "")
   elseif false then
       backend = AudioEngine:set_backend("ALSA", "", "")
       for i,_ in backend:enumerate_devices():iter() do print (i.name) end
       backend:set_device_name("HDA Intel PCH")
       backend:set_peridod_size(3)
       backend:set_buffer_size(1024)

   else
       AudioEngine:set_backend("None (Dummy)", "", "")
   end

   print (AudioEngine:current_backend_name())

   print (backend:buffer_size())
   print (AudioEngine:get_last_backend_error())

   s = load_session ("/home/rgareus/Documents/ArdourSessions/lua2/", "lua2")

   assert (s)

   s:request_roll (ARDOUR.TransportRequestSource.TRS_UI)
   print (s:transport_rolling())

   s:goto_start()

   ARDOUR.LuaAPI.usleep (10 * 1000000) -- 10 seconds

   close_session()