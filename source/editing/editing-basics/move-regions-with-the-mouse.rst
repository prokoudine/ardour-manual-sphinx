.. _move_regions_with_the_mouse:

Move regions with the mouse
===========================

Moving or copying a region is done using the :ref:`Grab mouse mode
<toolbox>`, or the Smart mode with the pointer in the lower half of the
region to begin a move or :ref:`copy <copy_regions>` operation.

With the pointer in the region, using a left-drag will make the region
follow the pointer as it is moved around. By default, the region can
move freely along the timeline.

To move a region from one track to another, the move must be started as
described above, but the pointer should end in the desired track. The
region will follow the pointer.

.. note::
   If some other kinds of tracks are visible, the region will remain where
   it is as the pointer moves across them, and will then jump to the new
   track. This serves as a visual reminder that an audio region cannot be
   dragged into an automation track or a bus, for example.

Move Multiple Regions
---------------------

In order to move multiple regions, they should be selected before
moving. Then left-dragging one of the selected regions will move all the
regions, keeping their positions relative to each other.

Fixed-Time Motion
-----------------

Moving region(s) to other track(s) while keeping them at the same exact
position on the timeline is done by simply using a middle-drag instead.

On macOS, where the middle click might not be available, the same effect
can be achieved by switching to the :ref:`Lock mode <toolbox>` (as
opposed to **Slide** or **Ripple**) in the top-left area of the screen.
