# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ArmPlan(Model):
    """The plan object in an ARM, represents a marketplace plan.

    :param name: The name
    :type name: str
    :param publisher: The publisher
    :type publisher: str
    :param product: The product
    :type product: str
    :param promotion_code: The promotion code
    :type promotion_code: str
    :param version: Version of product
    :type version: str
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'promotion_code': {'key': 'promotionCode', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, name=None, publisher=None, product=None, promotion_code=None, version=None):
        self.name = name
        self.publisher = publisher
        self.product = product
        self.promotion_code = promotion_code
        self.version = version
