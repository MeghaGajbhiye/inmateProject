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


class JobSchedulingError(Model):
    """An error encountered by the Batch service when scheduling a job.

    :param category: The category of the job scheduling error. Possible
     values include: 'usererror', 'servererror', 'unmapped'
    :type category: str or :class:`SchedulingErrorCategory
     <azure.batch.models.SchedulingErrorCategory>`
    :param code: An identifier for the job scheduling error. Codes are
     invariant and are intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the job scheduling error, intended
     to be suitable for display in a user interface.
    :type message: str
    :param details: A list of additional error details related to the
     scheduling error.
    :type details: list of :class:`NameValuePair
     <azure.batch.models.NameValuePair>`
    """ 

    _validation = {
        'category': {'required': True},
    }

    _attribute_map = {
        'category': {'key': 'category', 'type': 'SchedulingErrorCategory'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[NameValuePair]'},
    }

    def __init__(self, category, code=None, message=None, details=None):
        self.category = category
        self.code = code
        self.message = message
        self.details = details
