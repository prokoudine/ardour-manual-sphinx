Connecting audio and MIDI devices
=================================

Normally Ardour does not care about how audio and MIDI gets into the computer—it pretty much deals only with its own inputs and outputs; it is up to the user to ensure that all external routing is sound. After all, Ardour has no way to know how signals from the outside world get to it. However, there are some things that Ardour can do to help troubleshoot problems with audio and MIDI connections—at least on the computer side.

For example, a typical setup might include a microphone that feeds a mixer that then feeds the computer. A failure can occur anywhere in that signal chain, including the cables that connect everything together. As far as Ardour is concerned, the most important connection is the one coming from the sound source to the physical audio input of the computer—in this example, the cable connecting between the mixer and the computer.

Common sense and basic troubleshooting skills are needed when problems arise, and in the above example, one would have to go through the entire signal chain to ensure that each component was working as it should.

For some cases, Ardour eliminates possible I/O issues. One such case is automatically saving I/O per device to sessions and restoring connections when switching the backend, e.g. from ALSA to PulseAudio and vice versa.

Common Problems
---------------

Ardour tries to set things up in a sane manner by automatically connecting the hardware inputs of the computer to its master input and the hardware outputs to the master output. If the signal coming into the hardware inputs is active, the meters on Ardour's master channel should move. If they don't, some things to check include:

-  Making sure there is actually an input signal
-  Making sure the input signal is getting into the computer
-  Making sure that Ardour is talking to the correct sound card
-  Making sure that the sound card in use by Ardour is working properly
