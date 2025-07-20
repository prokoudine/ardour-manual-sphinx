.. _note_splitting_joining:

Note splitting and joining
==========================

It is possible to evenly split (tuple) and join notes in both the
**Draw** and the **Internal Edit** modes.

Splitting notes
---------------

To split a note or a group of notes into tuplets, first select the
notes.

.. figure:: images/note-split-select.gif
   :width: 50.0%

Press :kbd:`S` to split selected notes into two tuplets. In the example
below, each note with a duration of two whole notes will be split into
two notes, each with a duration of one whole note. For each newly
created note, Ardour will display its velocity inherited from the
original notes.

.. figure:: images/note-split-into-two.gif
   :alt: Split notes into two
   :width: 50.0%

Repeatedly pressing :kbd:`S` will increment the amount of tuplets. Thus, the
next key press will divide the original note into 3 notes 2 and 2/3
beats long each, then 4 notes 2 beats long each etc. Ardour will display
a temporary message at the bottom of the MIDI region to tell how many
subdivisions have been created.

.. figure:: images/note-split-sequential.gif
   :width: 50.0%

To stop incrementing the amount of subdivisions, deselect notes by
clicking elsewhere in the MIDI region or by pressing :kbd:`Esc`.

Joining notes
-------------

To join several notes into one, select the notes, then press J:

.. figure:: images/note-join-simple.gif
   :alt: Joining adjacent notes
   :width: 50.0%

If non-adjacent notes are selected, and there is a blank space between
them, the note will extend from the beginning of the earliest note to
the end of the latest note and fill the blank spaces with itself:

.. figure:: images/note-join-extend.gif
   :alt: Joining and extending notes
   :width: 50.0%

If non-adjacent notes are selected, and there is at least one note
between them, newly created note will overlay the existing note:

.. figure:: images/note-join-overlap.gif
   :alt: Joining non-adjacent notes
   :width: 50.0%
