MIDI on macOS
=============

In order for CoreMIDI to work with Jack MIDI, a CoreMIDI-to-JACK-MIDI **bridge** is required. This feature is available on versions equal to or greater than version 0.89 of JackOSX.

Routing MIDI
------------

Inside Ardour
~~~~~~~~~~~~~

MIDI ports show up in Ardour's MIDI connection matrix in multiple locations. Bridged CoreMIDI ports as well as JACK MIDI ports that have been created by other software clients will show up under the :guilabel:`Other` tab. Bridged CoreMIDI hardware ports show up under the :guilabel:`Hardware` tab.

.. _external-apps:

External Applications
~~~~~~~~~~~~~~~~~~~~~

There are multiple options for connecting MIDI ports outside of Ardour.

-  `MIDI Monitor <http://www.snoize.com/MIDIMonitor/>`__ is a handy tool for doing various MIDI-related tasks.
-  `MIDI Patchbay <https://github.com/notahat/midi_patchbay>`__ allows connection of ports and filters MIDI data.
