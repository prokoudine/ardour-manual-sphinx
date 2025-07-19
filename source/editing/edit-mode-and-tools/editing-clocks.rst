.. _editing_clocks:

Editing clocks
==============

Clock Modes
-----------

Every clock in Ardour has multiple different, selectable **clock
modes**. Each mode displays time using different units. The clock mode
can be changed by right-clicking on the clock and selecting the desired
mode from the menu. Some clocks are entirely independent of any other
clock's mode; others are linked so that changing one changes all clocks
in that group. The different modes are:

Timecode
   Time is shown as **SMPTE timecode** in Hours:Minutes:Seconds:Frames, measured from the timecode zero point on the timeline (which may not correspond to the session start and/or absolute zero on the timeline, depending on configurable timecode offsets). The frames value is dictated by either the Timecode frames-per-second :ref:`session property <session_properties_timecode>`, or, if slaved to an external timecode master, the master's setting. Under the transport clocks is an indication of the current timecode source (``INT`` means that Ardour is its own timecode source).

Bars:Beats
   Time is shown as Bars:Beats:Ticks, indicating **musical time**.

Minutes:Seconds
   Time is shown as Hours:Minutes:Seconds.Milliseconds.

Seconds
   Time is shown as Seconds.Deciseconds.

Samples
   Time is shown as a **sample count**. The number of samples per second is given by the current sample rate.

Changing clock values with the keyboard
---------------------------------------

New values for the clock can be typed in after clicking on the relevant
clock. Clicking on the clock will show a thin vertical cursor bar just
to the right of the next character to be overwritten. Time should be
typed in the same order as the current clock mode—if the clock is in
Timecode mode, it should be hours, minutes, seconds, frames. So, to
change to a time of ``12:15:20:15`` one would type :kbd:`12152015`.
Freshly typed numbers will appear in a different color, from right to
left, overwriting the existing value. Mid-edit, after typing :kbd:`3222`
the clock might look like this:

.. figure:: images/clockedit.png
   :alt: A clock being edited in Ardour

   A clock being edited in Ardour

Finishing the edit is done by pressing :kbd:`Enter` or :kbd:`Tab`. The
:kbd:`Esc` key allows to exit an edit without changing the clock. If an
entry is mis-typed so that the new value would be illegal (for example,
resulting in more than 30 frames when timecode is set to 30 frames per
second), the clock will reset at the end of the edit, and move the
cursor back to the start to allow for another try.

Avoiding the mouse entirely
---------------------------

There is a shortcut available to edit the transport clocks entirely
without the mouse. It can be found in the :ref:`Keyboard Shortcuts
<keyboard_shortcuts>` window, **Global > Transport > Focus On Clock**.
If bound to a key (:kbd:`/` by default), then pressing that key is
equivalent to clicking on the primary (left) transport clock, and
editing can begin immediately.

Entering Partial Times
----------------------

One detail of the editing design that is not immediately obvious is that
it is possible to enter part of a full time value.

As an example, supposing that the clock is in **Bars:Beats** mode,
displaying ``024|03|0029``, altering the value to the first beat of the
current bar can be done by clicking on the clock and typing
:kbd:`010000`. Similarly, if it is in Minutes:Seconds mode, displaying
``02:03:04.456``, getting to exactly 2 hours can be achieved by clicking
on the clock and typing :kbd:`0000000` to reset the minutes, seconds and
milliseconds fields.

Entering Delta Times
--------------------

Values can also be typed into the clock that are intended as a relative
change, rather than a new absolute value, by *ending* the edit by
pressing **+** or **-** (the ones on any keypad will also work). The
plus key will add the entered value to the current value of the clock,
minus will subtract it. For example, if the clock is in **Samples** mode
and displays ``2917839``, moving it back 2000 samples is done by typing
:kbd:`2000` and :kbd:`-`, rather than ending with **Enter** or **Tab**.

Changing clock values with the mouse
------------------------------------

Using a scroll wheel
~~~~~~~~~~~~~~~~~~~~

With the mouse pointer over the clock, moving the scroll wheel changes
the clock values. Moving the scroll wheel up (:kbd:`⇑`) increases the
value shown on the clock, moving it down (:kbd:`⇓`) decreases it. The
step size is equal to the unit of the field hovered over (seconds,
hours, etc.).

Dragging the mouse
~~~~~~~~~~~~~~~~~~

With the mouse pointer over the clock, pressing the left mouse button
and dragging also affects the clocks: dragging upwards increases the
value shown on the clock, dragging downwards decreases it, again with a
step size equal to the unit of the field where the drag began on.
