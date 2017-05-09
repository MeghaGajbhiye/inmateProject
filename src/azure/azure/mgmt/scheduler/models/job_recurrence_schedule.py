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


class JobRecurrenceSchedule(Model):
    """JobRecurrenceSchedule.

    :param week_days: Gets or sets the days of the week that the job should
     execute on.
    :type week_days: list of str or :class:`DayOfWeek
     <azure.mgmt.scheduler.models.DayOfWeek>`
    :param hours: Gets or sets the hours of the day that the job should
     execute at.
    :type hours: list of int
    :param minutes: Gets or sets the minutes of the hour that the job should
     execute at.
    :type minutes: list of int
    :param month_days: Gets or sets the days of the month that the job should
     execute on. Must be between 1 and 31.
    :type month_days: list of int
    :param monthly_occurrences: Gets or sets the occurrences of days within a
     month.
    :type monthly_occurrences: list of
     :class:`JobRecurrenceScheduleMonthlyOccurrence
     <azure.mgmt.scheduler.models.JobRecurrenceScheduleMonthlyOccurrence>`
    """ 

    _attribute_map = {
        'week_days': {'key': 'weekDays', 'type': '[DayOfWeek]'},
        'hours': {'key': 'hours', 'type': '[int]'},
        'minutes': {'key': 'minutes', 'type': '[int]'},
        'month_days': {'key': 'monthDays', 'type': '[int]'},
        'monthly_occurrences': {'key': 'monthlyOccurrences', 'type': '[JobRecurrenceScheduleMonthlyOccurrence]'},
    }

    def __init__(self, week_days=None, hours=None, minutes=None, month_days=None, monthly_occurrences=None):
        self.week_days = week_days
        self.hours = hours
        self.minutes = minutes
        self.month_days = month_days
        self.monthly_occurrences = monthly_occurrences
