Configuring MIDI
================

MIDI is a way to describe musical performances and to control music hardware and software.

Ardour can import and record MIDI data, and perform a variety of editing operations on it. Furthermore, MIDI can be used to control various functions of Ardour.

MIDI input and output for Ardour are handled internally by the same "engine" that handles audio input and output. However, Ardour can use as many MIDI devices as the system can see as there are no syncing difficulties as there would be with audio.

Linux
   **ALSA MIDI** is the standard MIDI framework on Linux systems.
Windows
   **MME** is the standard MIDI framework on Windows systems.
macOS
   **CoreMIDI** is the standard MIDI framework on OSX systems.

.. note::
   JACK is an alternate audio system which Ardour can utilize for both audio and MIDI. JACK is used to route audio between independent applications, and is now considered an advanced use case which is not recommended for most users. Users with a need to use JACK for audio routing should consult the latest documentation at the `JACK website <https://jackaudio.org/>`__.

Read below for details:

.. toctree::
   :maxdepth: 1

   midi-on-linux
   midi-on-os-x