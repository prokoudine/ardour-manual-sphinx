.. _osc_basics:

OSC basics
==========

OSC lets synthesizers and other devices communicate with Ardour. OSC
devices can send commands relating to playback (such as play or stop),
performance (such as volume, play, stop), and almost any other function
(such as **Edit**, or **Undo**).

Ardour is probably one of the most OSC-controllable audio applications
around, but as with all OSC-controllable apps, you can't do much without
knowing what messages can be sent. This document describes the various
categories of messages that Ardour understands. It is subject to change,
particularly the "Actions" part below, since this relates to the GTK GUI
for Ardour rather than the backend.

Connecting to Ardour via OSC
----------------------------

OSC support is not enabled by default, but can be turned on via Edit >
Preferences > Control Surfaces. Once enabled, Ardour will listen on port
``3819`` by default. This port number can be changed by editing
``$ARDOUR_CONFIG`` and adding this line within the ``<Config>`` section:

.. code-block:: xml

   <Option name="osc-port" value="*Your choice here*"/>

Ardour sends any feedback to the port and address that sent any feedback
request or to a port set manually in the setup dialog. The port does not
have to match Ardour's port. In fact it is better not to. This means
that Ardour can deal with more than one controller at a time.

The two controllers can bank independently and even use different math
for faders. This could be used to allow talent to adjust their own
monitor mix using a tablet or phone that can run an OSC controller. For
a full explanation of how Ardour's feedback works please read :ref:`OSC
feedback In Ardour <osc58_feedback>`.

.. _osc_set-up:

Setting up the control surface
------------------------------

Control surface set up allows the controller to tell Ardour about its
capabilities. The surface can tell Ardour how many control strips it has
for banking, if it is capable of setting its faders or buttons to values
set by Ardour's GUI or automation, What kind of math the faders use and
more.

Any time the ``/set_surface`` command is sent, the current bank is
recalculated and if feedback is turned on, the values of each strip's
controls are sent (or refreshed) as well. This will also refresh the
Master feedback setup.

Since Ardour 5.1, there is now a GUI setup in response to those using
tablets with applications such as touchOSC or AndrOSC who need to be
able to set a port for Ardour to send to. It can also change the default
setting for set_surface. For more information about Ardour's OSC
configuration GUI please read :ref:`Ardour's Setup
Dialog. <osc58_using_the_setup_dialog>`

If ``/set_surface`` is not sent, the default values are used:

-  ``Bank Size``: ``0`` — No banking (or infinite bank size).
-  ``Strip Types``: ``159`` — All strip types except hidden and special.
-  ``Feedback``: ``0`` — All off.
-  ``Fader Mode``: ``0`` — gain in dB (not relevant with feedback off)
-  ``Send Page Size``: ``0`` — No Send Paging.
-  ``Plugin Page Size``: ``0`` — No Plugin (parameter) Paging.
-  ``reply port``: ``8000`` — control surface will receive feedback on port
   8000
-  ``Link set``: ``0`` — no linking for this control surface
-  ``Link ID``: ``0`` — no link ID

These values give the same behaviour as prior versions of Ardour. (or
the closest possible)

``/set_surface *bank_size* *strip_types* *feedback* *fadermode* *send_page_size* *plugin_page_size* *port* *linkset* *linkid*``

See below for an explanation of each parameter.

.. note::

   The ``/set_surface`` message may have all values except the last
   in-line. For example: ``/set_surface/8/31/8403/0/8 i 16`` would be
   valid. Do be careful of switches which send a ``0`` on release, it
   may be necessary to set the value as the release value rather than
   the press value.
   
   The ``/set_surface`` message may have less than the full set of
   parameters. those left out will remain as they were before the
   ``/set_surface`` message was sent. All parameters included must be
   valid.
   
   For example, setting send page size would require also setting
   ``bank_size``, ``strip_types``, ``feedback`` and ``gain mode``. Using
   only two parameters will set ``bank_size`` and ``strip_types``.
   Sending ``/set_surface`` with no parameters will result in Ardour
   returning a ``/set_surface`` message with the current settings.
   Surfaces using ``/set_surface iiii b st fb gm`` as was the case in
   versions of Ardour older than 5.10 will continue to work.

bank_size
~~~~~~~~~

``bank_size`` is the number of channel strips the controller supports
without banking. Setting this to ``0`` turns banking off by setting the bank
size to infinite.

.. note::
   
   Bank size can also be set with */set_surface/bank_size size.*

strip_types
~~~~~~~~~~~

``strip_types`` is an integer made up of bits. The easy way to deal with
this is to think of strip_types items being worth a number and then
adding all those numbers together for a value to send. Strip Types will
determine what kind of strips will be included in bank. This would
include: Audio, MIDI, busses, VCAs, Master, Monitor and hidden or
selected strips.

Aside from setting the track types for the main mix assignments, using
``/set_surface/strip_types`` with more than one surface button will
allow switching between modes for example: inputs only, busses only,
selected only, hidden only, by having the buttons send values of: ``3``,
``12``, ``256``, ``512``. A full mix button might have a value ``31``.

While Master and Monitor are listed as possibilities, most surfaces will
not use them. Using ``/master`` and ``/monitor`` makes more sense.
However, in the case where there are no master or monitor fader strips
on the surface, it may be necessary to include them in the banked
strips.

Please see: :ref:`Calculating Feedback and Strip-types
Values <osc58_feedback_and_strip_types_values>`.

.. note::

   Strip types can also be set with ``/set_surface/strip_types types``.

feedback
~~~~~~~~

``feedback`` is an integer made up of bits. The easy way to deal with this
is to think of feedback items being worth a number and then adding all
those numbers together for a value to send.

Please see: :ref:`Calculating Feedback and Strip-types
Values <osc58_feedback_and_strip_types_values#feedback>`.

.. note::

   Feedback can also be set with ``/set_surface/feedback feedback``.

gainmode
~~~~~~~~

Gainmode is an int:

-  ``0``: dB value as a float from ``-193`` to ``+6``. Sent as ``/strip/gain SSID value``. (-193 or below are the same as ``−∞``)
-  ``1``: A positional fader based on the same math as Ardour's GUI. A
   Float from ``0`` to ``1``. Sent as ``strip/fader SSID value``. At the same time
   the gain value in dB is sent to the channel name as text. The name
   will be restored after a short timeout.
-  ``2``: A positional fader based on the same math as Ardour's GUI. A
   Float from ``0`` to ``1``. Sent as ``/strip/fader SSID value``. At the same time
   the gain value in dB is sent as ``/strip/gain SSID value``.
-  ``3``: A positional fader based on the same math as Ardour's GUI. A
   Float from ``0`` to ``1``. Sent as ``/strip/fader SSID value``.

Gainmode applies only to feedback values. The controller can choose
which gain math to use by choosing to use the ``/*/gain`` or ``/*/fader`` path
to send to Ardour. This makes sure a controller that doesn't set up
Ardour's OSC can still use either math. The gainmode for feedback also
determines the path Ardour uses for feedback so that the feedback
messages match the control messages.

.. note::
   
   Gain mode can also be set with ``/set_surface/gainmode gainmode``.

send_page_size
~~~~~~~~~~~~~~

``send_page_size`` is an int for the number of send channels that can be
controlled at one time. Each channel has a name, level and enable
control.

.. note::
   
   Send page size can also be set with
   ``/set_surface/send_page_size send_page_size``.

plugin_page_size
~~~~~~~~~~~~~~~~

``plugin_page_size`` is an int for the number of plugin controls that can be
controlled at one time. Each control has a name and level. As each
plugin is different (as is each parameter), the surface should expect to
control the plugin parameters with a variable control (pot or slider)
with a float value from ``0`` to ``1`` (even on/off switches).

.. note::
   
   Plugin page size can also be set with
   ``/set_surface/plugin_page_size plugin_page_size``.

port
~~~~

The port the controller would like to receive it's feedback on. The
surface can directly set the manual port or set it's host to ``auto``
port mode.

The value for ``port`` can be ``0`` for ``auto`` port mode or any port
value above ``1024``. It is suggested not to use Ardour's port number of
``3819`` as controllers on the same machine that try to use the same
port will fail.

If the surface does not tell Ardour which port to use, the default is
8000 or the setting set up in the OSC setup GUI. There can only be one
port setting per host. If that setting is ``auto``, than more than one
controller can be run on that host, but if a manual port is set there
can only be one. In the case of ``auto`` mode, the control surface must
set it's receive port to be the same as it's send port. If that is not
possible, then manual port mode must be used. This allows a smart
controller to use a number of ports on the same ip while a smartphone
set up as a personal monitor control can use the default manual port.

.. note::

   The host's port can also be set with ``/set_surface/port port``.

   Changing the port will remove feedback from a device on the same
   host using a different port.

Link set and Link ID
~~~~~~~~~~~~~~~~~~~~

Please see :ref:`Linking Surfaces <osc58_linking_surfaces>` for more
information.

Querying Ardour for information
-------------------------------

The control surface may wish to control the type a frequency of updates
it receives. It can do this with querying commands. See :ref:`Querying
Ardour with OSC <osc58_querying_ardour>`.

Using more than one surface
---------------------------

Ardour can use more than one surface at a time that both control the
same controls in Ardour. It is also possible to use two surfaces in
concert with each other. See :ref:`Linking Surfaces
<osc58_linking_surfaces>` for more information.

List of OSC messages
--------------------

Parameter types show how the value will be used. However, they may be
sent as a different type if needed, see :ref:`Parameter Types in
OSC <osc58_parameter_types>`.

This list shows all messages that can be sent to Ardour to control it.
Most of these messages are also sent back as feedback when the
corresponding value changes. There exist additional feedback-only
messages, see :ref:`Feedback <osc58_feedback>` for more information.

.. _osc_global:

Master or global messages
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _osc_transport:

Transport Control
^^^^^^^^^^^^^^^^^

``/transport_stop``
   Stops a rolling transport

``/transport_play``
   Puts transport in play mode

``/toggle_roll``
   Toggles between play and stop

``/stop_forget``
   Stop transport and delete/forget last take

``/set_transport_speed *speed*``
   where *speed* is a float ranging from -8.0f to 8.0f

``/ffwd``
   Adds 1.5 times to transport speed to maximum +8 times normal speed

``/rewind``
   Adds -1.5 times to transport speed to maximum -8 times normal speed

``/goto_start``
   Move playhead to start of session

``/goto_end``
   Move playhead to end of session

``/jump_bars *bars*``
   Where *bars* is a float (+/-) of the number of bars to jump

``/jump_seconds *seconds*``
   Where *seconds* is a float (+/-) of the number of seconds to jump

``/toggle_click``
   Toggle metronome click on and off

``/marker *marker*``
   Where *marker* may be a float or int of the nth marker or a string with the marker name to locate to. If the playhead is at a marker and the *marker* is unique, the marker at the playhead will be renamed to the string sent

``/add_marker``
   Adds marker to the current transport position

``/remove_marker``
   Removes marker at the current transport position (if there is one)

``/next_marker``
   Move playhead to next marker

``/prev_marker``
   Move playhead to previous marker

``/locate *spos* *roll*``
   Where *spos* is the target position in samples and *roll* is a bool/integer defining whether you want transport to be kept rolling or not

``/loop_toggle``
   Toggle loop mode on and off

``/loop_location *start* *end*``
   *start* is the beginning of a loop and *end* is the end of a loop, both are integer frame positions

``/midi_panic``
   Ardour will send an all notes off to all MIDI tracks

``/cancel_all_solos``
   Cancel All Solos/PFLs/AFLs

``/scrub *delta*``
   Where *delta* is a float indicating forward or reverse movement. See :ref:`OSC Scrub Modes <osc58_jog_modes#scrub>`

``/jog *delta*``
   Where *delta* is a float indicating forward or reverse movement

``/jog/mode *mode*``
   Where *mode* is an int from 0 to 7 indicating what the */jog* command controls. See :ref:`OSC Jog Modes <osc58_jog_modes>`

.. _osc_recording:

Recording control
^^^^^^^^^^^^^^^^^

``/toggle_punch_in``
   Toggles punch in

``/toggle_punch_out``
   Toggles punch in

``/rec_enable_toggle``
   Toggles master record enable

.. _osc_information:

Transport Information
^^^^^^^^^^^^^^^^^^^^^

``/transport_frame```
   Ardour sends /transport_frame *current_frame*

``/transport_speed``
   Ardour sends /transport_speed *speed*

``/record_enabled``
   Ardour sends /record_enabled *recordenable_status*

.. _osc_editing:

Editing-related
^^^^^^^^^^^^^^^

``/undo``
   Performs undo for the last operation

``/redo``
   Performs redo for the last operation

``/save_state``
   This is the regular **Session > Save** operation

``/session_name *new_name*``
   Set session name to *new_name* (if *new_name* is legal and unique)

.. _osc_Master-strip:

Master and Monitor strip control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``/master/gain *dB*``
   *dB* is a float indicating the desired gain in dB

``/master/fader *position*``
   *position* is a float between ``0`` and ``1`` setting the desired position of the fader

``/master/db_delta *delta*``
   *delta* is a float that will increase or decrease the gain of master by the amount of the delta

``/master/trimdB *dB*``
   *dB* is a float from ``-20`` to ``+20`` representing the desired trim gain in dB

``/master/pan_stereo_position *position*``
   *position* is a float from ``0`` to ``1`` representing the desired pan position

``/master/mute *key*``
   *key* is an optional float ``1`` representing a master bus select

``/master/select *state*``
   *state* is an int of ``0`` or ``1`` representing the desired mute state

``/monitor/gain *dB*``
   *dB* is a float indicating the desired gain in dB

``/monitor/fader *position*``
   *position* is a float between ``0`` and ``1`` setting the desired position of the fader

``/monitor/db_delta *delta*``
   *delta* is a float that will increase or decrease the gain of monitor by the amount of the delta

``/monitor/mute *state*``
   *state* is an int of ``0`` or ``1`` where ``1`` is muted

``/monitor/dim *state*``
   *state* is an int of ``0`` or ``1`` where ``1`` is dimmed

``/monitor/mono *state*``
   *state* is an int of ``0`` or ``1`` where ``1`` is mono mode

.. _osc_strips:

Track specific operations
~~~~~~~~~~~~~~~~~~~~~~~~~

For each of the following, *ssid* is the Surface Strip ID for the track

The user may use a subset all available strips. See :ref:`Making a user
selected strip list. <osc58_custom_strips>`

SSID has a different meaning than RID in Ardour version 4.7 and before.
Effectively, banking is always being used and the SSID is generated on
the fly. The SSID is the position of the strip within bank as an int 1
to bank size. There are no gaps as there have been in the past.
Depending on the value of strip_types sent to Ardour, Master and
Monitor, may be included in the list of SSIDs or not as set in
*/set_surface*.

Some Surfaces (many Android applets) are not able to deal with more than
one parameter in a command. However, the two parameter commands below
can also be sent as /strip/command/ssid param. In this case the param
should be a float even if an int is required below.

``/bank_up``
   Change bank to the next higher bank.

``/bank_up *delta*``
   Where *delta* is a float of ``1`` to bank up and ``-1`` is bank down for use with an encoder.

``/bank_down``
   Change bank to the next lower bank.

``/use_group *state*``
   Where *state* is a float of ``1`` to use group or ``0`` to not use group.
   :ref:`More info on use_group <osc58_feedback_and_strip_types_values#use-group>`.

``/strip/spill *ssid*``
   Use strips this strip is grouped with or those that feed this bus (if this strip is a bus) or that this vca (if this is a VCA) controls.
   See `Spill Strips <#osc_spill>`__ for more details.

``/strip/hide *ssid* *y/n*``
   Where *y/n* = 1 hide this strip, ``0`` for show this track.
   `Hiding strips. <osc58-feedback_and_strip_types_values#hidden>`

``/strip/name *ssid* *strip_name*``
   where *strip_name* is a string representing the desired name for the strip.

``/strip/group *ssid* *group_name*``
   where *group_name* is a string representing the name of the group desired.
   See `groups <#osc_groups>`__ for more details.

``/strip/mute *ssid* *mute_st*``
   where *mute_st* is a bool/int representing the desired mute state of the track.

``/strip/solo *ssid* *solo_st*``
   where *solo_st* is a bool/int representing the desired solo state of the track.

``/strip/solo_iso *ssid* *state*``
   where *state* is a bool/int representing the desired solo isolate state of the track.

``/strip/solo_safe *ssid* *state*``
   where *state* is a bool/int representing the desired solo safe/lock state of the track.

``/strip/monitor_input *ssid* *monitor_st*``
   where *monitor_st* is a bool/int where 1 is forced input monitoring.

``/strip/monitor_disk *ssid* *monitor_st*``
   where *monitor_st* is a bool/int where 1 is forced disk monitoring.
   When input and disk are both off, auto-monitoring is enabled.

``/strip/recenable *ssid* *rec_st*``
   where *rec_st* is a bool/int representing the desired rec state of the track.

``/strip/record_safe *ssid* *rec_st*``
   where *rec_st* is a bool/int representing the desired record safe state of the track.

``/strip/polarity *ssid* *invert*``
   where *invert* is a bool/int representing the desired polarity of the track.

``/strip/gain *ssid* *gain*``
   where *gain* is a float ranging from ``-193`` to ``6`` representing the desired gain of the track in dB.

``/strip/fader *ssid* *position*``
   where *position* is a float ranging from ``0`` to ``1`` representing the fader control position.

``/strip/db_delta *ssid* *delta*``
   where *delta* is a float that will increase or decrease the gain of a track by the amount of the delta.

``/strip/*/automation *ssid* *mode*``
   where *mode* is an int ranging from ``0`` to ``3`` representing the desired automation mode for the control.
   :ref:`See OSC Automation <osc58_automation>`.

``/strip/*/touch *ssid* *state*``
   where *state* is an int of ``1`` for touched and ``0`` for released.
   :ref:`See OSC Automation <osc58_automation>`.

``/strip/trimdB *ssid* *trim_db*``
   where *trim_db* is a float ranging from ``-20`` to ``20`` representing the desired trim of the track in dB.

``/strip/pan_stereo_position *ssid* *position*``
   where *position* is a float ranging from ``0`` to ``1`` representing the desired pan position of the track.

``/strip/pan_stereo_width *ssid* *width*``
   where *width* is a float ranging from 0 to 1 representing the desired pan width of the track.

``/strip/send/gain *ssid* *sendid* *send_gain*``
   where *sendid* = nth_send, *send_gain* is a float ranging from ``-193`` to ``+6`` representing the desired gain in dB for the send.

``/strip/send/fader *ssid* *sendid* *send_gain*``
   where *sendid* = nth_send, *send_gain* is a float ranging from ``0`` to ``1`` representing the desired position for the send as a fader.

``/strip/send/enable *ssid* *sendid* *state*``
   where *sendid* = nth_send, *state* is ``1`` for enabled and ``0`` for disabled.

``/strip/list``
   see: :ref:`Querying Ardour with OSC. <osc58_querying_ardour>`

``/strip/sends *ssid*``
   see: :ref:`Querying Ardour with OSC. <osc58_querying_ardour>`

``/strip/receives *ssid*``
   see: :ref:`Querying Ardour with OSC. <osc58_querying_ardour>`

``/strip/plugin/list *ssid*``
   see: :ref:`Querying Ardour with OSC. <osc58_querying_ardour>`

``/strip/plugin/descriptor *ssid*``
   see: :ref:`Querying Ardour with OSC. <osc58_querying_ardour>`

``/strip/plugin/reset *ssid* *piid*``
   where *piid* = nth Plugin, will reset all values to the plugin's original values.

``/strip/plugin/activate *ssid* *piid*``
   where *piid* = nth Plugin, will set the plugin's state to active.

``/strip/plugin/deactivate *ssid* *piid*``
   where *piid* = nth Plugin, will set the plugin's state to inactive.

``/strip/plugin/parameter *ssid* *piid* *param* *value*``
   where *piid* = nth Plugin, *param* = nth param, *value* is a float ranging from ``0`` to ``1`` representing the desired parameter value.

``/strip/name *ssid* *name*``
   where *name* is a string for the desired name of the track.

.. _osc_select:

Selected Strip Operations
~~~~~~~~~~~~~~~~~~~~~~~~~

Selected strip operations are complex enough for their own page. Please
read :ref:`Selection Considerations in OSC
<osc58_selection_and_expansion_considerations>`. This is most important
if more than one OSC surface is being used with Ardour.

There are two kinds of selection in OSC. GUI selection and local
expansion. By default expansion follows selection.

-  GUI selection: Use ``/strip/select`` to set. Selecting a strip in the
   GUI will set OSC surface select and the surface will set GUI
   selection as well.
-  Local expansion: Use ``/strip/expand`` to expand a strip without
   changing overall selection. When ````/strip/expand```` is set to ``0``
   or ``false``, the select channel will go back to using the strip
   selected by the GUI. While expand is turned on, selecting a strip on the
   GUI does not select the OSC strip. Sending a ``/strip/select`` message
   will override the expand as if it had been set to false. Good for more
   than one OSC controller at a time.

Here’s the converted table in definition format, with each definition prepended by three spaces and wrapped in triple backticks, as requested:

Here’s the same definition list with the three leading spaces removed from each line:

/strip/select *ssid* *y/n*
   Where *y/n* = ``1`` for select. Sets both GUI select and strip to expanded mode (``0`` is ignored).

/strip/expand *ssid* *y/n*
   Where *y/n* = ``1`` for expanded mode. Sets only local strip to Expanded. Setting to ``0`` resets the expansion to follow selection.

``/select/expand *y/n*``
   Where *y/n* = ``1`` for expanded mode, ``0`` for Select mode.

``/select/hide *y/n*``
   Where *y/n* = ``1`` hide this strip, ``0`` for show this track.

``/select/name *strip_name*``
   where *strip_name* is a string representing the desired name for the strip

``/select/comment *comment*``
   where *comment* is a string representing the desired comment for the strip

``/select/group *group_name*``
   where *group_name* is a string representing the name of the group desired.

``/select/group/enable *state*``
   where *state* is an int representing the desired enable state of the group the selected strip is a part of

``/select/group/gain *state*``
   where *state* is an int which sets the gain sharing of the group the strip belongs to.

``/select/group/relative *state*``
   where *state* is an int which sets relative state of the group the strip belongs to.

``/select/group/mute *state*``
   where *state* is an int which sets the mute sharing of the group the strip belongs to.

``/select/group/solo *state*``
   where *state* is an int which sets the solo sharing of the group the strip belongs to.

``/select/group/recenable *state*``
   where *state* is an int which sets the recenable sharing of the group the strip belongs to.

``/select/group/select *state*``
   where *state* is an int which sets the select sharing of the group the strip belongs to.

``/select/group/active *state*``
   where *state* is an int which sets the route active sharing of the group the strip belongs to.

``/select/group/color *state*``
   where *state* is an int which sets the color sharing of the group the strip belongs to.

``/select/group/monitoring *state*``
   where *state* is an int which sets the monitoring sharing of the group the strip belongs to.

``/select/recenable *y/n*``
   Where *y/n* is ``1`` for enabled and ``0`` for disabled

``/select/record_safe *y/n*``
   Where *y/n* is ``1`` for safe and ``0`` for unlocked

``/select/mute *y/n*``
   Where *y/n* is ``1`` for enabled and ``0`` for disabled

``/select/solo *y/n*``
   Where *y/n* is ``1`` for enabled and ``0`` for disabled

``/select/solo_iso *state*``
   where *state* is a bool/int representing the desired solo isolate state of the track

``/select/solo_safe *state*``
   where *state* is a bool/int representing the desired solo safe/lock state of the track

``/select/monitor_input *y/n*``
   Where *y/n* is 1 for monitor from input and ``0`` for auto

``/select/monitor_disk *y/n*``
   Where *y/n* is 1 for monitor from disk and ``0`` for auto

``/select/polarity *invert*``
   where *invert* is a bool/int representing the desired polarity of the track

``/select/gain *gain*``
   Where *gain* is a float ranging from ``-193`` to ``6`` representing the desired gain of the track in dB.

``/select/fader *position*``
   Where *position* is an float ranging from ``0`` to ``1`` representing the fader control position.

``/select/db_delta *delta*``
   where *delta* is a float that will increase or decrease the gain of the selected track by the amount of the delta.

``/select/vca *name* *state*``
   where *name* is a string with the name of the VCA, and *state* is an int that determines if the named VCA will control this strip.

``/select/vca/toggle *name*``
   where *name* is a string with the name of the VCA. This toggles the use of the named vca with this strip. Any trailing ``[_]`` will be ignored.

``/select/spill``
   show only strips this strip is grouped with or those that feed this bus or that this vca controls.

``/select/*/automation *mode*``
   where *mode* is an int ranging from ``0`` to ``3`` representing the desired automation mode for the control.

``/select/*/touch *state*``
   where *state* is an int of ``1`` for touched and ``0`` for released.

``/select/trimdB *trim_db*``
   where *trim_db* is a float ranging from ``-20`` to ``20`` representing the desired trim of the track in dB.

``/select/pan_stereo_position *position*``
   where *position* is a float ranging from ``0`` to ``1`` representing the desired pan position of the track

``/select/pan_stereo_width *width*``
   where *width* is a float ranging from ``0`` to ``1`` representing the desired pan width of the track

``/select/pan_elevation_position *position*``
   where *position* is a float ranging from ``0`` to ``1`` representing the desired pan elevation of the track

``/select/pan_frontback_position *position*``
   where *position* is a float ranging from ``0`` to ``1`` representing the desired front to back position of the track

``/select/pan_lfe_control *value*``
   where *value* is a float ranging from ``0`` to ``1`` representing the desired LFE control value for the track

``/select/send_gain *sendid* *send_gain*``
   where *sendid* = nth_send, *send_gain* is a float ranging from ``-193`` to ``+6`` representing the desired gain in dB for the send

``/select/send_fader *sendid* *send_gain*``
   where *sendid* = nth_send, *send_gain* is a float ranging from ``0`` to ``1`` representing the desired position for the send as a fader

``/select/send_enable *sendid* *state*``
   where *sendid* = nth_send, *state* is ``1`` for enabled and ``0`` for disabled

``/select/send_page *delta*``
   where *delta* is an int or float selecting another send as a delta from the current send.

Let me know if you need the next table or want this broken into sections.

``/select/send_page`` and ``/select/plugin_page`` may be used with a
page up and page down switch by using a switch with a value of ``1`` for
page up and a switch with a value of ``-1`` for page down. An encoder
can be used as well.

.. _osc_plugins:

Selected Plugin Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~

These operations control the selected plugin on the selected strip.
Plugins and parameters are specified by their position in the list of
plugins and controllable parameters. Parameters are paged to allow
accessing all parameters on a surface with limited inputs, the plugin
(parameter) page size is configured with ``/set_surface``.

When the selected strip is changed, the plugin in the same position in
the newly selected strip is made the selected plugin (even if it is a
different type of plugin). If the new strip has fewer plugins, the last
plugin is selected. If the new strip has no plugins, no plugin is
selected.

Here is the converted definition list from the table you provided:

``/select/plugin *delta*``
   where *delta* is an int or float selecting another plugin as a delta from the currently selected plugin index.

``/select/plug_page *up_or_down*``
   where *up_or_down* is ``1`` for page up or ``-1`` for page down (``0`` is ignored).

``/select/plugin/activate *y/n*``
   where *y/n* is ``1`` for activating and ``0`` for deactivating the selected plugin.

``/select/plugin/parameter *piid* *paid* *value*``, ``/select/plugin/parameter *paid* *value*``, ``/select/plugin/parameter/*piid*/*paid* *value*``, ``/select/plugin/parameter/*paid* *value*``
   where *piid* = nth plugin, *paid* = nth parameter, and *value* is a
   float from ``0`` to ``1``. If *piid* is omitted, the currently selected
   plugin is used. Otherwise, the specified plugin is made the selected
   plugin and its parameter modified. Feedback messages omit the *piid*
   argument. The *paid* is normally passed as an argument (second form)
   but can be put in the path (last form) using the
   ``/set_surface/feedback`` state command. See :ref:`Calculating
   Feedback and Strip-types Values.
   <osc58_feedback_and_strip_types_values#feedback>`

Let me know if you'd like this broken out further or formatted
differently!

The *paid* argument is specified as a 1-based index into the list of
*controllable* parameters only (as specified by the controllable flag in
the :ref:`/strip/plugin/descriptor query message
<osc58_querying_ardour>`, skipping non-controllable-only parameters).

.. _osc_groups:

Using groups with strip and select
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No grouping will occur unless ``use_group`` is set either by using
``/set_surface/strip_types`` with the use groups bit set or by using
``/use_group i 1``.

The result for ``/strip/group`` or ``/select/group`` is determined by the
parameter passed in the command and the current group and available list
of groups. The group name the control surface sends may be:

-  "none", "" or " " will remove this strip from this group. If this was
   the only strip in this group, the group is deleted. Some OSC
   controllers have trouble sending an empty string and a list of groups
   contains "none" as well so a dropdown can just send a text item and
   work.
-  The name of a group this strip does not belong to will remove this
   strip from it's current group and add it to the named group. If this
   strip was the only strip in the group it was removed from, that group
   will be deleted.
-  An unused name when this strip is not part of a group will create a
   new group with the group name sent and add this strip to that group
-  An unused name when this strip is already a part of a group will
   rename this group to the name sent.

To create a new group from a strip that is already joined to a group,
the strip must first remove itself from the current group.

.. _osc_spill:

Spill Strips
^^^^^^^^^^^^

``/select/spill`` or ``/strip/spill`` will:

-  set the current set of strips in use to include only the strips that
   are a part of the group the strip is a part of so long as that strip
   is a track.
-  set the current set of strips to the set of strips that feed this
   strip if it is a bus. In the case where this strip is being fed by
   sends rather than strip outputs, the strips that feed this bus will
   have their names set to the name of the strip with ``-send`` appended
   to it and the fader, pan and mute will control the send rather than
   the strip. The other strip controls will be disabled in this mode.
   This only happens when the strip that calls spill is a bus. In the
   case where a strip that is part of a group is chosen as above where
   the group all sends to a common bus this will not happen. This can be
   useful for a group that uses "Add New Aux Bus" to switch from sends
   to faders.
-  set the current set of strips to the set of strips that are
   controlled by the VCA if this strip is a VCA.

``spill/group``, ``spill/bus`` or ``spill/vca`` can also be used to
force the type of spilling that is done. This may be useful if the strip
is a bus that is a part of a group and the group variation is required.

In all cases, if there is a bus or VCA attached to the group of strips
it will be included as well.

What is less obvious, is how to return to the normal set of strips.
There are a number of ways of doing so depending on the operator's
wishes. The most obvious way is to use ``/set_surface/strip_types`` to
set the strip list as desired. It is expected that a control surface may
have more than one strip types button in any case to see only inputs or
only busses etc and of course one to give a full mix. Another option is
to reselect the custom set of strips with ``/strip/custom/mode *mode*``.

.. _osc_plugins_details:

Controlling plugins
^^^^^^^^^^^^^^^^^^^

.. _osc_menu:

Menu actions
~~~~~~~~~~~~

Every single menu item in Ardour's GUI is accessible via OSC. There is a
single common syntax to trigger the action as if it was selected with
the mouse (or keyboard):

``/access_action *action_name*``

``access_action`` can be inlined for control surfaces that are unable to
send string parameters. The ``action_name`` is composed of a group and
an action in the form of ``Group/action`` which fits very well as an OSC
path extension:

``/access_action/*Group/action* *key_pressed*``

The key_pressed is optional, but if present is a float ``1`` or ``0``
where the command is ignored if ``key_pressed`` is ``0``.

Some of the Menu Actions duplicate other OSC commands. In all cases it
is better to use the OSC commands rather than the Menu Actions if
possible as the OSC commands are more direct.

The :ref:`list of actions <list_of_menu_actions>` shows all available
values of ``action-name`` for Ardour.
