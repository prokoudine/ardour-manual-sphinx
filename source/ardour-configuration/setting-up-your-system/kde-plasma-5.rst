KDE Plasma 5
============

Under KDE Plasma 5, plugin and various other windows will not stay on top of any main window; therefore a workaround is required.

Workaround
~~~~~~~~~~

In order to force ancillary windows in Ardour to stay on top, the following steps are necessary:

#. Launch the **System Settings** application.
#. Open :menuselection:`Workspace > Window Management`.
#. Select :guilabel:`Window Rules` in the left-hand sidebar. It should default to the :guilabel:`Window matching` tab.
#. Click on the :guilabel:`New…` button.
#. On the line that says :guilabel:`Window class (application)`, set the combo box to :guilabel:`Substring Match` and type ``ardour`` in the text entry field.
#. In the list box that is labeled :guilabel:`Window types:`, click on the option :guilabel:`Dialog Window`, then press and hold :kbd:`Ctrl` while clicking on the second option :guilabel:`Utility Window`.
#. Select the :guilabel:`Arrangement & Access` tab.
#. Check the box next to the :guilabel:`Keep above` option. On the same line, select :guilabel:`Force` from the combo box, then click on the :guilabel:`Yes` radio button for that line.
#. Click on the :guilabel:`OK` button to dismiss the dialog.

At this point the **System Settings** application can be closed.

Background info
~~~~~~~~~~~~~~~

`According to one of the lead KDE developers <https://bugs.kde.org/show_bug.cgi?id=172615#c26>`__, they are not willing to follow the ICCCM standard for utility windows. Apparently they are alone in this understanding, as plugin windows on Ardour under Linux work out of the box on every other WM out there.

Under KDE 4, there was a workaround in Ardour (:menuselection:`Preferences > Theme > All floating windows are dialogs`) that would "trick" KDE into forcing certain window types to be on top of their parent windows, but this no longer works under KDE Plasma 5.
