.. _navigating_the_editor:

Navigating the Editor
=====================

Navigating the Editor window is obviously a very frequent operation. Ardour sticks with a lot of the usual conventions in this regard, to allow for a quick learning. As those operations are so common, it is worth taking the time to learn most of the keyboard and mouse shortcuts in order for these to become fast and natural.

The keyboard shortcuts can, as always, be edited, so the defaults are shown here.

Scrolling
---------

Scrolling can be done on-canvas, or with the :ref:`Summary <summary>`.

On Canvas
~~~~~~~~~

======================= ============== ========
Action                  Mouse          Keyboard
======================= ============== ========
Scrolling up            :kbd:`⇑`       :kbd:`↑`
Scrolling down          :kbd:`⇓`       :kbd:`↓`
Scrolling up one page   :kbd:`⇞`
Scrolling down one page :kbd:`⇟`
Scrolling left          :kbd:`Shift-⇑`  
Scrolling right         :kbd:`Shift-⇓`  
======================= ============== ========

.. note::
   Moving the playhead outside the view may scroll the screen accordingly, so using :kbd:`←` or :kbd:`→`, while not *scrolling* per se, will result in scrolling if **Transport > Follow playhead** is checked. This is also true with the :ref:`Navigation Timeline <mini_timeline>`, and anything that moves the playhead.

In the Summary
~~~~~~~~~~~~~~

Clicking and dragging in the Summary will scroll the view left and right. If the screen view is clicked (the white rectangle) and dragged, the view can also be scrolled vertically.

Additionally, on the left and on the right of the Summary, the **<** and **>** arrows buttons allow to scroll one screen either left or right.

Zooming
-------

Zooming (on time) can be done on-canvas (which will always be centered around the mouse cursor), with the Summary, or with the :ref:`Zoom Controls <zoom_controls>`.

.. _on_canvas_1:

On Canvas
~~~~~~~~~

=========== =============
Zooming in  :kbd:`Ctrl-⇑`
Zooming out :kbd:`Ctrl-⇓`
=========== =============

.. _in_the_summary-1:

In the Summary
~~~~~~~~~~~~~~

Resizing the screen view in the **Summary** (the white rectangle) changes
the zoom accordingly.

With the zoom controls
~~~~~~~~~~~~~~~~~~~~~~

With the **Zoom Focus** set, the **−** and **+** buttons will zoom out or in around this focus. The **[ ]** button zooms to the whole session as defined by the start and end markers.

These controls are bound to the keyboard :kbd:`−` and :kbd:`=` respectively by default.

Height of the tracks
--------------------

Changing the height of the tracks results in more or less tracks on screen. This can be done on canvas, with the **Summary** or with the zoom controls.

.. _on-canvas-2:

On canvas
~~~~~~~~~

Using :kbd:`Alt-⇓` or :kbd:`Alt-⇑` while hovering over a track reduces or enhances its height, i.e. zooms on the hovered track, regardless of the selection.

The :kbd:`F` key resizes the tracks so that only the selected one(s) are displayed. If some unselected tracks are in-between those selected tracks, their :ref:`visibility <the_tracks_and_busses_list>` will be toggled off.

.. _in-the-summary-2:

In the Summary
~~~~~~~~~~~~~~

Resizing the screen view in the Summary (the white rectangle) changes
the number of tracks displayed (hence their heights) accordingly. It
behaves more like a zoom as the relative height of the tracks are kept.

.. _with-the-zoom-controls-1:

With the zoom controls
~~~~~~~~~~~~~~~~~~~~~~

The three rightmost buttons of the zoom control bar, while not zoom
buttons, act upon the height of the tracks:

-  The first selector directly selects how many tracks are currently on screen.
-  The second one reduces the height of the selected track(s). If none are selected, all the tracks are affected, while maintaining (as long as it is possible) their relative heights.
-  The third one enlarges the tracks, and is the counterpart of the previous one.
