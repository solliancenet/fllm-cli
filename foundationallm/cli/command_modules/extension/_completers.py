# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from foundationallm.cli.core.decorators import Completer
from foundationallm.cli.core.extension import get_extension_names

from foundationallm.cli.core.extension.operations import get_index_extensions


@Completer
def extension_name_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    return get_extension_names()


@Completer
def extension_name_from_index_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    return get_index_extensions(cli_ctx=cmd.cli_ctx).keys()
