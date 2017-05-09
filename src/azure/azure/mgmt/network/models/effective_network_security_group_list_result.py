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


class EffectiveNetworkSecurityGroupListResult(Model):
    """Response for list effective network security groups api service call.

    :param value: Gets list of effective network security groups
    :type value: list of :class:`EffectiveNetworkSecurityGroup
     <azure.mgmt.network.models.EffectiveNetworkSecurityGroup>`
    :param next_link: Gets the URL to get the next set of results.
    :type next_link: str
    """ 

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EffectiveNetworkSecurityGroup]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, value=None, next_link=None):
        self.value = value
        self.next_link = next_link
