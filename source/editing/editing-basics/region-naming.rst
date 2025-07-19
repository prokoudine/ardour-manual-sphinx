.. _region_naming:

Region naming
=============

**Region names** are initially derived from either:

-  the name of the track for which they were recorded, or
-  the name of the embedded/imported file they represent.

Whole file region names
-----------------------

These are not audio files, but regions that represent the full extent of
an audio file. Every time a new recording is done, or a new file is
imported to the session, a new region is created that represents the
**entire audio file**. This region will have the name of the
track/playlist/original file, followed by a "-", then a number plus a
dot and then a number.

For **recorded regions**, the number will increase each time a new
recording is made. So, for example, if there is a track called
``Didgeridoo``, the first recorded whole file region for that playlist
will be called ``Didgeridoo-1``. The next one will be ``Didgeridoo-2``
and so on.

For **imported regions**, the region name will be based on the original
file name, but with any final suffix (e.g. ".wav" or ".aiff") removed.

Normally, whole file regions are not inserted into tracks or playlists,
but regions derived from them are. The whole-file versions live in the
:ref:`Editor's region list <the_region_list>` where they act as an
organizing mechanism for regions that are derived from them.

Normal region names
-------------------

When a region is inserted into a track and playlist, its initial name
will end in a **version number**, such as ``.1``. For a recorded region,
if the whole file region was ``Hang drum-1``, then the region in the
track will appear with the name ``Hang drum-1.1``. For an imported
region, if the whole file region was ``Bach:Invention3``, then the
region in the track will appear with the name ``Bach:Invention3.1``.

Copied region names
-------------------

Duplicating or splitting a region creates new region(s) that are based
on the same original files. Hence, they share the same base name (in the
example above, ``Hang drum-1``), but their version number will be
incremented each time. Duplicating ``Hang drum-1.4`` by
:kbd:`Ctrl`-left-dragging it will create a new region called
``Hang drum-1.5``. Splitting ``Hang drum-1.5`` by hitting the :kbd:`S`
key will remove the ``Hang drum-1.5`` region and create two shorter
regions named ``Hang drum-1.6`` and ``Hang drum-1.7``.

Renaming regions
----------------

Regions can be renamed at any time using the region context menu: **right
click > *name_of_the_region* > Rename…**. The new name does not need to
have a version number in it (in fact, it probably should not). Ardour
will add a version number in the future if needed (e.g. if the region is
copied or sliced).
