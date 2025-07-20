.. _adding_clips_to_the_cue_grid.rst

Adding clips to the cue grid
============================

Adding tracks
-------------

It's possible to add tracks in the Cue window the usual way, either by
double-clicking on the free space in the canvas or by choosing the **Track
> Add Track, Bus, or VCA** menu item. The important part is to enable the
**Show on Cue Page** checkbox in the newly opened dialog.

Alternatively, it's possible to drop an existing audio or MIDI file into
the empty part of the canvas to automatically create the cue track and
fill the first empty trigger slot with it.

Trigger slots not only work as a drag-and-drop target, they also work as
a drag-and-drop sources. It's possible to drag the contents of an
existing trigger slot into the empty part of the canvas to create a new
track and fill the first slot with the contents of the original slot.
It's also possible to drag and drop the contents of one slot into
another in case one wants to use the same clip with some variations
(e.g. a custom follow length).

Loading clips to slots
----------------------

There are several ways to load a clip into a trigger slot:

-  From right click menu: right-click over a trigger slot, choose **Load**,
   select an audio or a MIDI file.
-  From **Clip Properties** box: click the **Load** button, select an audio or a
   MIDI file.
-  From the **Clips** library: choose an audio or a MIDI file, listen to it
   before adding, then pick, drag towards the grid and drop into a
   trigger slot.
-  From the **Regions** list: choose a region, drag it towards the grid and
   drop it into a trigger slot.
-  From the timeline: select a region, right-click, choose **{Region Name}
   > Bounce (with processing)** or **{Region Name} > Bounce (without
   processing)**, then enable the Bounce to **Trigger Slot** checkbox and
   choose the cue.
-  Using bounce to create and name new clips will keep the **Cue Track**
   title and **Cue Clip** names easily recognizable.

The type of data must match the type of tracks a clip is being inserted
to. E.g., it's impossible to place a MIDI clip into a trigger slot of an
audio track.

Clearing trigger slots
----------------------

There are two ways to remove an assigned clip from a selected trigger
slot:

#. Pressing **Delete** or **Backspace**
#. Right-clicking on the trigger slot and selecting **Clear** in the menu.
