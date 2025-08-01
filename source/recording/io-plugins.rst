.. _io_plugins:

I/O plugins
===========

I/O plugins are a way to process audio outside the normal Ardour session or connect to sources typically unavailable in a DAW, such as outputs of NDI devices. Pre-plugins run before Ardour does any processing, post-plugins run after Ardour has done all processing.

A common use case is wet recording where a number of plugins are applied directly to the physical input. The processed signal then can be routed to any number of tracks or busses in Ardour. This is a lot like doing some of the processing with a chain of guitar pedals, then feeding the signal to an Aux In port on a mixing console or an input port on a multi-effects digital pedalboard.

The rationale for pre-processing with I/O plugins is that it's a more lightweight way to do it as compared to busses. Much of that is because busses have automatable parameters such as fader and panner positions, as well as plugins' parameters. Evaluating parameter automation (even when there's none) adds additional load to the CPU. However I/O plugins are not automatable, so there's no evaluation happening. As far as Ardour is concerned, they are almost like JACK audio server clients running alongside Ardour.

Another use case would be loading an instance of the NDI Input plugin as a pre-processing plugin to be able to capture and mix sources from NDI devices, or loading an instance of the NDI Output plugin to send audio from Ardour over IP to a receiver for broadcasting.

.. figure:: images/io-plugins-ndi-input.png
   :alt: NDI Input plugin loaded as a pre-processing I/O plugin
   :figclass: hdimage

   NDI Input plugin loaded as a pre-processing I/O plugin

It's also possible to use the post-processing section to load plugins for room correction or signal analysis (VU meters, spectrum analyzers etc.).

Adding I/O plugins
------------------

New I/O plugins can be added in the **I/O Plugins** dialog (**Window > I/O Plugins**).

.. figure:: images/io-plugins-empty-slots.png
   :alt: Empty slots in the I/O Plugins dialog
   :figclass: hdimage

   Empty slots in the I/O Plugins dialog

Right-clicking opens the same menu for plugin selection available for mixer channel strips:

.. figure:: images/io-plugins-right-click-menu.png
   :alt: Right-click menu in the I/O Plugins dialog
   :figclass: hdimage

   Right-click menu in the I/O Plugins dialog

Double-clicking opens the **Plugin Selector** dialog.

Once a plugin has been selected and added, it shows in either Pre- or Post-process section depending on your choice.

.. figure:: images/io-plugins-one-plugin-added.png
   :alt: ACE Compressor added to the pre- section
   :figclass: hdimage

   ACE Compressor added to the Pre-process section

Routing I/O plugins
-------------------

I/O plugins have the same user interface for setting input and outputs that is also available in mixer channel strips. The button above the plugin name opens a drop-down menu for quickly choosing an input port. The button below opens the drop-down menu for choosing the output port.

.. figure:: images/io-plugins-choose-output.png
   :alt: Choosing output for an I/O plugin
   :figclass: hdimage

   Choosing output for an I/O plugin

Additionally, new tracks automatically connected to an I/O plugin can be easily created in the Recorder window by clicking the **+** button and then setting a new for that track.

.. figure:: images/io-plugins-new-track-from-io-plugin.png
   :alt: New track connected to an I/O plugin
   :figclass: hdimage

   New track connected to an I/O plugin

On the **Audio Connections** dialog, the ports of pre- and post-process plugins are listed on dedicated tabs (**I/O Pre** and **I/O Post**), separately from all other ports.

.. figure:: images/io-plugins-in-audio-connections.png
   :alt: I/O Plugins in the Audio Connections dialog
   :figclass: hdimage

   I/O Plugins in the Audio Connections dialog
