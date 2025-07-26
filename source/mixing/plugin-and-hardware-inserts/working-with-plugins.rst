.. _working_with_plugins:

Working with plugins
====================

**Plugins** are bits of software that get loaded by Ardour in order to:

-  Create various audio or MIDI effects
-  Generate audio by functioning as "software instruments"

they are usually written by 3rd parties, though a few :ref:`come bundled with
ardour <bundled_plugins>` (some are only available in official
builds distributed from ardour.org). the sources for plugins are many
and varied; see :ref:`here <getting_more_plugins>` for some information
on how to get them.

Ardour supports a variety of different plugin standards:


LADSPA
   An early, simple, lightweight plugin API, audio effects only, plugins have no editors/GUI of their own (Ardour provides one, however).

LV2
   An extensible, full-featured plugin API, audio and MIDI, plugins can provide their own GUIs but may use the one Ardour provides instead.

AU
   OS X only, full featured, audio and MIDI, plugins can provide their own GUI.

VST
   Plugins using Steinberg's VST2 and VST3 plugin standard.

Adding/Removing/Copying Plugins
-------------------------------

Within Ardour, plugins are just another type of **processor** and so the
techniques for adding/removing/copying/moving processors apply to
plugins as well. These techniques are covered on the :ref:`Processor Box
<processor_box>` page.
