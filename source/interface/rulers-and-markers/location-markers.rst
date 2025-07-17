.. _location_markers:

Location markers
================

Location markers appear in the :ref:`Locations Markers <ruler>` ruler at the top of the timeline. They have multiple uses, most commonly—for navigation in a session, e.g. where this or that instrument should start/stop playing. Custom markers can be created at any position in a session.

The start and end markers, that define the length of the session, appear automatically once any content has been added to the session (either recorded or imported). The end marker automatically shifts to the right once more material gets added.

Creating location markers
-------------------------

There are multiple ways to create custom markers at the current playhead position:

-  using the keyboard shortcut (default is :kbd:`Tab`)
-  using the **Transport > Markers > Add Mark from Playhead** menu.

Adding a marker at an arbitrary location on the timeline (i.e. not at the playhead position) can also be done either by:

-  right-clicking in the Location Marker ruler, and selecting **Add > Location Marker**, or
-  using the :ref:`Ranges & Marks List <the_ranges_and_marks_lists>`, clicking **New Marker** and using the :ref:`clock widget <editing_clocks>` to set its position.

Moving location markers
-----------------------

Left-clicking and dragging moves a single marker to a new location on the timeline.

It is possible to move multiple markers by the same distance. Left-clicking each marker creates a selection of markers that can be dragged left or right together.

Renaming Location Markers
-------------------------

There are three ways to rename a location marker:

#. Double-click on a marker opens a dialog where a new name can be submitted.
#. Right-clicking on a marker and selecting **Rename…** opens a dialog where a new name can be submitted.
#. Editing and confirming the name by pressing Enter in an entry box in the **Ranges & Marks** sidebar.

Removing Location Markers
-------------------------

There are three ways to remove a location marker:

#. Hovering the marker and pressing :kbd:`Enter`.
#. Right-clicking on a marker and selecting **Remove**.
#. Clicking the x for a marker of choice in the **Ranges & Marks** sidebar.

More options
------------

The context (right-click) menu for location markers has more options
than the ones mentioned above:

Locate to Here
   Moves the playhead to the selected marker.

Play from Here
   Moves the playhead to the selected marker and starts playback.

Move Mark to Playhead
   This changes the position of the selected marker to that of the playhead.

Create Range to next Marker
   This creates a pair of range markers between the selected marker and the next one to the right on the timeline.

Promote to Time Origin
   This makes the position of the chosen range marker the origin time. This is mostly useful when the **Display Delta to Origin Marker** clock mode is enabled to display the difference between current playhead position and the origin time. Absolute time stays unaffected.

Hide
   This hides the selected marker from the ruler until the user chooses to unhide it.

Rename…
   This opens a dialog to rename the marker.

Lock
   This prevents a marker from being accidentally moved elsewhere.
