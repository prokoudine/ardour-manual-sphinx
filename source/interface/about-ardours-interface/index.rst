Ardour's interface overview
###########################

In Ardour, work is done in one of four windows: the :guilabel:`Editor`, the :guilabel:`Mixer`, the :guilabel:`Recorder`, or the :guilabel:`Cue`.

.. raw:: html
   <figure class="imagemap" style="width:100%;">
   <img src="images/editor_map.png" alt="The Editor window" width="900" height="502">
   <!-- common -->
   <a href="@@main-menu" class="area" style="left: 0px; top: 0px; width: 168px; height: 13px;"></a>
   <a href="@@status-bar" class="area" style="left: 746px; top: 0px; width: 154px; height: 13px;"></a>
   <a href="@@transport-bar" class="area" style="left: 0px; top: 13px; width: 99px; height: 29px;"></a>
   <a href="@@selection-and-punch-clocks" class="area" style="left: 99px; top: 13px; width: 69px; height: 29px;"></a>
   <a href="@@other-toolbar-items#latency-compensation-info" class="area" style="left: 168px; top: 13px; width: 69px; height: 29px;"></a>
   <a href="@@other-toolbar-items#playhead_options" class="area" style="left: 237px; top: 13px; width: 51px; height: 29px;"></a>
   <a href="@@transport-clocks" class="area" style="left: 288px; top: 13px; width: 183px; height: 29px;"></a>
   <a href="@@other-toolbar-items#status_indicators" class="area" style="left: 471px; top: 13px; width: 28px; height: 29px;"></a>
   <a href="@@other-toolbar-items#monitor_section_info" class="area" style="left: 499px; top: 13px; width: 26px; height: 29px;"></a>
   <a href="@@mixing-linear-nonlinear-workflows" class="area" style="left: 525px; top: 13px; width: 42px; height: 29px;"></a>
   <a href="@@selection-and-punch-clocks" class="area" style="left: 567px; top: 13px; width: 65px; height: 29px;"></a>
   <a href="@@mini-timeline" class="area" style="left: 632px; top: 13px; width: 187px; height: 29px;"></a>
   <a href="@@other-toolbar-items#mode_selector" class="area" style="left: 819px; top: 13px; width: 81px; height: 29px;"></a>
   <!-- editor -->
   <a href="@@toolbox" class="area" style="left: 53px; top: 42px; width: 171px; height: 17px;"></a>
   <a href="@@grid-controls" class="area" style="left: 224px; top: 42px; width: 64px; height: 17px;"></a>
   <a href="@@nudge-controls" class="area" style="left: 288px; top: 42px; width: 73px; height: 17px;"></a>
   <a href="@@zoom-controls" class="area" style="left: 746px; top: 42px; width: 154px; height: 17px;"></a>
   <a href="@@ruler" class="area" style="left: 53px; top: 59px; width: 693px; height: 65px;"></a>
   <a href="@@editor-lists" class="area" style="left: 746px; top: 59px; width: 154px; height: 442px;"></a>
   <a href="@@summary" class="area" style="left: 53px; top: 458px; width: 693px; height: 43px;"></a>
   <a href="@@track-and-bus-groups" class="area" style="left: 53px; top: 124px; width: 10px; height: 334px;"></a>
   <a href="@@automation" class="area" style="left: 63px; top: 174px; width: 683px; height: 51px;"></a>
   <a href="@@control-masters-mixer-strips" class="area" style="left: 63px; top: 410px; width: 683px; height: 48px;"></a>
   <a href="@@audio-track-controls" class="area" style="left: 63px; top: 139px; width: 683px; height: 35px;"></a>
   <a href="@@midi-track-controls" class="area" style="left: 63px; top: 225px; width: 683px; height: 102px;"></a>
   <a href="@@bus-controls" class="area" style="left: 63px; top: 346px; width: 683px; height: 64px;"></a>
   <a href="@@bus-controls" class="area" style="left: 63px; top: 124px; width: 683px; height: 15px;"></a>
   <a href="@@audio-track-controls" class="area" style="left: 63px; top: 327px; width: 683px; height: 19px;"></a>
   <a href="@@audiomidi-mixer-strips" class="area" style="left: 0px; top: 42px; width: 53px; height: 460px;"></a>
   
   <figcaption>
      The Editor window. Clicking on a section accesses its description.
   </figcaption>
   </figure>


.. figure:: images/editor_map.png
   :alt: The Editor window. Clicking on a section accesses its
   description.
   :width: 900px
   :height: 502px

   The Editor window. Clicking on a section accesses its description.

.. figure:: images/mixer_map.png
   :alt: The Mixer window. Clicking on a section accesses its
   description.
   :width: 900px
   :height: 502px

   The Mixer window. Clicking on a section accesses its description.

.. figure:: images/recorder_map.png
   :alt: The Recorder window. Clicking on a section accesses its
   description.
   :width: 900px
   :height: 502px

   The Recorder window. Clicking on a section accesses its description.

.. figure:: images/cue_map.png
   :alt: The Cue Grid window. Clicking on a section accesses its
   description.
   :width: 900px
   :height: 502px

   The Cue Grid window. Clicking on a section accesses its description.

The Editor, Mixer, Recorder and Clip Launcher share the same toolbar (the top of the window). The sections displayed in this toolbar can be customized to the user's workflow, by checking options in :menuselection:`Preferences > Appearance > Toolbar`.

Switching between these 4 different modes is done:

-  with the `Mode Selector buttons <@@other-toolbar-items#mode_selector>`__ in the upper right
-  with the menu :menuselection:`Window > Editor` (or :menuselection:`Mixer / Recorder / Cue Grid > Show`.

Additionally, the M shortcut allows switching between the Editor and Mixer.

Multiple windows can be visible at the same time (e.g. for a multi-monitor setup) using :menuselection:`Window > Editor` (or :menuselection:`Mixer / Recorder / Cue Grid > Detach` option in the same submenu.

The Editor
**********

The Editor window includes the editor track canvas where audio and MIDI data can be arranged along a timeline. This is the window where editing and arranging a project is done. The window has a general "horizontal" sense to it: the timeline flows from left to right, the playhead showing the current position in the session moves from left to right—the window really represents time in a fairly literal way.

It is possible to show a single channel strip in the editor window, and some people find this enough to work on mixing without actually opening the mixer window. Most of the time though, both of these windows will be needed at various stages of a session's lifetime.

The Mixer
*********

The Mixer window represents signal flow and is the window that will probably be used most when mixing a session. It includes channel strips for each track and bus in the session. It has a general "vertical" sense to it: signals flow from the top of each channel strip through the processing elements in the strip to reach the output listed at the bottom.

To learn more about the process of mixing, see
`Mixing <@@basic-mixing>`__.

The Recorder
************

The Recorder window is a very specialized view that provides a compact view of all track's record and monitor status, and a simplified timeline that keeps everything in view at once. Most of the information that is shown in this mode is already available in Mixer or Editor mode, but the Recorder aims at having everything in sight and under control while tracking a performance.

The Recorder is covered in great detail in `its own page <@@recorder>`__.

The Cue Grid
************

The Cue Grid window, unlike the rest of Ardour, allows for a non-linear workflow. It is a clip launcher, that allows to chain and combine various loops and samples, and program events.

Instead of anchoring these samples or loops on a timeline, the Cue Grid gives them instruction on when they are triggered, how they are played, what happens at the end of the clip, etc…

The `Cue <@@cue>`__ section of this manual describes this worfkow.
