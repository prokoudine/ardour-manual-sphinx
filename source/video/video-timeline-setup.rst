.. _video_timeline_setup:

Video timeline setup
====================

No configuration is required if everything is to meant be run on a
single machine, and the version of Ardour comes from
[Ardour.org](https://ardour.org). Everything is pre-configured and
included with the download/install.

Single machine
--------------

If Ardour is compiled from source, or installed from a 3rd party
repository, three additional tools will need to be installed manually,
which are used by Ardour to provide video features:

-  xjadeo (the video monitor application):
   `https://xjadeo.sf.net <https://xjadeo.sourceforge.net/>`__
-  harvid (a video decoder used for the thumbnail timeline):
   `https://x42.github.com/harvid/ <https://x42.github.io/harvid/>`__
-  ffmpeg, ffprobe (used to import/export video, extract soundtracks and
   query video information and encode mp3 for export): https://ffmpeg.org

Ardour requires xjadeo ≥ version 0.6.4, harvid ≥ version 0.7.0 and
ffmpeg (known to work versions: 1.2, 2.8.2, 5.0)

The Ardour development team is in control of the first two applications.
ffmpeg however can be a bit of a problem. To avoid conflicts with
distribution packages, Ardour looks for ``ffmpeg_harvid`` and
``ffprobe_harvid``.

All four applications need to be found in ``$PATH`` (e.g. ``$HOME/bin``
or ``/usr/local/bin``). For convenience the binary releases of harvid
include ffmpeg_harvid and ffprobe_harvid. Ardour binaries from
ardour.org do include all relevant tools and most GNU/Linux
distributions also provide those.

Binary releases of the video-tools are available from ardour.org via a
dedicated installer script:
`install_video_tools.sh <https://github.com/Ardour/ardour/blob/master/tools/videotimeline/install_video_tools.sh>`__.

The easiest way to install the video-utilities on Linux is by running
the following line in a terminal:

```
sh -c "$(curl -s -L https://git.io/tVUCkw)"
```

Studio setup
------------

as setting up a proper a/v post-production studio can be a complicated
task, it is advised to read the info in the previous section to get
familiar with the tools involved first. as much as the ardour team
streamlines and simplifies the *single machine* setup, the *studio setup*
is focused on modularity.