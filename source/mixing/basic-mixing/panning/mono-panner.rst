.. _mono_panner:

Mono panner
===========

The default **mono panner** distributes 1 input to 2 outputs. Its behaviour
is controlled by a single parameter, the position. By default, the
panner is centered.

Mono panner user interface
--------------------------

.. figure:: images/mono-panner.png
   :alt: The mono panner
   :class: right-float

The mono panner looks quite similar to the :ref:`stereo
panner <stereo_panner>` interface. The difference is that the L/R
labels in the lower half of the mono panner do not move because there is
no "width" to control.

On the adjacent picture, the panner is centered, as shown by the central
position of the slider, called position indicator.

Using the mouse
---------------

To change the position smoothly, press the right button and drag
anywhere within the panner. Note that grabbing the position indicator
is not needed to drag.

Reset to defaults
   Click :kbd:`Shift`-right

Change to a "hard left"
   Double click right in the left side of the panner

Change to a "hard right"
   Double click right in the right side of the panner

Set the position to center
   Double Click right in the middle of the panner

Keyboard bindings
-----------------

When the pointer is within a mono panner user interface, the following
keybindings are available to operate on that panner:

:kbd:`←` / :kbd:`Ctrl-←` 
   move position 1° / 5° to the left
:kbd:`→` / :kbd:`Ctrl-→`
   move position 1° / 5° to the right
:kbd:`0`
   reset position to center

Using the scroll wheel/touch scroll
-----------------------------------

When the pointer is within a mono panner user interface, the scroll
wheel may be used as follows:

:kbd:`⇑` or :kbd:`⇐` 
   move position to the left by 1°
:kbd:`Ctrl-⇑` or :kbd:`Ctrl-⇐` 
   move position to the left by 5°
:kbd:`⇓` or :kbd:`⇒` 
   move position to the right by 1°
:kbd:`Ctrl-⇓` or :kbd:`Ctrl-⇒` 
   move position to the right by 5°
