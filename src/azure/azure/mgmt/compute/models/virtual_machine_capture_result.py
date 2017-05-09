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

from .sub_resource import SubResource


class VirtualMachineCaptureResult(SubResource):
    """Resource Id.

    :param id: Resource Id
    :type id: str
    :param output: Operation output data (raw JSON)
    :type output: object
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'output': {'key': 'properties.output', 'type': 'object'},
    }

    def __init__(self, id=None, output=None):
        super(VirtualMachineCaptureResult, self).__init__(id=id)
        self.output = output
