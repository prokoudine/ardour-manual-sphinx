.. _toolbox:

Toolbox
=======

.. figure:: images/toolbar-tools.png
   :alt: Editor toolbar's tools, aka toolbox
   :width: 66.0%

   Editor toolbar's tools, AKA toolbox.

.. _toolbox_global_edit_mode:

Global Edit mode
----------------

Ardour has a global Edit Mode selector at the left side of the Editing toolbar, which affects how regions are moved or copied:

Slide
   Regions move freely. Ardour creates overlaps when necessary.
Ripple
   Editing affects the regions to the "right" of the edit (see below).
Lock
   No region motion is permitted (except for "nudge").

The general idea behind the Ripple edit mode is this:

-  Deleting a range will move later regions to compensate for the deleted time
-  Deleting a region will move later regions to compensate for the deleted region's length
-  Moving a region will move later regions to compensate for the length of the move
-  Inserting a new region (via dragging or via Paste) will move later regions to the right to compensate

Within this general behavior several variations are available as Ripple edit modes:

#. **Selected**. Only applies the ripple logic to currently selected tracks. After making a selection, you can use the :kbd:`Alt` modifier and click on tracks to add or remove them to/from the selection. Markers will stay intact.
#. **All**. Applies the ripple logic to all tracks on the timeline and shifts location, CD, and cue markers accordingly. Selecting a range with this mode will automatically make a time-constrained selection in all tracks of the project.
#. **Interview**. This mode works just like the **Selected** mode with one exception: when you select a range and press :kbd:`Del`, this will remove the selected portion of either audio or MIDI without shifting other clips to the left to match the freed space on the timeline. The main use case for this mode is editing interviews where you want the ripple behavior to edit out e.g. periods of silence, while being able to just delete e.g. an out-of-place noise or an exclamation by the interviewer.

.. note::
   If **Snap To Grid** is enabled, then regions can only move so that they align with locations determined by the current snap settings (beats, or seconds, or other region boundaries, etc). See :ref:`Snap To the Grid <grid_controls>` for details.

.. _toolbox_edit_point:

The edit point selector
-----------------------

Numerous editing operations require the definition of an edit point, that is chosen in this selector. More information about the Edit Point can be found :ref:`here <toolbox_edit_point_control>`.

.. _toolbox_smart_mode:

The Smart mode toggle switch
------------------------------

The Smart mode toggle button (shortcut: :kbd:`y`) to the left of the mouse mode buttons modifies the behavior of Grab Mode: when enabled, the mouse behaves as if it is in Range mode in the upper half of a region, while behaving as if it is in Grab mode in the lower half. This makes it possible to avoid constant switching between these two modes.

.. _toolbox_mouse_mode:

Mouse modes
-----------

Editing :ref:`regions <working_with_regions>` and their contents is very complex and, by virtue of this, requires different mouse modes in order to be able to perform typical editing chores in a way that is powerful and makes sense.

============= =====================
**Mode**      **Keyboard Shortcut**
Grab          :kbd:`G`
Range         :kbd:`R`
Cut           :kbd:`C`
Audition      None
Stretch       :kbd:`T`
Grid          :kbd:`Y`
Draw          :kbd:`D`
Internal Edit :kbd:`E`
============= =====================

.. note::
   Changes to the mouse pointer only occur when hovering over the track canvas; the mouse pointer *always* changes to a hand in the ruler area regardless of what mode is selected, and always moves the :ref:`playhead <controlling_playback>` to the position left-clicked on—as long as there is no marker or other tag under the mouse position clicked on.

.. _toolbox_grab:

Grab Mode
~~~~~~~~~

Grab mode is used for selecting, moving, deleting and copying objects. In this mode, the mouse pointer appears as a hand and can be used to select and perform various operations on objects such as regions, markers etc…. This is the most common mode to work in, as it allows the for selection and moving of :ref:`regions <working_with_regions>`, as well as the modification of control points in :ref:`automation lanes <automation_lanes>`.

.. _toolbox_range:

Range Mode
~~~~~~~~~~

In Range mode, the mouse pointer appears as a vertical line; left-clicking on the track canvas will display the time at the position clicked on. left-clicking and dragging on the track canvas will create a time range for the track clicked and dragged on; adjacent tracks can be selected as well by dragging the mouse into them. Once a time range has been defined, it can be resized by left-clicking on either the left-hand or right-hand side of the range and dragging the mouse to the desired position.

.. _toolbox_cut:

Cut Tool Mode
~~~~~~~~~~~~~

In Cut Tool mode, the mouse pointer appears as a pair of scissors and allows for the separation of any region into two distinct regions by left-clicking at the desired point of separation. If more than one track is selected, then all the regions on the selected tracks will be split at the point clicked on. If no track is selected, then only the region hovered by the mouse cursor will be split.

.. _toolbox_stretch:

Stretch Mode
~~~~~~~~~~~~

In Stretch mode, the mouse pointer appears as an expanding square symbol and is used to resize regions using a timestretch algorithm. Resizing a region is done by left-clicking on the right-hand side of the region and dragging the edge to the desired position; once the button is released a **Time Stretch Audio** dialog will appear, as detailed in the dedicated `Stretching <@@stretching>`__ page.

.. _toolbox_audition:

Audition Mode
~~~~~~~~~~~~~

Left-clicking on a given region using Audition Mode will play the the session for the time span of that region. The regions can also be **scrubbed** by left-clicking and dragging in the direction desired; the amount dragged in one direction or the other will determine the playback speed.

.. _toolbox_grid:

Grid Mode
~~~~~~~~~

The Grid mode has been designed to easily create and edit tempo maps.

Left-clicking on the timeline above a bar line creates a new tempo marker.

.. video:: videos/grid-tool-add.mp4
   :width: 100%

Left-clicking and dragging on the timeline above a bar line when a tempo marker already exists in that position changes the value of the current and the previous markers to accomodate for.

.. video:: videos/grid-tool-edit.mp4
   :width: 100%

Left-clicking and dragging on the timeline anywhere between two bar lines creates a tempo ramp.

.. video:: videos/grid-tool-create-ramp.mp4
   :width: 100%

.. _toolbox_draw:

Draw mode
~~~~~~~~~

In Draw mode, the mouse pointer will change to a pencil; the effect it will have depends on the type of track or region it is utilized in.

In an :ref:`audio track <audio_track_controls>`, a green line will appear in the region which is that region's :ref:`gain envelope <gain_envelopes>`. left-clicking anywhere in a given region between two existing control points will add one to the region at the X-coordinate clicked on with the Y-coordinate being on the line connecting the control points on either side of the new one. left-clicking on a control point will allow it to be moved to any point in the region in between the control points that bound it on either side of itself. And finally, left-clicking on a control point and pressing the :kbd:`Del` key or holding down the :kbd:`Shift` key while right-clicking on it will delete the control point.

In an :ref:`automation lane <automation_lanes>`, if any automation is defined in it, a green line connecting its control points will appear in the lane. Control points in the lane are manipulated in exactly the same way as they are in a region's gain envelope (see previous paragraph for details).

In a :ref:`MIDI track <midi_track_controls>`,

-  :left-clicking in a part of the track that has no region, creates a one-bar long region, while :left-dragging will create a region of arbitrary length.
-  :left-clicking on a region in Percussive mode creates a diamond indicating a hit.
-  :left-clicking on a region in Sustained mode creates a note whose duration is one :ref:`Grid unit <grid_controls>`, while left-dragging creates a note of arbitrary Grid units length.

.. _toolbox_edit_internal:

Internal Edit Mode
~~~~~~~~~~~~~~~~~~

In the **Internal Edit** mode, the mouse pointer will change to cross-hairs.

-  On an automation lane, it allows to edit the automation like the Draw tool.
-  On a MIDI region, it allows to lasso-select multiple notes at a time.
-  On an audio region, it displays the current level of the signal and allows to edit the region gain like the Draw tool.
