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


class WorkflowTriggerCallbackUrl(Model):
    """WorkflowTriggerCallbackUrl.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: Gets the workflow trigger callback URL.
    :vartype value: str
    """ 

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self):
        self.value = None
