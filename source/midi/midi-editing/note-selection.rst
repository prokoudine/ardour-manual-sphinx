.. _note_selection:

Note selection
==============

Navigating/Selecting notes with the keyboard
--------------------------------------------

:kbd:`Tab` selects the next note in a MIDI region, while :kbd:`Ctrl-Tab`
selects the previous note. Holding down the :kbd:`Shift` key as well
prevents previously visited notes from being deselected.

Selecting notes with the mouse
------------------------------

While in :ref:`Internal Edit Mode <toolbox>`, any note can be clicked on
to select it. Once a note has been selected, :kbd:`Shift`-left-clicking
on another note selects all notes between the first note selected and
the second one. Adding or removing a note to or from the selection is
done by :kbd:`Ctrl`-left-clicking it. Clicking and dragging outside of a
note will **rubberband select** any notes enclosed by the selection
rectangle; holding down the :kbd:`Shift` key will prevent any previously
selected notes from being deselected.

In any mode, :kbd:`Shift`-left-clicking on a note on the Scroomer (the
piano header of the track, see :ref:`MIDI Track Controls
<midi_track_controls>`) will add all occurrences of that note to the
selection, while middle-clicking will only select/deselect all
occurrences of that note, clearing the previous selection. Scroomer
selections work on all MIDI regions of a track at once.

Listening to selected notes
---------------------------

If **Edit > Preferences > MIDI > Sound MIDI notes as they are selected** is
enabled, Ardour will send a pair of NoteOn/NoteOff messages through the
track as notes are selected. Assuming there is an appropriate device or
synthesizer attached to the track, these should be audible.
