Using the mouse
===============

Clicking
--------

Throughout this manual, the term click refers to the act of pressing and releasing the Left mouse button. This action is used to select objects, activate buttons, turn choices on and off, pop up menus and so forth. On touch surfaces, it also corresponds to a single, one-finger tap on the GUI.

Right-Clicking
--------------

The term right-click refers to the act of pressing and releasing the Right mouse button. This action is used to pop up context menus (hence the term "context click", which will also be seen). It is also used by default in combination with the shift key to delete objects within the editor window.

Some mice designed for use with Mac OS X may have only one button. By convention, pressing and holding the Control key while clicking is interpreted as a right-click by many applications.

Middle-Clicking
---------------

A middle-click refers to the act of pressing and releasing the Middle mouse button. Not all mice have a middle click button (see the `Mouse <@@mouse>`__ chapter for details). Sometimes the scroll wheel acts as a clickable middle button. This action is used for time-constrained region copying and mapping MIDI bindings.

Internally, your operating system may identify the mouse buttons as Button1, Button2, and Button3, respectively. It may be possible to invert the order of buttons to accommodate left-handed users, or to re-assign them arbitrarily. This manual assumes the canonical order.

Double-Clicking
---------------

A double click refers to two rapid press/release cycles on the leftmost mouse button. The time interval between the two actions that determines whether this is seen as two clicks or one double click is controlled by your system preferences, not by Ardour.

Dragging
--------

A drag primarily refers to the act of pressing the leftmost mouse button, moving the mouse with the button held down, and then releasing the button. On touch surfaces, this term also corresponds to a single one-finger touch-move-release action.

Ardour also uses the middle mouse button for certain kinds of drags, which will be referred to as a middle-drag.

Modifiers
---------

There are many actions in Ardour that can be carried out using a mouse button in combination with a modifier key. When the manual refers to Left, it means that you should first press the key, carry out a left click while is held down, and then finally release the key.

Available modifiers depend on your platform:

Linux Modifiers
~~~~~~~~~~~~~~~

-  :kbd:`Ctrl` (Control)
-  :kbd:`Shift`
-  :kbd:`Alt`
-  :kbd:`Win` (Super/Windows)

.. _mac-modifiers:

macOS Modifiers
~~~~~~~~~~~~~~~

-  :kbd:`Cmd` (Command, "windmill")
-  :kbd:`Ctrl` (Control)
-  :kbd:`Alt` (Option)
-  :kbd:`Shift`

Scroll Wheel
------------

Ardour can make good use of a scroll wheel on the mouse (assuming it has one), which can be utilized for a variety of purposes. Scroll wheels generate vertical scroll events, :kbd:`⇑` ScrollUp) and :kbd:`⇓` (ScrollDown). Some also emit horizontal events, :kbd:`⇐` (ScrollLeft) and :kbd:`⇒` (ScrollRight).

When appropriate, Ardour will differentiate between these two different scroll axes. Otherwise it will interpret ScrollDown and ScrollLeft as equivalent and similarly interpret ScrollUp and ScrollRight as equivalent.

Typically, scroll wheel input is used to adjust continuous controls such as faders and knobs, or to scroll vertically or horizontally inside a window. In most continuous control cases, holding down the :kbd:`Ctrl` key while scrolling will use "fine" mode and the scroll wheel increments will then be 10% of normal.
