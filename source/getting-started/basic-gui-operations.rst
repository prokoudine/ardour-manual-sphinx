Basic GUI operations
====================

By default, Ardour will show helpful **tooltips** about the purpose and use of each GUI element if the pointer is positioned over it and hovered there for a short while. These little pop-up messages can be a good way to discover the purpose of many aspects of the GUI.

Pop-ups can also be distracting for experienced users, who may wish to disable them via :menuselection:`Edit > Preferences > GUI > Show tooltip if mouse hovers over a control`.

Selection Techniques
--------------------

Ardour follows the conventions used by most other computer software (including other DAWs) for **selecting objects** in the GUI.

Selecting individual objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clicking on an object (sometimes on a particular part of its on-screen representation) will select the object, and deselect other similar objects.

Selecting multiple (similar) objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A :kbd:`Ctrl-left`-click on an object toggles its selected status, so using :kbd:`Ctrl-left` on a series of objects will select (or deselect) each one of them. A completely arbitrary set of selections can be constructed with this technique.

Selecting a range of objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In cases where the idea of "select all objects between this one and that one" makes sense, select one object and then :kbd:`Shift-left`-click on another to select both of them as well as all objects in between.

Time range selection
~~~~~~~~~~~~~~~~~~~~

To select a time **range** in the Editor, :kbd:`Left`-click and drag the mouse. A :kbd:`Ctrl-left` drag then lets you create other ranges and a :kbd:`Shift-left`-click extends a range to cover a wider area.

Selection Undo
~~~~~~~~~~~~~~

The set of objects (including time range) that are selected at any one time is known as the selection. Each time an object is selected or deselected, the new selection is stored in an undo/redo stack. This stack is cleared each time the content of the timeline changes.

If a complex selection has been built up and then accidentally cleared it, choosing :menuselection:`Edit > Undo Selection Change` will restore the previous selection. If a selection is undone and a return to the state before the undo is desired, choosing :menuselection:`Edit > Redo Selection Change` will take the selection back to where it was before :menuselection:`Edit > Undo Selection Change` was chosen.:

Cut and Paste Operations
------------------------

The **clipboard** is a holder for various kinds of objects (regions, control events, plugins) that is used during **cut-and-paste operations**.

Cut
~~~

A **cut** operation removes selected objects and places them in the clipboard. The existing contents of the clipboard are overwritten. The default key binding is :kbd:`Ctrl-x`.

Copy
~~~~

A **copy** of the selected objects are placed in clipboard. There is no effect on the selected objects themselves. The existing contents of the clipboard are overwritten. The default key binding is :kbd:`Ctrl-c`.

Paste
~~~~~

The current contents of the clipboard are **pasted** (inserted) into the session, using the current edit point as the destination. The contents of the clipboard remain unchanged—the same item can be pasted multiple times. The default key binding is :kbd:`Ctrl-v`.

Deleting Objects
----------------

Within the Editor window (and to some extent within the Mixer window too), there are several techniques for **deleting** objects (regions, control points, and more).

Using the mouse and keyboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the object(s) to be deleted and then press the :kbd:`Del` key. This does **not** put the deleted object(s) in the clipboard, so they cannot be pasted elsewhere.

Using normal cut and paste shortcuts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the object(s) and then press :kbd:`Ctrl-x`. This puts the deleted object(s) in the clipboard so that they can be pasted elsewhere.

Using just the mouse
~~~~~~~~~~~~~~~~~~~~

By default, :kbd:`Shift Right` will delete the clicked-upon object. Like the :kbd:`Del` key, this does **not** put the deleted object(s) in the clipboard.

.. note::
   The modifier and mouse button used for this can be controlled via :menuselection:`Edit > Preferences > User Interaction > Delete using …`. Any modifier and mouse button combination can be used.

Undo/Redo for Editing
---------------------

While editing, it sometimes happens that an unintended change is made, or a choice is made that is later decided to be wrong. All changes to the arrangement of session components (regions, control points) along the timeline can be **undone** (and **redone** if necessary).

The default keybindings are :kbd:`Ctrl-Z` for Undo and :kbd:`Ctrl-R` for Redo. These match the conventions of most other applications that provide undo/redo.

Changes are also saved to the **session history** file, so that undo/redo is possible even if the session is closed and reopened later, even if Ardour is exited in between.

The maximum number of changes that can be undone can be configured under :menuselection:`Edit > Preferences > Misc > Undo`. The maximum number of changes stored in the history file is a separate parameter, and can also be set in the same place.

.. note::
   In addition to the normal undo (which works only on actions that change the timeline), there is a **visual undo** which will revert any command that affects the display of the editor window. Its shortcut is :kbd:`Ctrl-Z`. There is also an undo for selection; see "Selection Techniques" above.
