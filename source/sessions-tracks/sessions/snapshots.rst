.. _snapshots:

Snapshots
=========

A snapshot is a backup of the current state of a session. It differs from a simple save by allowing branching. It is a "frozen" version of the session at a certain point in time.

For example, creating a snapshot before changing the entire arrangement of a piece, or drastically altering the signal processing provides a reference to come back to, should that not work out.

This is accomplished by using either of the **Session > Snapshot** menus. A small dialog will appear, allowing to enter a name for the snapshot. The default name is based on the current date and time.

The difference between the two snapshot menus is:

Snapshot (& keep working on current version)…
   Saves a snapshot of the session, but keeps the current session active, i.e. any subsequent **Session > Save** will overwrite the original session, and the snapshot will remain unchanged.

Snapshot (& switch to new version)…
   Saves a snapshot of the session, and uses this snapshot as the current active session, i.e. any subsequent **Session > Save** will overwrite the snapshot, and the original session will remain unchanged.

Any number of snapshots can be created.

.. warning::
   Creating a snapshot does **not** modify the session, nor does it save the session. Instead, it saves an alternate version of the session, within the session folder. The snapshot shares all data present in the session.

Switching to a Snapshot
-----------------------

Switching to an existing snapshot is done by navigating the :ref:`Snapshot List <the_snapshot_list>` and clicking the the name of the desired snapshot. Ardour will switch to the snapshot, and, if there are unsaved changes in the current session, offer to save them.

Starting Ardour With a Snapshot
-------------------------------

Since a snapshot is just another session file stored within the session folder, that "version" can be chosen when loading an existing session. The browser in the **Open Session** dialog will show an expander arrow for sessions that have more than one session file (i.e. snapshots) present. Clicking on it shows the list, and then clicking on the name of the snapshot loads it.
