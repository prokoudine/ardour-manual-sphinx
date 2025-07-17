.. _track_context_menu:

Track context menu
==================

Within the editor window, context-clicking (right click) on either a region or empty space within a track displays the track context menu. The context menu provides easy access to many track-level operations.

If a region is clicked, the first item in the menu is the name of the region. If a :ref:`layered region <layering-display>` is clicked, the next item in the menu is Choose Top. If selected, a dialog appears that allows to change the vertical order of layers at that point. See :ref:`Layering Display <layering-display>` for more details.

The rest of the track context menu is structured as follows:

Play  
   (No description)

Play from Edit Point  
   Plays from the location of the current :ref:`Edit Point <edit_point_control>`.

Play from Start  
   Plays from the start of the session

Play Region  
   Plays the duration of the session from the start of the earliest selected region to the end of the latest selected region

Loop Region  
   Creates the loop range from the start/end positions of selected regions and plays the loop until stopped

Select  
   (No description)

Select All in Track  
   Selects all the regions and automation points in the current track

Select All Objects  
   Selects all the regions and automation points in the session

Invert Selection in Track  
   Select the previously unselected regions, and deselect the previously selected ones *only* in the current track

Invert Selection  
   Select the previously unselected regions, and deselect the previously selected ones

Set Range to Loop Range  
   Creates a range selection on the selected tracks, based on the selected loop markers, and switches to :ref:`Range Mode tool <toolbox_range>`

Set Range to Punch Range  
   Same as above, based on the selected punch markers

Set Range to Selected Regions  
   Same as above, based on the selected regions (i.e. from the start of the earliest region to the end of the latest one)

Select All After Edit Point  
   Select all the regions and automation points that exist after the Edit Point, even if the region starts before it. If some tracks are selected, only selects on these tracks.

Select All Before Edit Point  
   Same as above, but before the Edit point (i.e. to the left of it)

Select All After Playhead  
   Same as above, but considering the Playhead, regardless of the Edit Point choice

Select All Before Playhead  
   Same as above, with the Playhead

Select All Between Playhead and Edit Point  
   Selects all the regions between the Playhead and the Edit Point

Select All Within Playhead and Edit Point  
   Same as above, but the regions must be totally included between the Playhead and Edit Point

Select Range Between Playhead and Edit Point  
   Creates a Range between the Playhead and the Edit Point

Edit  
   (No description)

Cut  
   Deletes the current selection, but puts it in memory ready to be pasted

Copy  
   Copies the current selection to memory

Paste  
   Pastes the memory at the :ref:`Edit Point <edit_point_control>`, after a Cut or Copy operation

Align  
   Aligns the sync point of all selected regions to the Edit Point

Align Relative  
   Same as above, but considers multiple regions as a block and aligns the whole block, not each region

Insert Selected Region  
   If a region is selected in :ref:`the Region List <the_region_list>`, inserts it in the track

Insert Existing Media  
   Inserts an external media file in the track, same as :ref:`the Session > Insert Media menu <adding_pre_existing_material>`

Nudge  
   (No description)

Nudge Entire Track Later  
   Moves all the region to the right by the amount shown in the :ref:`nudge timer <nudge_controls>`

Nudge Track After Edit Point Later  
   Same as above, but only for regions that begin after the Edit Point

Nudge Entire Track Earlier  
   Same as above, to the left

Nudge Track After Edit Point Earlier  
   Same as above, to the left

(un)Freeze  
   Consolidates all the regions in the track into one *frozen* region which can be handled as a normal, single region. This operation can be undone at any time with the same sub-menu.
