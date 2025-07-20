.. _midi_scene_automation:

MIDI scene automation
=====================

Ardour is capable of being used to both record and deliver MIDI "scene"
automation. These are MIDI messages typically used to switch presets or
"scenes" on a variety of external equipment (or software), including
lighting and other audio/video tools. A common use case is to
automatically change presets between songs or to change lighting
conditions based on a specific position on the timeline.

Each change from one scene to another is represented by a marker in the
"Marker" bar.

Typically, scene changes are delivered as a combination of bank and
program change MIDI messages. MIDI allows for 16384 banks, each with 128
programs.

Recording scene changes
-----------------------

Ardour has a dedicated MIDI port named **Scene In**. Recording scene
changes can be done by connecting this port to whatever source(s) of
MIDI scene (bank/program change) messages should be recorded.

Whenever the global record enable button is engaged and Ardour's
transport is rolling, a new marker will be created for each scene change
message received via the "Scene In" port.

If two different scene changes are received within a certain time
period, only the later one will be recorded as a new marker. The default
threshold for this is ``1`` millisecond.

If a scene change message is received while the playhead is close to an
existing marker with an associated scene change, the recording process
will alter the scene change in the existing marker rather than adding a
new one. The default threshold for this "proximity" test is ``1``
millisecond.

Manually creating scene changes
-------------------------------

This feature is not currently implemented.

Playing back scene changes
--------------------------

Ardour has a dedicated MIDI port named **Scene Out**. Playing back scene
changes can be done by connecting this port to whatever target(s) of
MIDI scene (bank/program change) messages should be sent to.

When the global record enable button is *not* enabled, the relevant
message(s) will be sent via the "Scene Out" port as the playhead rolls
past each marker with a scene change associated with it.

Editing scene changes
---------------------

This feature is not currently implemented.

Disabling scene changes
-----------------------

This feature is not currently implemented.
