#
# This file is part of TEN Framework, an open source project.
# Licensed under the Apache License, Version 2.0.
# See the LICENSE file for more information.
#
from ten import (
    Addon,
    register_addon_as_extension,
    TenEnv,
)


@register_addon_as_extension("coze_python_async")
class AsyncCozeExtensionAddon(Addon):

    def on_create_instance(self, ten_env: TenEnv, name: str, context) -> None:
        from .extension import AsyncCozeExtension

        ten_env.log_info("AsyncCozeExtensionAddon on_create_instance")
        ten_env.on_create_instance_done(AsyncCozeExtension(name), context)
