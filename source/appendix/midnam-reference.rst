.. _midnam_reference:

MIDNAM reference
================

Add information of how these files are defined instead of telling the
user to go modify an existing file, also, remove the “you” language!

Adding a custom MIDNAM file
---------------------------

MIDNAM files are XML, and can be edited using any text editor. When
doing so, please ensure to change the "Model" of the device, as Ardour
will only load each model once (i.e. it will skip files, if there are
clashes).

After you have done modifications to a file, it is a good idea to
validate it. This can be done using the tool ``xmllint`` as shown below:

.. code:: bash

   $ xmllint --valid --noout myfile.midnam
   $ wget http://www.midi.org/dtds/MIDINameDocument10.dtd
   $ xmllint --dtdvalid MIDINameDocument10.dtd myfile.midnam

Once you are satisfied with your file, you have to put it at a location
where Ardour picks it up. The best place would be the (hidden) directory
:ref:`Ardour configuration directory
<@@files_and_directories_ardour_knows_about>` subdirectory patchfiles.
in your home-folder. Should the sub-directory ``patchfiles`` not exist
yet, just create it. The path and file-names are case-sensitive. The
file should end with ``.midnam``.

After restarting Ardour, hit the small Log-button in the upper right
corner of the main window. It should say something like (this is Linux,
macOS, or Windows will be different):

::

   [INFO]: Loading 3 MIDI patches from /home/username/.config/ardour8/patchfiles

The added device should now show up in the dropdown mentioned in the
previous paragraph.

Sharing the MIDNAM file
-----------------------

Should the MIDNAM-file be useful for the general public, it would be
nice to share it: Fork the Ardour-project on
`GitHub <https://github.com/Ardour/ardour>`__ by hitting the
**Fork** button. Go to the patchfiles-directory (and read the README).

You can upload the file using the Web-Interface. Be sure to select
"*Create a new branch for this commit and start a pull request*".
