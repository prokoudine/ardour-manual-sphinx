.. _inserts:

Inserts
=======

Inserts are signal tap points that can be placed anywhere inside a
channel strip. Unlike Auxes, they will interrupt the signal flow,
feeding the signal from before the insert point to its Insert send(s),
and connecting the remainder of the channel strip to the Insert
return(s), both of which are either audio device or JACK ports.

.. note::
   When an insert is created, the signal will be interrupted until the
   relevant connections to the insert ports are made!

While jack ports are visible to other JACK applications, ALSA ports are
only useful for patching in audio equipment external to the computer. If
inserting a software processor is required, a plugin would be the first
choice. If a plugin is not available then the jackd audio backend would
have to be used. This is not very common any more but there are some
older jack clients that require using jack.

Inserts work the same as the inserts on analog consoles except they are
not normalled like most jacks on an analog console.

An insert allows to either use a special external DSP JACK application
that is not available as a plugin, or to splice an external analog piece
of gear into a channel strip, such as a vintage compressor, tube
equalizer, etc. In the latter case, the inserts would first be connected
to a pair of hardware ports, which are in turn connected to the outboard
gear. This is done on the **Send/Output** and **Return/Input** tabs of
the **Insert** dialog respectively.

.. figure:: images/port-insert-send.png
   :alt: Insert / Send
   :width: 60%

   Insert Dialog, the Send/Output tab

Apart from providing access to the connections matrix, the dialog allows
adjusting the output gain and toggling phase inversion for Send/Output,
as well as measuring and adjusting latency for the insert.

.. note::
   Inserts will incur an additional period of latency, which can be
   measured and compensated for during mixing, but not during tracking!

Disabling (bypassing) an insert is done by clicking on its LED in the
processor box.
