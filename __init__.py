#!/usr/bin/env python
from .bulk_disable_silkscreen_designators_action import BulkDisableSilkscreenDesignators
from .bulk_hide_silkscreen_designators_action import BulkToggleSilkscreenDesignators

BulkToggleSilkscreenDesignators().register()
BulkDisableSilkscreenDesignators().register()
