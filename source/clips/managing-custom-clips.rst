.. _managing_custom_clips:

Managing the custom clips
=========================

.. _managing-custom-clips-folder:

Managing the custom clips folder
--------------------------------

Ardour currently does not provide a way to reorganize clips in the main
custom folder. For the time being, it is suggested to use a file manager
to manage the folder.

As all the clips you already added to the project have been copied, you
do not need to close Ardour to reorganize clips in the custom clips
folder. Feel free to create new subfolders and move files around. All
the changes will be reflected in the clips browser after you switch to
another folder and back.

You do not need a fast drive for custom clips folders. Playing back a
short clip will have little impact on the performance, and copying a
file into the project should be likewise fast even from a hard disk. You
can even use a network drive to store and access all your clips and
loops.

.. _adding_custom_clips:

Adding custom clips
-------------------

There are three major ways to add new clips to your custom **Clips**
folder.

#. In the Editor window, drag a region from the list of regions to the
   Clips tab. Ardour will automatically switch to the Clips tab, display
   the main custom clips library, and let you drop the region there.
#. In the Editor window, use the right-click menu to bounce a region or
   a range to the Clips library. You can bounce either processed (with
   all effects) or unprocessed (sans all effects) version of the audio
   data. The option to bounce to the clips library will be available in
   the bounce dialog. Additionally, if the track in question is visible
   in the Cue window, you can automatically insert a bounced clip into
   the slot of a particular scene for that track.
#. You can use the file manager to navigate to the location of the
   custom clips library and place audio and/or MIDI files there.

Changes will take effect in Ardour once you switch to another folder and
back.

.. _removing_custom_clips:

Removing custom clips
---------------------

#. Use a file manager to navigate to your main custom clips folder.
#. Locate the file you do not need any more, remove it to the trash bin.

Likewise, changes will take effect in Ardour once you switch to another
folder and back.
