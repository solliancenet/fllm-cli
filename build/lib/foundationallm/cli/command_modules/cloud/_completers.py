# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from foundationallm.cli.core.cloud import get_custom_clouds
from foundationallm.cli.core.decorators import Completer

from foundationallm.cli.command_modules.cloud.custom import get_clouds


@Completer
def get_cloud_name_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    return [c.name for c in get_clouds(cmd.cli_ctx)]


@Completer
def get_custom_cloud_name_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    return [c.name for c in get_custom_clouds(cmd.cli_ctx)]
