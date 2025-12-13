.. _loop_range:

Loop range
==========

The loop range is a special range that defines the start and end points
for loop play, which can be enabled in the transport bar. Loop range
markers show up on the Region Markers ruler.

.. _creating_loop_range:

Creating a Loop Range
---------------------

A loop range can be created in multiple ways.

-  By right-clicking on the Range Markers ruler at the top of the timeline, then selecting **Add > Loop Range**.
-  By selecting a region on the timeline, right-clicking, then selecting **[Region_Name] > Loop**. This will create a loop range's start and end markers matching the beginning and the end of the region, then start playback of the loop range immediately.
-  By selecting a range on the timeline, right-clicking, then selecting **Set Loop from Selection**. This will create a loop range's start and end markers matching the beginning and the end of the range selection respectively.
-  By selecting a range on the timeline, right-clicking, then selecting **Loop Range**. This will create the same loop region and start loop playback immediately.

.. _playing_loop_range:

Playing a Loop Range
--------------------

Playback of the loop range can be triggered the following ways:

-  By clicking the Play loop range button in the Transport toolbar
-  By pressing the L key.
-  By right-clicking on either of the two loop markers and selecting the
   Loop Range menu item.

.. _editing_loop_range:

Editing a Loop Range
--------------------

The loop range can be edited in multiple ways as well.

-  Individual markers can be dragged on the ruler by left-clicking and dragging. It is also possible to drag both the start and the end markers togother. Left-click and select both markers, then drag them.
-  Positions of the start and the end markers can be edited numerically in the :ref:`Ranges & Marks <ranges_and_marks_lists>` sidebar.
-  Positions of the start and the end markers can also be reset from another range selection by making that selection, then right-clicking and selecting the **Set Range from Selection** menu item.

.. _removing_oop_range:

Removing a Loop Range
---------------------

There are two ways to delete a loop range:

#. Right-clicking and selecting the Remove Range menu item.
#. Click the :kbd:`X` button in the list of ranges in the :ref:`Ranges & Marks <ranges_and_marks_lists>` sidebar.

More Options
------------

The right-click menu mostly copies that of a regular pair of range markers. The following options are available in addition to the ones mentioned above.

Play Range
   Starts playback at the left marker in the pair and stops at the right marker.

Locate to Marker
   Moves the playhead to the selected marker.

Play from Marker
   Moves the playhead to the selected marker and starts playback.

Loop Range
   Creates a loop range off the selected range markers pair and starts playback.

Set Marker from Playhead
   Changes the position of the selected marker to that of the playhead.

Zoom to Range
   Changes the zoom so that the area defined by the range markers would be maximized yet visible entirely within Ardour's window.

Loudness Assistant…
   Launches the Loudness Assistant to analyze the selection defined by the selected pair of range markers.

Export Range…
   Exports the selection defined by the selected pair of range markers.

Promote to Time Origin
   This makes the position of the chosen range marker the origin time. This is mostly useful when the **Display delta to origin marker** clock mode is enabled to display the difference between current playhead position and the origin time. Absolute time stays unaffected.

Separate Regions in Range
   Cuts all regions crossing the positions of the range markers.

Select All in Range
   Select entire regions that cross the borders of the range markers.

Select Range
   Create a selection from the range markers in all selected tracks and busses.
