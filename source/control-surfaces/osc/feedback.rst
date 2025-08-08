.. _osc_feedback:

Feedback
========

Feedback from the Ardour to the the control surface is very useful for a
number of things. Motor faders need to know where the the track they
have been attached to is at before they were assigned otherwise the DAW
fader will jump to where the controller fader is. Likewise, the buttons
on each strip need to know what their value is so they can light their
LED correctly. Transport controls should let you know if they are active
too. This is what feedback is all about.

Ardour does feedback by sending the same path back that is used to
control the same function. As such any controls that have feedback have
a parameter that is the value of the control or its state (on or off).

In the case of OSC paths listed on the main OSC page as having no
parameter, if they have feedback, they will also work with a 1 for
button press and 0 for button release. This is because many OSC
controllers will only use exactly the same path for feedback as for
control. For example, ``/transport_stop`` can be used also in the form
of ``/transport_stop *press*``, where ``press`` is an int/bool
indicating if the button is pressed or not.

The feedback does not have the same meaning as the control message.
Where the button release sent to Ardour will be ignored and has no
meaning. Both states have meaning in feedback to the controller. The
feedback will be ``/transport_stop *state*``, where ``state`` is an
int/bool indicating if the transport is stopped or not.

With feedback turned on, OSC control commands that try to change a
control that does not exist will get feedback that resets that control
to off. For example, sending a ``/strip/recenable`` to a bus will not
work and Ardour will try to turn the controller LED off in that case.
Also note that Pan operation may be limited by pan width in some cases.
That is with pan width at ``100%`` (or ``-100%``) there is no pan
position movement available.

It may come as a surprise, but feedback often generates more network
traffic than control itself does. Some things are more obvious like head
position or meters. But even a simple button push like transport start
sends not only a signal to turn on the play LED, but also one to turn
off the stop LED, the Rewind LED, the Fast Forward LED and the Loop LED.
That is still minor, think instead of a surface refresh such as happens
when the surface is first connected and then most of that happens every
time the fader strips are banked. This is why feedback is enabled in
sections so that as little feedback as is actually needed is sent. This
is also a consideration if the surface is connected via wifi.

List of OSC feedback messages
-----------------------------

Feedback only
~~~~~~~~~~~~~

These messages are feedback only. They are sent as status from Ardour
and some of them may be enabled separately from other feedback. See:
:ref:`Calculating Feedback and Strip-types
Value <osc_feedback_and_strip_types_values_feedback>`.

.. note::

   See strip section below for info about ssid and wrapping it into the
   path. Also ``/master`` and ``/monitor`` support what the ``/strip``
   does.

In the case where the gain mode is set to position, the track name will show
the dB value while values are changing.

``/strip/name *ssid* *track_name*``
   where *track_name* is a string representing the name of the track

``/strip/*/automation_name *ssid* *name*``
   where *name* is a string representing the current automation mode for
   the control. See :ref:`OSC Automation <osc_automation>`.

``/session_name *session_name*``
   where *session_name* is a string representing the name of the session

``/strip/meter *ssid* *meter*``
   where *meter* is a value representing the current audio level. The
   exact math used is determined by the feedback bits set.

``/strip/signal *ssid* *signal*``
   where *signal* is a float indicating the instantaneous audio level is -40dB or higher

``/position/smpte *time*``
   where *time* is a string with the current play head time. Seconds as per SMPTE.

``/position/bbt *beat*``
   where *beat* is a string with the current play head bar/beat

``/position/time *time*``
   where *time* is a string with the current play head time. Seconds are in milliseconds

``/position/samples *samples*``
   where *samples* is a string with the current play head position in samples

``/heartbeat *LED*``
   where *LED* is a float that cycles 1/0 at 1 second intervals

``/record_tally *state*``
   Some record enable is true or "ready to record". For a "Recording" sign at studio door.

Transport Control
~~~~~~~~~~~~~~~~~

``/transport_stop *state*``
   *state* is true when transport is stopped

``/transport_play *state*``
   *state* is true when transport speed is 1.0

``/ffwd *state*``
   *state* is true when transport is moving forward but not at speed 1.0

``/rewind *state*``
   *state* is true when transport speed is less than 0.0

``/marker *position*``
   *position* is a string in the form previous <-> next or current

``/loop_toggle *state*``
   *state* is true when loop mode is true

``/cancel_all_solos *state*``
   Where *state* true indicates there are active solos that can be canceled.

``/jog/mode/name *name*``
   Where *name* is a string indicating the name of the current jog mode.

Recording control
~~~~~~~~~~~~~~~~~

``/rec_enable_toggle *state*``
   Master record enabled

Master and monitor strips
~~~~~~~~~~~~~~~~~~~~~~~~~

Master and monitor strips are similar to track strips but do not use the
SSID. Rather they use their name as part of the path:

``/master/gain *dB*``
   where *dB* is a float ranging from ``-193`` to ``+6`` representing
   the actual gain of master in dB

``/master/fader *position*``
   where *position* is an int ranging from ``0`` to ``1023``
   representing the fader control position

``/master/trimdB *dB*``
   where *dB* is a float ranging from ``-20`` to ``+20`` representing
   the actual trim for master in dB

``/master/pan_stereo_position *position*``
   where *position* is a float ranging from ``0`` to ``1`` representing
   the actual pan position for master

``/master/mute *state*``
   where *state* is a bool/int representing the actual mute state of the
   Master strip

``/monitor/gain *dB*``
   where *dB* is a float ranging from ``-193`` to ``6`` representing the
   actual gain of monitor in dB

``/monitor/fader *position*``
   where *position* is an int ranging from ``0`` to ``1023``
   representing the fader control position

``/monitor/mute *state*``
   where *state* is a bool/int representing the actual mute state of the
   Monitor strip

``/monitor/dim *state*``
   where *state* is a bool/int representing the actual dim state of the
   Monitor strip

``/monitor/mono *state*``
   where *state* is a bool/int representing the actual mono state of the
   Monitor strip

Track specific operations
~~~~~~~~~~~~~~~~~~~~~~~~~

For each of the following, *ssid* is the surface strip ID for the track.

.. note::

   Some surfaces (many Android applets) are not able to deal with more
   than one parameter in a command. However, the two parameter commands
   below can also be sent as ``/strip/command/ssid`` param. Feedback can
   be set to match this with the ``/set_surface/feedback *state*``
   command. See :ref:`Calculating Feedback and Strip-types Values 
   <osc_feedback_and_strip_types_values#feedback>`.

``/bank_up *LED*``
   where *LED* is a bool that indicates another bank_up operation is
   possible.

``/bank_down *LED*``
   where *LED* is a bool that indicates another bank_down operation is
   possible.

``/strip/name *ssid* *strip_name*``
   where *strip_name* is a string representing the name of the strip

``/strip/group *ssid* *group_name*``
   where *group_name* is a string representing the name of the group the
   track belongs to

``/strip/mute *ssid* *mute_st*``
   where *mute_st* is a bool/int representing the actual mute state of
   the track

``/strip/solo *ssid* *solo_st*``
   where *solo_st* is a bool/int representing the actual solo state of
   the track

``/strip/monitor_input *ssid* *monitor_st*``
   where *monitor_st* is a bool/int. True/1 meaning the track is forced
   to monitor input

``/strip/monitor_disk *ssid* *monitor_st*``
   where *monitor_st* is a bool/int. True/1 meaning the track is forced
   to monitor disk,  
   where both disk and input are false/0, auto monitoring is used.

``/strip/recenable *ssid* *rec_st*``
   where *rec_st* is a bool/int representing the actual rec state of the
   track

``/strip/record_safe *ssid* *rec_st*``
   where *rec_st* is a bool/int representing the actual record safe
   state of the track

``/strip/gain *ssid* *gain*``
   where *gain* is a float ranging from -193 to 6 representing the
   actual gain of the track in dB.

``/strip/fader *ssid* *position*``
   where *position* is an float ranging from 0 to 1 representing the
   actual fader position of the track.

``/strip/*/automation *ssid* *mode*``
   where *mode* is an int ranging from 0 to 3 representing the actual
   automation mode for the control. See `:ref:OSC Automation.
   <osc_automation>`.

``/strip/trimdB *ssid* *trim_db*``
   where *trim_db* is a float ranging from -20 to 20 representing the
   actual trim of the track in dB.

``/strip/pan_stereo_position *ssid* *position*``
   where *position* is a float ranging from 0 to 1 representing the
   actual pan position of the track

Selected operations
~~~~~~~~~~~~~~~~~~~

Selection feedback is the same as for strips, only the path changes from
*/strip* to */select* and there is no *ssid*. there are some extra
feedback and commands that will be listed here.

``/select/n_inputs *number*``
   where *number* number of inputs for this strip

``/select/n_outputs *number*``
   where *number* number of outputs for this strip

``/select/comment *text*``
   where *text* is the strip comment

``/select/solo_iso *state*``
   where *state* is a bool/int representing the Actual solo isolate
   state of the track

``/select/solo_safe *state*``
   where *state* is a bool/int representing the actual solo safe/lock
   state of the track

``/select/polarity *invert*``
   where *invert* is a bool/int representing the actual polarity of the
   track

``/select/pan_stereo_width *width*``
   where *width* is a float ranging from 0 to 1 representing the actual
   pan width of the track

``/select/send_gain *sendid* *send_gain*``
   where *sendid* = nth_send, *send_gain* is a float ranging from -193
   to +6 representing the actual gain in dB for the send

``/select/send_fader *sendid* *send_gain*``
   where *sendid* = nth_send, *send_gain* is a float ranging from 0 to 1
   representing the actual position for the send as a fader

``/select/send_name *sendid* *send_name*``
   where *send_name* is a string representing the name of the buss this
   send goes to.

``/select/group/enable *state*``
   where *state* is an int representing the current enable state of the
   group the selected strip is a part of

``/select/group/gain *state*``
   where *state* is an int which shows the gain sharing of the group the
   strip belongs to. See :ref:`Track and Bus Groups
   <track_and_bus_groups>` for more details

``/select/group/relative *state*``
   where *state* is an int which shows relative state of the group the
   strip belongs to. See :ref:`Track and Bus Groups
   <track_and_bus_groups>` for more details

``/select/group/mute *state*``
   where *state* is an int which shows the mute sharing of the group the
   strip belongs to. See :ref:`Track and Bus Groups
   <track_and_bus_groups>` for more details

``/select/group/solo *state*``
   where *state* is an int which shows the solo sharing of the group the
   strip belongs to. See :ref:`Track and Bus Groups
   <track_and_bus_groups>` for more details

``/select/group/recenable *state*``
   where *state* is an int which shows the recenable sharing of the
   group the strip belongs to. See :ref:`Track and Bus Groups
   <track_and_bus_groups>` for more details

``/select/group/select *state*``
   where *state* is an int which shows the select sharing of the group
   the strip belongs to. See :ref:`Track and Bus Groups
   <track_and_bus_groups>` for more details.

``/select/group/active *state*``
   where *state* is an int which shows the route active sharing of the
   group the strip belongs to. See :ref:`Track and Bus Groups
   <track_and_bus_groups>` for more details.

``/select/group/color *state*``
   where *state* is an int which shows the color sharing of the group
   the strip belongs to. See :ref:`Track and Bus Groups
   <track_and_bus_groups>` for more details.

``/select/group/monitoring *state*``
   where *state* is an int which shows the monitoring sharing of the
   group the strip belongs to. See :ref:`Track and Bus Groups
   <track_and_bus_groups>` for more details.

``/select/vcas *name* *state* ...``
   where *name* is a string with the name of the VCA, and *state* is an
   int that determines if the named VCA will control this strip. Note
   that this lists all VCAs in a session.

Selected plugin
~~~~~~~~~~~~~~~

Feedback about plugin parameters is sent only for a single, selected
plugin (parameters for other plugins and other strips can be changed
with ``/select/plugin/parameter`` and ``/strip/plugin/parameter``, but
without feedback). Whenever the plugin (or strip) changes, the name and
activation of the plugin and name and value of a number of its
parameters (determined by the plugin page size) is sent as feedback.

``/select/plugin/name *name*``
   where *name* is a string with the name of the selected plugin.

``/select/plugin/parameter/name *paid* *name*``
   where *name* is a string with the name of the specified parameter.

``select/plugin/parameter *paid* *value*``
   where *value* is a float ranging from ``0`` to ``1`` representing the
   current parameter value.

Menu actions
~~~~~~~~~~~~

There is no feedback for Menu actions.

Every single menu item in Ardour's GUI is accessible via OSC. However,
there is no provision for returning the state of anything set this way.
This is not a bad thing as most menu items either do not have an on/off
state or that state is quite visible. Bindings that affect other
parameters that OSC does track will show on those OSC controls. Examples
of this might be track record enable for tracks 1 to 32, play or stop.