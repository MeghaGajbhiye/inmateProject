# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GenerateUpgradedDefinitionParameters(Model):
    """GenerateUpgradedDefinitionParameters.

    :param target_schema_version: The target schema version.
    :type target_schema_version: str
    """ 

    _attribute_map = {
        'target_schema_version': {'key': 'targetSchemaVersion', 'type': 'str'},
    }

    def __init__(self, target_schema_version=None):
        self.target_schema_version = target_schema_version
