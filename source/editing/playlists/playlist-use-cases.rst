.. _playlist_use_cases:

Playlist use cases
==================

Using playlists for parallel processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the uses of playlists is to apply multiple effects to the same
audio stream. For example, applying two different non-linear effects
such as distortion or compression to the same audio source (linear
effects can be just applied one after the other in the same track) can
be done by creating a new track, applying the original track's playlist,
and then applying effects to both tracks independently.

.. note::
   The same result could be achieved by feeding the track to multiple
   busses which then contain the processing, but this increases the overall
   latency, complicates routing and uses more space in the Mixer window.

Using playlists for "takes"
---------------------------

Using playlists for **takes** is a good solution when one needs the ability
to edit individual takes, and select between them.

Each time a new take is started, a new playlist should be created with **p
> New**. Thus, later, any previous or later takes can be selected as
desired.

Creating a composite edit from multiple takes, can be achieved either:

-  by creating a new track to assemble the final version, and "cherry
   picking" from the playlists in the original track by copying regions
   over as required
-  by recording each successive take on top of the others in "layers"
   and then editing them using the layer tools.

Using playlists for multi-language productions
----------------------------------------------

The same approach as for takes is useful when recording or editing
content in multiple versions, such as dubbed movie dialog in several
languages: having all versions on the same track allows to apply the
same processing, making it easy to switch language before exporting the
session.
