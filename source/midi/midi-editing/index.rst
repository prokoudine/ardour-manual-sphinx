.. _midi_editing:

MIDI editing
============

Ardour's handling of MIDI and how it allows the editing of MIDI data differs in key ways from most other DAWs and MIDI sequencers. Also, unlike its handling of audio data, the editing of MIDI data in Ardour is necessarily destructive by nature.

Here are the key features of MIDI editing in Ardour:

- All editing is done in-place, in-window; there is no separate piano
  roll window or pane. Notes are edited right where they appear.
- Editing note information in Ardour occurs in only a single region.
  There is no way currently to edit note data for multiple regions at
  the same time; so, for example, notes cannot be selected in several
  regions at once and then all deleted. However they can be copied and
  pasted from one region to another.
- Every MIDI track has its own MIDI port for input; it may have an
  arbitrary combination of audio and MIDI outputs, depending on the
  signal processing in the track.
- Full automation for MIDI tracks, integrated with the handling of all
  MIDI CC data for each track.
- Controllers (CC data) can be set to discrete or continuous modes (the
  latter will interpolate between control points and send additional
  data).
- There is a Normal and a Percussive mode for note data editing.
- The visible note range is controlled by a **scroomer** widget, which
  is a combination scroll/zoom tool for altering the zoom level and
  range of visible MIDI data. When in internal edit mode, you can also
  use scroll operations to adjust the visible range in various ways.

.. toctree::
   :maxdepth: 1
   :caption: Contents

   controlling-midi-range.rst
   add-new-notes.rst
   handling-overlapping-notes.rst
   note-selection.rst
   note-cut-copy-and-paste.rst
   note-splitting-joining.rst
   change-note-properties.rst
   midi-velocity-editing.rst
   patch-change.rst
   midi-region-copies.rst
   quantize-midi.rst
   transposing-midi.rst
   midi-list-editor.rst
   transform-midi.rst

   