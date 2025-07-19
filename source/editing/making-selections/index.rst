.. _making_selections:

Making selections
=================

Many editing operations in Ardour require to first **select one or more
regions** to change them in some way. A single region, or multiple regions
can be selected, including regions in different tracks. When a region is
selected, it will appear in a darker color than unselected regions.

If a track is a member of a group that is active and has the **Select**
property enabled, then Ardour will attempt to match whatever selections
is made in one track across every other track of the group. See
:ref:`Corresponding Regions Selection <corresponding_regions_selection>`
for more information on precisely how selections will be propagated to
other tracks.

Track selection
---------------

Tracks are **selected** by clicking on the Track header at the left of
the Editor window. Multiple tracks can be selected with
:kbd:`Ctrl`-left-clicks, or a range of consecutive tracks with
:kbd:`Shift`-left.

Region selection
----------------

Using the :ref:`Grab Mode tool <toolbox>`, left clicking on a region
selects it. If :ref:`Smart mode <toolbox>` is enabled, the lower half of
the region must be clicked.

Deselecting a region
--------------------

Still using the :ref:`Grab Mode tool <toolbox>`,
:kbd:`Ctrl`-left-clicking the region deselects it. If :ref:`Smart mode
<toolbox>` is enabled, the lower half of the region must be clicked.

Note that a :kbd:`Ctrl`-left-click simply toggles the selected status of an object,
so it can be used to select unselected regions too.

Selecting multiple regions in a track
-------------------------------------

This can be achieved in different ways:

-  :kbd:`Ctrl`-left-clicking each region.
-  Dragging a rubberband box from an empty point in a track before the
   first region to select to a point within or after the last region to
   select. Using :kbd:`Ctrl`-left-drag allows doing it multiple times.
-  If the regions are all adjacent to one another, clicking the first
   region to select, then :kbd:`Shift`-left-clicking the last one.

Selecting all regions in a track
--------------------------------

The **Select > Select All In Track** option in the context menu
(right-click on the track) selects all the regions in the track at once.

See the :ref:`Track Context Menu <track_context_menu>` for more
information on other per-track selection operations that are available.

Selecting multiple regions across different tracks
--------------------------------------------------

This can be achieved by a :kbd:`Ctrl`-left-click or
:kbd:`Shift`-left-click on the regions to select.

Selecting a region from the region list
---------------------------------------

Clicking the name of the region in the :ref:`Region List
<the_region_list>` selects it. This will do nothing for whole-file
regions, since they do not exist anywhere in a playlist or track.
