.. _fades_crossfades:

Fades and crossfades
====================

Every region has a fade-in and fade-out. By default, the region fade is
very short, and serves to de-click the transitions at the start and end
of the region. By adjusting the regions fade length, a more gradual
transition can be accomplished.

Region Fades
------------

**Region fades** are possible at the beginning and end of all audio regions.
In object mode, a grip appears at the top left and top right of an audio
region when the cursor hovers over it. Placing the cursor over the top
of the grip displays the region fade cursor tip. Clicking and dragging
the grip left or right in the timeline adjusts the length of the fade.

Crossfades
----------

**Crossfades** refer to the behavior of two audio regions transitioning
smoothly (mixing) from one to another on the same track. Historically,
this was done by splicing two pieces of analog tape together, and this
concept was carried forward into digital editing. Each track is a
sequence of sound files (regions). If two regions are butted against
each other, there needs to be a method to splice them smoothly together.
The crossfade allows one region to fade smoothly out, while the next
region fades smoothly in, like two pieces of tape that have been cut at
an angle, and overlapped.

But Ardour uses a more refined "layered" editing model, and therefore it
is possible for multiple regions to be stacked on a single location with
arbitrary overlaps between different layers. For this reason, crossfades
must be implemented differently. It can't be assumed that a crossfade is
an entity that exists between two regions; instead each region must have
its own associated crossfades at each end, and the topmost region must
always crossfade down to the underlying region(s), if any.

Ardour solves this problem by putting a crossfade at the beginning and
end of every region. The fades of the bottom-most region are first
rendered, and then each region is rendered on top of the one below it,
with fades at the end of each region providing a crossfade to the
region(s) beneath it.

It is important to understand that region fades *are* crossfades. When
one region has another region or multiple regions beneath its fade area,
then what will be heard is the topmost region fade-out mirrored as a
fade-in on the underlying region(s). The grip for the topmost region
will allow changing the length and type of the crossfade into the
underlying region(s). In this way complicated series of crossfades can
be created, and then another region layered atop the others, and faded
into a complicated series.

If a region doesn't have any region(s) under it, then the region is
crossfaded to silence; for convenience this is called a "fade" rather
than a crossfade.

Fade Shapes
-----------

.. figure:: images/crossfade_menu.png
   :alt: The fade shape context menu
   :class: right-float

To activate/deactivate or change the shape of a region's fadein or
fade-out, the cursor has to be hovered over the region fade grip until
the cursor tip indicates region fade editing, then right-clicked to
bring up a context menu. In the context menu is a list of options for
the region fade. **Activate/Deactivate** enables and disables the region
fade.

Ardour has a setting for the type of fade that's used by default. It can
be changed in **Edit > Preference > Editor**.

Because each fade is also a crossfade, it has an inverse fade shape for
the audio beneath the fade. It is important to know how the shapes
differ, and which are most suitable for various editing tasks.

The different types of fades are:

Linear  
   A simple linear coefficient decrease, and its mathematical inverse. 
   A linear fade starts attenuating quickly, and then cuts off even more
   abruptly at lower levels. When used as a crossfade, the signals are
   each -6dB attenuated at the midpoint. This is the correct crossfade
   to use with highly-correlated signals for a smooth transition.

Constant Power  
   The constant power curve starts fading slowly and then cuts off
   abruptly. When used as a crossfade between 2 audio regions, the
   signals are symmetrically attenuated, and they each reach -3dB at the
   midpoint. This is the correct crossfade to use when splicing audio in
   the general (uncorrelated) case.

Symmetric  
   The symmetric fade starts slowly, then attenuates significantly
   before transitioning to a slower fade-out near the end of the fade.
   When used as a crossfade, the Symmetric curve is not mathematically
   correct like the Constant Power or Linear curves, but it provides a
   slower fade-out at low volumes. This is sometimes useful when editing
   2 entire music works together so that the transition is more gradual.

Slow  
   The slow curve is a modified linear decibel fade. The initial curve
   starts more gradually so that it has a less abrupt transition near
   unity. After that, it sounds like a perfectly smooth fader or knob
   moved to silence. This shape is excellent as a general-purpose
   fade-out. When used as a crossfade, the inverse fade curve maintains
   constant power but is therefore non-symmetric; so its use is limited
   to those cases where the user finds it appropriate.

Fast  
   The fast curve is a linear decibel fade; it sounds like a perfectly
   smooth fader or knob moved to silence. This shape is excellent as a
   general-purpose fade-in. When used as a crossfade, the inverse fade
   curve maintains constant power but is therefore non-symmetric; so its
   use is limited to those cases where the user finds it appropriate.

Although these fade shapes serve specific purposes, any of the shapes is
usable in any situation, so the final decision is mostly an artistic
choice.

These fade curves are developed to provide a range of common uses, and
are developed with the least possible amount of changes in the "slope"
of the line. This provides artefact-free crossfades. Some DAWs provide
complicated fade editors with parametric "spline" controls of the fade
curves. While it might be interesting to develop a fade curve with a
faster cutoff, the mathematical difference between this and simply
shortening the fade is vanishingly small; and the amount of effort to
shorten the fade is much easier than messing with a crossfade editor
dialog.
