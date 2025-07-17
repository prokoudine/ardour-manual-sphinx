Overview of all timecode related settings
=========================================

Timecode settings are accessed from the menu in three places:

-  :menuselection:`Session > Properties > Timecode`
-  :menuselection:`Edit > Preferences > Transport`
-  :menuselection:`Edit > Preferences > MIDI`

Timecode settings
-----------------

:guilabel:`Timecode frames-per-second`
   Configure timecode frames-per-second (23.976, 24, 24.975, 25, 29.97, 29.97 drop, 30, 30 drop, 59.94, 60). Note that all fractional framerates are actually fps*(1000.0/1001.0).

:guilabel:`Pull up/down`
   Video pull-up modes change the effective samplerate of Ardour to allow for changing a film soundtrack from one frame rate to another. See `Telecine <http://en.wikipedia.org/wiki/Telecine>`__

:guilabel:`Slave Timecode offset`
   The specified offset is added to the received timecode (MTC or LTC).

:guilabel:`Timecode Generator offset`
   Specify an offset which is added to the generated timecode (so far only LTC).

:guilabel:`JACK Time Master`
   Provide Bar|Beat|Tick and other information to JACK.

These settings are session specific.

Transport preferences
---------------------

:guilabel:`External timecode source`
   Select timecode source: JACK, LTC, MTC, MIDI Clock

:guilabel:`Match session video frame rate to external timecode`
   This option controls the value of the video frame rate while chasing an external timecode source. When enabled, the session video frame rate will be changed to match that of the selected external timecode source. When disabled, the session video frame rate will not be changed to match that of the selected external timecode source. Instead the frame rate indication in the main clock will flash red and Ardour will convert between the external timecode standard and the session standard.

:guilabel:`External timecode is sync locked`
   Indicates that the selected external timecode source shares sync (Black & Burst, Wordclock, etc) with the audio interface.

:guilabel:`Lock to 29.9700 fps instead of 30000/1001`
   The external timecode source is assumed to use 29.97 fps instead of 30000/1001. SMPTE 12M-1999 specifies 29.97df as 30000/1001. The spec further mentions that drop-frame timecode has an accumulated error of -86ms over a 24-hour period. Drop-frame timecode would compensate exactly for a NTSC color frame rate of 30 * 0.9990 (ie 29.970000). That is not the actual rate. However, some vendors use that rate—despite it being against the specs—because the variant of using exactly 29.97 fps has zero timecode drift.

:guilabel:`LTC incoming port`
   Offers a session agnostic way to retain the LTC port connection.

:guilabel:`Enable LTC generator`
   Does just what it says.

:guilabel:`Send LTC while stopped`
   Enable to continue to send LTC information even when the transport (playhead) is not moving. This mode is intended to drive analog tape machines which unspool the tape if no LTC timecode is received.

:guilabel:`LTC generator level`
   Specify the Peak Volume of the generated LTC signal in dbFS. A good value is 0 dBu (which is -18 dbFS in an EBU calibrated system).

These settings are common to all sessions.

MIDI preferences
----------------

:guilabel:`Send MIDI Timecode`
   Enable MTC generator

:guilabel:`Send MIDI Clock`
   Enable MIDI Clock generator

These settings are also common to all sessions.
