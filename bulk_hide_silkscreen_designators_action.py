#!/usr/bin/env python
import pcbnew
import os.path
import wx


def _get_selected_footprints() -> list[pcbnew.FOOTPRINT]:
    return [
        footprint
        for footprint in pcbnew.GetCurrentSelection()
        if type(footprint).__name__ == "FOOTPRINT"
    ]


def _show_no_footprints_selected_dialog():
    dlg = wx.MessageDialog(
        None,
        "Please select one or multiple footprints!\n...or use Ctrl+A to select everything.",
        "No footprints selected",
        wx.OK | wx.ICON_ERROR,
    )
    dlg.ShowModal()
    dlg.Destroy()


def _get_selected_footprints_or_warn() -> list[pcbnew.FOOTPRINT]:
    selected_footprints = _get_selected_footprints()
    if len(selected_footprints) == 0:
        _show_no_footprints_selected_dialog()
    return selected_footprints


class BulkToggleSilkscreenDesignators(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Bulk Toggle silkscreen designators"
        self.category = "Silkscreen"
        self.description = "Hide/Show all silkscreen reference designators for selected footprints"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "icon.png")

    def Run(self):
        selected_footprints = _get_selected_footprints_or_warn()
        if len(selected_footprints) == 0:
            return

        for selected_footprint in selected_footprints:
            reference = selected_footprint.Reference()
            if reference:
                reference.SetVisible(not reference.IsVisible())

        pcbnew.Refresh()


BulkHideSilkscreenDesignators = BulkToggleSilkscreenDesignators
