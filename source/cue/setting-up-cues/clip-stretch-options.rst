.. _clip_stretch_options:

Setting up stretch options
==========================

Stretching
----------

When loading an audio clip into a trigger slot, Ardour applies some
heuristics to estimate its tempo in beats per minute. Unless a metadata
in the file source provides information,
`minibpm <https://github.com/breakfastquay/minibpm>`__ is used to
analyze and detect the file's BPM.

After tempo is estimated, the clip is time-stretched to match the
session's tempo map. This means that should session's tempo change over
time (in either ramped or constant mode), all audio clips will be
re-stretched to accommodate for that.

Disabling stretching when original clip's tempo doesn't match that of
the session will most of the times make the clip audibly go out of sync
with the beat.

Stretch modes
-------------

Once stretching is enabled, there are several options how to apply it:

-  **Crisp** works best for sounds with fast onset like drums and percussion
-  **Smooth** is best used for sustained notes like pads
-  **Mixed** is for anything in between

BPM
---

This is where the estimated tempo is displayed. It can also be
progressively divided or multiplied by two.

Supposing session's tempo is currently ``120bpm`` and original clip's
tempo is ``90bpm``, stretching the clip to match session's tempo will
make it sound faster that it originally is.

If the estimated clip's tempo is divided by ``2``, stretching the
resulted ``45bpm`` back to ``120bpm`` will make the clip sound faster.
Vice versa, multiplying the original clip's tempo by 2 and then
stretching it down from ``180bpm`` to ``120bpm`` will make the clip
sound slower than it originally is.

Clip length
-----------

This control allows adjusting the estimated tempo in a finer manner, by
changing the amount of beats it takes to play the clip in the selected
trigger slot. The change is immediately displayed in the BPM field
above.

Length in Bars
--------------

This is an estimate of the clip's length as measured in bars for two
popular time signatures: 4/4 and 3/4.
