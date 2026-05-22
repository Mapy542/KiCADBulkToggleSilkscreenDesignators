#!/usr/bin/env python
import os.path

import pcbnew

from .bulk_hide_silkscreen_designators_action import _get_selected_footprints_or_warn


class BulkDisableSilkscreenDesignators(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Bulk Hide silkscreen designators"
        self.category = "Silkscreen"
        self.description = "Hide all silkscreen reference designators for selected footprints"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "icon-hide.png")

    def Run(self):
        selected_footprints = _get_selected_footprints_or_warn()
        if len(selected_footprints) == 0:
            return

        for selected_footprint in selected_footprints:
            reference = selected_footprint.Reference()
            if reference:
                reference.SetVisible(False)

        pcbnew.Refresh()
