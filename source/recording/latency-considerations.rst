.. _latency_considerations:

Latency considerations
======================

In the days of analog tape recording, the routing of monitor signals was performed with relays and other analog audio switching devices. Digital recorders have the same feature, but may impart some :ref:`latency <latency_and_latency_compensation>` (delay) between the time a noise is made and the time that it will come back from the recorder.

The latency of *any* conversion from analog to digital and back to analog is about 1.5–2 ms. Some musicians claim that even the basic A/D/A conversion time is objectionable. However even acoustic instruments such as the piano can have approximately 3 ms of latency, due to the time the sound takes to travel from the instrument to the musician's ears. Latency below 5 ms should be suitable for a professional recording setup. Because 2 ms are already used in the A/D/A process, extremely low buffer sizes must be used in the workstation I/O setup to keep the overall latency below 5ms. Not all :ref:`computer audio systems <the_right_computer_system_for_digital_audio>` are able to work reliably at such low buffer sizes.

For this reason it is sometimes best to route the monitor signal through an external mixing console while recording, an approach taken by most if not all professional recording studios. Many computer I/O devices have a hardware mixer built in which can route the monitor signal "around" the computer, avoiding the system latency.

In either case, the monitoring hardware may be digital or analog. And in the digital case there will still be the A-D-A conversion latency of 1–2 ms.
