.. _corresponding_regions_selection:

Corresponding regions selection
===============================

:ref:`Track Groups <the_track_and_bus_group_list>` have a property
titled **Select** which, if enabled, cause Ardour to propagate a region
selection in one track of a group to the **corresponding regions** of the
other tracks in that group.

This can be particularly useful when an instrument has been recorded
using multiple microphones (e.g. a drumkit): by enabling the **Select**
property for the group, selecting a region in one of the tracks, Ardour
will select the corresponding region in every other track of the group,
which in turn means that a subsequent edit operation will affect all the
tracks together.

How Ardour decides which regions are "corresponding"
----------------------------------------------------

Regions in different tracks are considered to be corresponding for the
purposes of sharing **selection** if they satisfy *all* the following
criteria:

#. each region starts at the **same offset** within its source file,
#. each region is located at the **same position** on the timeline, and
#. each region has the **same length**.

Overlap correspondence
----------------------

Sometimes, the rules outlined above are too strict to get Ardour to
consider regions as corresponding. Regions may have been trimmed to
slightly different lengths, or positioned slightly differently, and this
will cause Ardour to not select regions in other grouped tracks.

In this case, changing **Edit > Preferences > Editor > Regions in active
edit groups are edited together**: to **whenever they overlap in time**
will allow regions in different tracks to be considered equivalent for
the purposes of selection if they overlap. This is much more flexible
and will cover almost all of the cases that the fixed rules above might
make cumbersome.
