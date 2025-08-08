.. _osc_selection_and_expansion_considerations:

Selection and expansion considerations
======================================

Ardour does not send every possible feedback value for each channel. It
does send expanded information on the selected channel. There are also
extra commands for the selected strip.

All the feedback and select commands have their own path ``/select``.
This means that for the selected channel the surface does not have to
keep track of the strip ID. The ``/select`` strip will follow the
"current mixer strip" in the GUI editor window.

There are two major uses for this:

#. Single strip control surfaces. Using ``/access_action
   Editor/select-next-route`` or ``/access_action
   Editor/select-prev-route`` to step through the mixer strips.
#. Using a "Super strip" section of knobs to control parts of the strip
   that are changed less often such as polarity, sends or plugin
   parameters.

Selection in Ardour's OSC implementation are complicated by the
possibility of using more than one OSC controller at the same time. User
"A" may select strip 4 and use a selected controller to make changes to
that strip. User "B" may subsequently select strip 7 to make changes on.
This leaves user "A" making changes to strip 7 which they did not
choose.

For this reason Ardour offers local expansion aside from the GUI
selection. Local expansion only affects the one OSC controller. GUI
selection is global and affects all controllers using GUI selection as
well as the GUI.

Both select and expansion use the ``/select`` set of commands.

In general, in a one user situation where that one user may use either
the OSC surface or the GUI, using GUI based selection makes the most
sense. This is the default because this is the more common use.

When there is more than one operator, then expansion only is the mode of
choice. It may make sense for one of the surfaces to use GUI selection
where the operator is also using the GUI for some things. However, the
set up should be carefully analyzed for the possibility of selection
confusions. Expansion should be considered the *safe* option.

It is always OK to use expansion on the surface even in a one user
scenario. This allows the user to use GUI and surface selection for
different uses.

It is also possible to use both if desired. ``/strip/select`` will ways
set the GUI select, but /strip/expand will set the select feedback and
commands locally without changing the GUI select. Another
``/strip/expand`` or a ``/strip/select`` will override that expand
command and releasing the ``/strip/expand`` or ``/select/expand``
(setting it to ``0`` or ``false``) will set the ``/select`` set of
commands and feedback back to whichever strip the GUI has selected at
that time. This could be used to switch between the GUI select and the
local expand to compare two strips settings.
