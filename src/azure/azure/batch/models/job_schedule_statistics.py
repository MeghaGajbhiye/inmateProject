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


class JobScheduleStatistics(Model):
    """Resource usage statistics for a job schedule.

    :param url: The URL of the statistics.
    :type url: str
    :param start_time: The start time of the time range covered by the
     statistics.
    :type start_time: datetime
    :param last_update_time: The time at which the statistics were last
     updated. All statistics are limited to the range between startTime and
     lastUpdateTime.
    :type last_update_time: datetime
    :param user_cpu_time: The total user mode CPU time (summed across all
     cores and all compute nodes) consumed by all tasks in all jobs created
     under the schedule.
    :type user_cpu_time: timedelta
    :param kernel_cpu_time: The total kernel mode CPU time (summed across all
     cores and all compute nodes) consumed by all tasks in all jobs created
     under the schedule.
    :type kernel_cpu_time: timedelta
    :param wall_clock_time: The total wall clock time of all the tasks in all
     the jobs created under the schedule.
    :type wall_clock_time: timedelta
    :param read_iops: The total number of disk read operations made by all
     tasks in all jobs created under the schedule.
    :type read_iops: long
    :param write_iops: The total number of disk write operations made by all
     tasks in all jobs created under the schedule.
    :type write_iops: long
    :param read_io_gi_b: The total gibibytes read from disk by all tasks in
     all jobs created under the schedule.
    :type read_io_gi_b: float
    :param write_io_gi_b: The total gibibytes written to disk by all tasks in
     all jobs created under the schedule.
    :type write_io_gi_b: float
    :param num_succeeded_tasks: The total number of tasks successfully
     completed during the given time range in jobs created under the
     schedule. A task completes successfully if it returns exit code 0.
    :type num_succeeded_tasks: long
    :param num_failed_tasks: The total number of tasks that failed during the
     given time range in jobs created under the schedule. A task fails if it
     exhausts its maximum retry count without returning exit code 0.
    :type num_failed_tasks: long
    :param num_task_retries: The total number of retries during the given
     time range on all tasks in all jobs created under the schedule.
    :type num_task_retries: long
    :param wait_time: The total wait time of all tasks in all jobs created
     under the schedule. The wait time for a task is defined as the elapsed
     time between the creation of the task and the start of task execution.
     (If the task is retried due to failures, the wait time is the time to
     the most recent task execution.).
    :type wait_time: timedelta
    """ 

    _validation = {
        'url': {'required': True},
        'start_time': {'required': True},
        'last_update_time': {'required': True},
        'user_cpu_time': {'required': True},
        'kernel_cpu_time': {'required': True},
        'wall_clock_time': {'required': True},
        'read_iops': {'required': True},
        'write_iops': {'required': True},
        'read_io_gi_b': {'required': True},
        'write_io_gi_b': {'required': True},
        'num_succeeded_tasks': {'required': True},
        'num_failed_tasks': {'required': True},
        'num_task_retries': {'required': True},
        'wait_time': {'required': True},
    }

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'user_cpu_time': {'key': 'userCPUTime', 'type': 'duration'},
        'kernel_cpu_time': {'key': 'kernelCPUTime', 'type': 'duration'},
        'wall_clock_time': {'key': 'wallClockTime', 'type': 'duration'},
        'read_iops': {'key': 'readIOps', 'type': 'long'},
        'write_iops': {'key': 'writeIOps', 'type': 'long'},
        'read_io_gi_b': {'key': 'readIOGiB', 'type': 'float'},
        'write_io_gi_b': {'key': 'writeIOGiB', 'type': 'float'},
        'num_succeeded_tasks': {'key': 'numSucceededTasks', 'type': 'long'},
        'num_failed_tasks': {'key': 'numFailedTasks', 'type': 'long'},
        'num_task_retries': {'key': 'numTaskRetries', 'type': 'long'},
        'wait_time': {'key': 'waitTime', 'type': 'duration'},
    }

    def __init__(self, url, start_time, last_update_time, user_cpu_time, kernel_cpu_time, wall_clock_time, read_iops, write_iops, read_io_gi_b, write_io_gi_b, num_succeeded_tasks, num_failed_tasks, num_task_retries, wait_time):
        self.url = url
        self.start_time = start_time
        self.last_update_time = last_update_time
        self.user_cpu_time = user_cpu_time
        self.kernel_cpu_time = kernel_cpu_time
        self.wall_clock_time = wall_clock_time
        self.read_iops = read_iops
        self.write_iops = write_iops
        self.read_io_gi_b = read_io_gi_b
        self.write_io_gi_b = write_io_gi_b
        self.num_succeeded_tasks = num_succeeded_tasks
        self.num_failed_tasks = num_failed_tasks
        self.num_task_retries = num_task_retries
        self.wait_time = wait_time
