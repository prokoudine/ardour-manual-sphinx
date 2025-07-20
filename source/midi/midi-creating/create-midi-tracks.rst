.. _create_midi_tracks:

Creating MIDI tracks
====================

A MIDI track is created much like any other track (see :ref:`Adding
Tracks, Busses and VCAs <adding_tracks_busses_and_vcas>`). However,
there are a few things that are unique to creating MIDI tracks.

When adding a MIDI track using the **Add Track/Bus/VCA** dialog, the
**MIDI Tracks** item should be highlighted in the **Template/Type** list
on the left. This will enable the **Instrument** combobox while
disabling the **Configuration** and **Record Mode** comboboxes.

The **Instrument** combobox allows the selection of a plugin for the
track to be created that will generate audio in response to MIDI data;
if the track is intended to drive an external device then **-none-**
should be selected instead.
