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


class JobScheduleAddParameter(Model):
    """A job schedule that allows recurring jobs by specifying when to run jobs
    and a specification used to create each job.

    :param id: A string that uniquely identifies the schedule within the
     account.
    :type id: str
    :param display_name: The display name for the schedule.
    :type display_name: str
    :param schedule: The schedule according to which jobs will be created.
    :type schedule: :class:`Schedule <azure.batch.models.Schedule>`
    :param job_specification: The details of the jobs to be created on this
     schedule.
    :type job_specification: :class:`JobSpecification
     <azure.batch.models.JobSpecification>`
    :param metadata: A list of name-value pairs associated with the schedule
     as metadata.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    """ 

    _validation = {
        'id': {'required': True},
        'schedule': {'required': True},
        'job_specification': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'schedule': {'key': 'schedule', 'type': 'Schedule'},
        'job_specification': {'key': 'jobSpecification', 'type': 'JobSpecification'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, id, schedule, job_specification, display_name=None, metadata=None):
        self.id = id
        self.display_name = display_name
        self.schedule = schedule
        self.job_specification = job_specification
        self.metadata = metadata
