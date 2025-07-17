About Ardour's documentation
============================

This section covers some of the typographical and language conventions used in this manual.

Keyboards and Modifiers
***********************

Keyboard bindings are shown like this: s or x.

x means "press the key, keep it pressed and then also press the x key".

Combinations such as e may be seen, which means "hold down the key *and* the key, and then, while keeping them both down, press the e key".

Different platforms have different conventions for which modifier key (Control or Command) to use as the primary or most common modifier. When viewing this manual from a machine identifying itself as running OS X, Cmd will be seen where appropriate (for instance in the first example above). On other machines Ctrl will be seen instead.

Mouse Buttons
*************

`Mouse buttons <@@mouse>`__ are referred to as Left, Middle and Right. Ardour can use additional buttons, but they have no default behaviour in the program.

Mouse Click Modifiers
~~~~~~~~~~~~~~~~~~~~~

Many editing functions are performed by clicking the mouse while holding a modifier key, for example Left.

Mouse Wheel
~~~~~~~~~~~

Some GUI elements can optionally be controlled with the mouse wheel when the pointer is hovering over them. The notation for mouse wheel action is ⇑ ⇐ ⇓ ⇒.

Context-click
~~~~~~~~~~~~~

The term context-click is used to indicate a Right-click on a particular element of the graphical user interface. Although right-click is the common, default way to do this, there are other ways to accomplish the same thing—this term refers to any of them, and the result is always that a menu specific to the item clicked on will be displayed.

"The Pointer"
~~~~~~~~~~~~~

When the manual refers to the "pointer", it means the on-screen representation of the mouse position or the location of a touch action if touch interface is being used.

Other User Input
****************

Ardour supports hardware controllers, such as banks of faders, knobs, or buttons.

Menu Items
**********

Menu items are indicated like this: :menuselection:`Top > Next > Deeper`. Each :menuselection:`>`-separated item indicates one level of a nested menu or sub-menu.

OSC Messages
************

OSC messages, whether sent or received, are displayed like this:
/transport_stop.

.. _dialog-options:

Preference/Dialog Options
*************************

Choices in various dialogs, notably the :guilabel:`Preferences` and :guilabel:`Properties` dialog, are indicated thus:

:menuselection:`Edit > Preferences > Audio > Some Option`.

Each successive item indicates either a menu, sub-menu, or a tabbed dialog navigation. The final item is the one to choose or select.

If an option is deselected, it will look like this:

:menuselection:`Edit > Preferences > Audio > Some other Option`.

.. _user=input:

User Input
**********

Some dialogs or features may require the user to input data such as this. In rare cases, certain operations will be required to be performed at the command line of the operating system:

``cat /proc/cpuinfo sleep 3600 ping www.google.com``

Program Output
**************

Important messages from Ardour or other programs will be displayed ``like this``.

Notes
*****

Important notes about things that might not otherwise be obvious are shown in this format.

Warnings
********

Hairy issues that might cause things to go wrong, lose data, impair sound quality, or eat your proverbial goldfish, are displayed in this way.
