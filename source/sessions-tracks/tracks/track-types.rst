.. _track_types:

Track types
===========

Ardour offers three **track types** depending on the type of data they contain, and differentiates between three **track modes**, depending on their recording behaviour.

Track types
-----------

An Ardour track can be of type **audio** or **MIDI**, depending on the **data** that the track will primarily record and play back. *However, either type of track can pass either type of data.* Hence, for example, one might have a MIDI track that contains an instrument plugin; such a track would record and play back MIDI data from disk but would produce audio, since the instrument plugin would turn MIDI data into audio data.

Nevertheless, when adding tracks to a session, its content is typically known, and Ardour offers three choices:

Audio  
   An **audio track** is created with a user-specified number of inputs. The number of outputs is defined by the master bus channel count (for details see :ref:`Channel Configuration <channel_configuration>`). This is the type of track to use when planning to work with existing or newly recorded audio.

MIDI  
   A **MIDI track** is created with a single MIDI input, and a single MIDI output. This is the type of track to use when planning to record and play back MIDI. There are several methods to enable playback of a MIDI track: add an instrument plugin to the track, connect the track to a software synthesizer, or connect it to external MIDI hardware.

   .. note::
      If an instrument plugin is added, the MIDI track outputs audio alongside MIDI data.

Audio/MIDI  
   There are a few notable plugins that can usefully accept both Audio and MIDI data (Reaktor is one, and various "auto-tune" like plugins are another). It can be tricky to configure this type of track manually, so Ardour allows to select this type specifically for use with such plugins. It is *not* generally the right choice when working normal MIDI tracks, and a dialog will warn of this.

Audio or MIDI Bus  
   A bus is a pseudo-track where multiple audio tracks can be mixed together for some common processing before being routed to the Master bus (which itself is a bus). A bus doesn't contain any regions or audio/MIDI data, it is fed a signal by :ref:`sends <aux_sends>` from one or multiple other tracks, or by :ref:`connecting tracks outputs <audiomidi_busses_mixer_strips>` to the bus' input. Busses are often used to apply one effect on multiple tracks, with the benefits of having the same parameters and less computer processing required as only one instance of the plugin is used.

   Ardour can differentiate audio busses from MIDI busses, allowing e.g. one instrument plugin to be used for several MIDI tracks.

   A bus output can also be routed to another bus.

VCA  
   A VCA is a way to group together tracks or busses to enable grouped-control over gain, solo and mute. Like the bus, it does not contain regions, but unlike it, it does not contain effects either. VCAs are commonly used to group together related tracks (e.g. "drums" or "vocals") to allow controlling the gain of all those tracks at once in the mix while retaining their relative gain. VCAs are fed audio by :ref:`assigning them <control-masters-mixer-strips>` to one or more tracks or busses.
