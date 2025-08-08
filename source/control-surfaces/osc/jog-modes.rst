.. _jog_modes:

Jog modes
=========

The ``/jog`` command will have a different affect depending on which jog
mode is selected. The jog system has two commands and gives feedback of
the mode chosen.


``/jog *delta*``
   Where *delta* is a float indicating the amount and direction.

``/jog/mode *mode*``
   Where *mode* is an int from ``0`` to ``7`` indicating the mode

Feedback is as below.

``/jog/mode/name *name*``
   Where *name* is a string indicating the name of the current jog mode.


``/jog/mode *mode*``
   Where *mode* is an int from ``0`` to ``7`` indicating the current jog mode.

Jog Modes
~~~~~~~~~

-  ``0`` Jog, each tick moves the Playhead forward or backward 0.2 seconds.
-  ``1`` Nudge, Moves the Playhead forward or backward by the amount of the
   nudge clock.
-  ``2`` Scrub, see `Scrub mode <#scrub-mode>`__.
-  ``3`` Shuttle, each tick raises or lowers the transport speed by 12.5%.
-  ``4`` Marker, Moves the Playhead to the previous or next Marker.
-  ``5`` Scroll, each tick scrolls the edit window by one, forward or back.
-  ``6`` Track, moves the current bank left or right by one strip.
-  ``7`` Bank, Moves the current bank left or right by one bank.

The jog mode may be set using a slider with ``0`` to ``7`` limits, a
group of switches or radio buttons. What works in any situation will
depend on the controller.

.. _scrub_mode:

Scrub mode
~~~~~~~~~~

Scrub deserves special mention. In an ideal world, scrub would be jog
with sound. However, Ardour does not have that functionality yet. So
scrub starts the transport rolling at either ``50%`` or ``100%``
depending on how fast the jog wheel is turned.

The position of the last tick is always saved and if no more ticks are
received, the transport is located there when stopped at time out. If
the jog wheel gives a value of ``0`` when released the transport stops
at the location the value 0 is sent.
