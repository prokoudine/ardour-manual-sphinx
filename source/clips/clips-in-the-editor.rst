.. _clips_in_the_editor:

Clips in the Editor
===================

There are two main uses for the Clips browser in the Editor window:

#. Reusing existing clips
#. Creating new clips from content in the timeline

.. clips_reusing_existing:

Reusing existing clips
----------------------

You have two options how to reuse a clip in the Editor.

#. Add to an existing track. Dragging and dropping a clip from the
   browser on an existing track will add this clip to a location on the
   timeline where you released the mouse button, snapping options apply.
   Audio clips can only be placed on audio tracks, MIDI clips can only
   be placed on MIDI tracks. Additionally, placing a single-channel
   (mono) clip on a multi-channel track will create a clip where only
   one channel is filled with the content of the original clip, the rest
   of the channels will be silent.
#. Create a new track. Dragging and dropping a clip below the bottom
   track will create a new track from the clip and name it after the
   clip's file name. Ardour will make a few judgements based on clip
   properties: the track will contain as many channels as the audio file
   has. And for a MIDI clip, Ardour will automatically add the "preview"
   virtual instrument of choice to the processor box.

.. clips_creating_new:

Creating new clips
------------------

You can create new clips for further reuse in the Editor window. Please
see the :ref:`Managing Custom Clips <managing_custom_clips>` page for
more detail.
