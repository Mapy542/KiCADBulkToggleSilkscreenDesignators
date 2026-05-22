# "Bulk Toggle Silkscreen Designators" KiCAD plugin

"Bulk Toggle Silkscreen Designators" is a plugin for KiCAD that adds two toolbar actions for reference designators on selected footprints:

- Bulk Toggle silkscreen designators toggles the selected reference designators on or off.
- Bulk Hide silkscreen designators always turns the selected reference designators off.

This project is forked from "Bulk Hide Silkscreen Designators" by ulikoehler.

## Installation

### Via KiCad Plugin Manager (recommended)

1. Open KiCad and go to **PCB Editor → Tools → Plugin and Content Manager**.
2. Click **Manage** next to "Repositories".
3. Click **+** and add the following URL:
    ```
    https://raw.githubusercontent.com/Mapy542/KiCADBulkToggleSilkscreenDesignators/master/repository.json
    ```
4. Click **OK**, then **Refresh**. The plugin will appear in the list.
5. Click **Install** and then **Apply Pending Changes**.

### Manual installation

Download the latest `kicad-package.zip` from the [Releases](https://github.com/Mapy542/KiCADBulkToggleSilkscreenDesignators/releases) page and install it via **Plugin and Content Manager → Install from File**.

## Remaining README content from the original plugin:

Only the reference designators on the `F.Silkscreen` and `B.Silkscreen` layer are affected. `F.Fab` and `B.Fab` are not affected.

## Motivation

If you design PCBs with lots of fotprints close together, the reference designators will overlap.
Since using the EDA data for assembly & maintenance is preferred anyway, the silkscreen designators serve little purpose in practice.

Without using this plugin, you will have to manually hide the reference designators on each footprint.

## Usage

1. Select the footprints you want to toggle or hide the reference designators on. Most often you want to just select everything using Ctrl+A.
2. Click one of the toolbar icons:

    - Toggle visibility: ![Toggle icon](icon.png)
    - Hide only: ![Hide icon](icon-hide.png)

3. Drink a coffee! You MUST drink a coffee after using this plugin. Without this crucial step, all the time saved will go to waste.

### Before using the plugin

![Before using the plugin](/before.png)

### After using the hide action

![After using the plugin](/after.png)

Click the toggle icon again to turn the designators back on. The hide-only icon keeps them disabled.
