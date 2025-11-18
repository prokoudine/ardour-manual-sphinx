.. _add_new_notes:

Adding new notes
================

MIDI notes can be added a few different way in Ardour:

.. _add_new_notes_using_the_mouse:

Using the mouse
---------------

Drawing notes with the mouse requires that a MIDI track
:ref:`exists <create_midi_tracks>`, and a blank MIDI region has been
:ref:`created <create_midi_regions>` in this track.

In the **Draw** `mode <toolbox>`, new notes can be added with a click or
a click-and-drag: a mouse *click* creates a note at the pointer location
(or the nearest grid anchor if grid is enabled), and its duration is one
:ref:`Grid unit <grid_controls>`. A mouse *drag* creates the note like a
click does, but allows continuously setting the duration of the note
until the mouse button is released.

It's also possible to *brush notes* by pressing Shift,
clicking, and dragging to the right.  New notes will be painted at an
interval defined by global  quantization, with the length defined in the
editor toolbar (see below).

The toolbar available in the Draw mode helps drawing notes of exact
length, in a certain MIDI channel, with predefined velocity:

.. figure:: images/midi-draw-toolbar.png
   :alt: MIDI draw toolbar

   MIDI draw toolbar

While the Velocity drop-down list only displays presets, you can hover
it and use mouse wheel scrolling to increment the current value by 1.
Scrolling above the other two drop-down lists will cycle through the
presets.

The Auto option in three drop-down lists works differently in all three
cases:


Length
   The length will be defined by the grid snapping setting

Channel
   This value will be inherited from the closest note

Velocity
   The value will be an interpolation between two closest notes, the position of the newly added note relative to either of the two notes will also be taken into consideration

.. _add_new_notes_using_step_entry:

Using step entry
----------------

The :ref:`Step Entry editor <step_entry>` allows to enter a melody in
sequence along time, using a virtual keyboard and specific controls. It
can be a very handy and fast way to create MIDI lines, in a kind of
typewriter way, all the more when using its different keyboard
shortcuts.

The **Step Entry** window is shown by right clicking the record button in
the :ref:`MIDI track header <midi_track_controls>` and selecting **Step
Entry**. This will automatically create a MIDI region to type into at
the playhead position, which will automatically expand at each step.

.. _add_new_notes_using_the_virtual_keyboard:

Using the virtual keyboard
--------------------------

The :ref:`Virtual MIDI Keyboard <virtual_keyboard>`—or a real MIDI
keyboard plugged in as the tracks input—can be used to record MIDI, as
a microphone would record audio.

It can be started by choosing the **Window > Virtual Keyboard** menu.
Exactly like for audio recording, the track(s) must be armed for
recording, the main record engaged, then the transport started. As for
the step entry, a MIDI region will be auto-generated at the playhead
position, and expanded as long as the recording lasts.
