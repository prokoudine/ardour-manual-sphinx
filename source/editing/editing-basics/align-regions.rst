.. _align_regions:

Align regions
=============

Aligning regions (sometimes called "spotting") means moving one or more
regions based on a defined location, which in Ardour is always the
:ref:`edit point <edit_point_control>`. An alignment operation moves the
region(s) so that some part of the region is positioned at the edit
point. Available alignment commands include:

Align Region starts, :kbd:`Ctrl-Win-a`
   Selected region(s) are moved so that their start is located at the current edit point

Align Region ends, :kbd:`Alt-a`
   Selected region(s) are moved so that the end is located at the current edit point

Align Region sync points, :kbd:`Shift-a`
   Selected region(s) are moved so that their sync point is located at the current edit point

Align Region starts relative, :kbd:`a`
   Selected region(s) are moved so that the start of the earliest region is located at the current edit point, and all others maintain their relative position relative to that region
