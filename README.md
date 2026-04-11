# "Bulk Toggle Silkscreen Designators" KiCAD plugin

"Bulk Toggle Silkscreen Designators" is a plugin for KiCAD that allows you to toggle the visibility of reference designators on the silkscreen layers for multiple footprints at once. Forked from "Bulk Hide Silkscreen Designators" by ulikoehler.

## Remaining README content from the original plugin:

Only the reference designators on the `F.Silkscreen` and `B.Silkscreen` layer are hidden. `F.Fab` and `B.Fab` are not affected.

## Motivation

If you design PCBs with lots of fotprints close together, the reference designators will overlap.
Since using the EDA data for assembly & maintenance is preferred anyway, the silkscreen designators serve little purpose in practice.

Without using this plugin, you will have to manually hide the reference designators on each footprint.

## Usage

1. Select the footprints you want to hide the reference designators on. Most often you want to just select everything using Ctrl+A.
2. Click on the icon in the toolbar: ![Icon](/icon.png)
3. Drink a coffee! You MUST drink a coffee after using this plugin. Without this crucial step, all the time saved will go to waste.

### Before "Bulk hide Silkscreen Designators"

![Before using the plugin](/before.png)

### After "Bulk hide Silkscreen Designators"

![After using the plugin](/after.png)
