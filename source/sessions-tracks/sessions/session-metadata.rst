.. _session_metadata:

Session metadata
================

.. figure:: images/edit-session-metadata.png
   :alt: The session metadata editor
   :class: right-float

Sessions can have various items of metadata attached to them, and saved in the session file. These metadata are filled by the user via **Session > Metadata > Edit Metadata…**.

These metadata will be exported as tags in the audio and video files that support it, as long as the right option is chosen at the :ref:`export <export_dialog>` stage. All the video format can retain a subset of the metadata if the **Include Session Metadata** is checked in the :ref:`export video <workflow_operations_export>` window, while only the Ogg-Vorbis (tagged) and FLAC (tagged) audio format will be exported with the metadata (as Vorbis comment).

Ardour can also reuse the metadata from another session file in the current session, with **Session > Metadata > Import Metadata…**. This menu brings up a file selector, asking for the source ardour session file to extract the data from. This can be handy when reusing a lot of information (Author, Artist Name, etc…) or working on multiple tracks of the same media.
