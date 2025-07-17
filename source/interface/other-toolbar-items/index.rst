Other toolbar items
===================

.. _latency-compensation-info:

The latency compensation info
-----------------------------

This section shows information about the latency compensation Ardour sets to align all signals in time whatever their route (and processing applied).

.. figure:: images/latency-compensation-info.png
   :alt: The latency compensation info

   Latency compensation info

The only button **Disable PDC** allows to enable/disable the plugin delay compensation (PDC). Enabling it will make all signal perfectly aligned, while disabling it will reduce the delay, at the expense of slightly misaligned signals for tracks that have plugins introducing latency.

The two infos are:

-  the maxium reported latency by a plugin chain (worst route latency)
-  the I/O latency, i.e. how long does it take for a signal arriving at any physical input to be played back again.

.. _playhead_options:

The playhead options
--------------------

The two buttons in this section control the behaviour of the playhead.

.. figure:: images/playhead-options.png
   :alt: The playhead options

   The playhead options

-  **Follow Range** is a toggle that can be used to control whether or not making a range selection will move the playhead to the start of the range.
-  **Auto Return** is a toggle switch too. When active, pressing the **Stop** button returns the playhead to its previous position, and when inactive, pressing Stop keeps the playhead at its current location. Activating **Auto Return` can be useful for hearing the same piece of audio before and after tweaking it, without having to set a loop range on it.

.. _status_indicators:

The status indicators
---------------------

The status buttons show the current session state.

.. figure:: images/status_buttons.png
   :alt: The status buttons

   The status buttons

Solo
   Blinks when one or more tracks are being soloed, see :ref:`Muting and Soloing <muting_and_soloing>`. Clicking this button disables any active explicit and implicit solo on all tracks and busses.
Audition
   Blinks when some audio is auditioned, e.g. by using the import dialog, or using the Audition context menu in the :ref:`Regions List <the_region_list>`. Clicking this button stops the auditioning.
Feedback
   Blinks when Ardour detects a feedback loop, which happens when the output of an audio signal chain is plugged back to its input. This is probably not wanted and can be dangerous for the hardware and the listener.

.. _monitor_section_info:

Monitor section info
--------------------

This section is only useful and active if the session has a :ref:`Monitor section <monitor-section>`.

.. figure:: images/monitor-section-info.png
   :alt: Monitor section info

   Monitor section info

The three buttons are exactly linked to their counterparts in the Monitor slice of the mixer, but as they sit in the toolbar, remain visible even in Editor mode.

The three buttons are:

-  **Mono**: sums all of the paths to a single mono signal and applies it to all Monitor Section outputs.
-  **Dim All**: Reduces overall monitor level by the amount set with the Dim level control.
-  **Mute All**: Mutes all monitoring.

.. _tb_master_level_meter:

The master level meter
----------------------

The global meter shows the levels of the master's output. 

.. figure:: images/master-level-meter.png
   :alt: The master level meter

   The master level meter

Its the same meter that sits in the :ref:`Master's Mixer strip <master_bus_strip>`, and also shows a peak indicator, that turns red when any level exceeds 0dB. It can be reset by a left click.

.. _tb_script_buttons:

Script/Shortcut buttons
-----------------------

The buttons in between the mode selector and the master level meter are script or shortcuts buttons, which are user-definable buttons to attach any session :ref:`lua-script <lua_scripting>` to, or any action shortcut (e.g. for tasks that are used often and buried deep inside nested menus).

.. figure:: images/script-buttons.png
   :alt: The script buttons

   The script/shortcuts buttons

The number of buttons (precisely, the number of columns of two buttons) can be set in the :ref:`Preferences <preferences_appearance_toolbar>`.

Left-clicking an affected button launches the script or shortcut, while right-clicking or clicking an unaffected button allows change the script/shortcut the button should execute.

.. _other_toolbar_items_mode_selector:

The mode selector
-----------------

The mode selector allows switching between the Editor, Mixer, or Recording windows.

.. figure:: images/mode_selector.png
   :alt: The mode selector

   The mode selector

If a window is detached, the corresponding button is lit. Clicking the button switches the detached window visibility.
