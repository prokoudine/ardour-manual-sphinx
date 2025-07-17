.. _arrangement:

Arrangement
===========

The **Arrangement** ruler allows creating range sections that separate meaningful parts of songs form each other and easily creating their copies. An example of using range sections would recording an intro, then the first verse, then the chorus, then recording the second verse, the copy/pasting the chorus with all tracks and automation to follow the second verse.

On the screenshot below, there's a typical setup with an intro, a verse, a chorus, a second verse, a chorus, a bridge, a chorus, and an outro:

.. figure:: images/arrangement-example.png
   :alt: Arrangement example

   Arrangement example

Creating range sections
-----------------------

To start a new range section, press :kbd:`Ctrl` and single-click on the Arrangement ruler. Ardour will create a new range section marker named 'verseN', where N is a number starting at 1 and incremented each time you create a new range section marker.

Because range section assume ranges, a second marker should be created the same way to define the end of the range. Thus, as the song ends with an 'outro' section, you will need to create the last range section marker at the end of the song and give it a name like 'end'.

Editing range sections
----------------------

To move the position of a range section marker, single-click and drag it left or right.

To rename a range section marker, either double-click it, or right-click, then select the **Rename…** menu item. This will open a dialog for editing the caption/name of the range section.

Removing range sections
-----------------------

To remove a range section marker, right-click it ans select the **Remove** menu item.
