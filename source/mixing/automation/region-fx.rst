.. _region_fx:

Region FX
=========

With Ardour, it's possible to apply effects to separate regions rather
than entire tracks. The effect and its automation remain with the
region, even when it is moved around on the timeline.

Applying effects directly to regions on the timeline is convenient for
many workflows. The given effect is rendered into memory and does not
add any additional DSP load during playback.

.. figure:: images/region-fx.png
   :alt: Region FX
   :width: 50%

The controls for region FX are available in the bottom pane when it's
enabled and the region properties dialog (Region > Properties in the
menu).

Adding a region effect
----------------------

To add a new region effect, right-click in the processor box of the
Region Properties dialog or bottom pane, then select an effect from the
list or use Plugin Selector.

.. figure:: images/region-fx-add.png
   :alt: Adding region effects
   :width: 75.0%

The selected effect will be added to the processor box:

.. figure:: images/region-fx-added-fx.png
   :alt: Added region effect
   :width: 50.0%

Editing a region effect
-----------------------

To edit the effect parameters, double-click its name in the processor
box.

Reordering region effects
-------------------------

To reorder region effects, pick and effect in the processor box, then
drag and drop it to the desired position.

Removing a region effect
------------------------

To remove a region effect, right-click on its name in the processor box
and select Delete in the menu.

Selecting region line
---------------------

Ardour defaults to displaying the gain automation line in the Internal
Edit mode. To choose an effect parameter instead, click on the Region
Line drop-down list in the Region Properties dialog, select an effect,
then a parameter.

.. figure:: images/region-fx-region-line.png
   :alt: Region line
   :width: 50.0%
