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


class Schedule(Model):
    """A schedule.

    :param status: The status of the schedule. Possible values include:
     'Enabled', 'Disabled'
    :type status: str or ~azure.mgmt.devtestlabs.models.EnableStatus
    :param task_type: The task type of the schedule. Possible values include:
     'LabVmsShutdownTask', 'LabVmsStartupTask', 'LabBillingTask'
    :type task_type: str or ~azure.mgmt.devtestlabs.models.TaskType
    :param weekly_recurrence: The weekly recurrence of the schedule.
    :type weekly_recurrence: ~azure.mgmt.devtestlabs.models.WeekDetails
    :param daily_recurrence: The daily recurrence of the schedule.
    :type daily_recurrence: ~azure.mgmt.devtestlabs.models.DayDetails
    :param hourly_recurrence: The hourly recurrence of the schedule.
    :type hourly_recurrence: ~azure.mgmt.devtestlabs.models.HourDetails
    :param time_zone_id: The time zone id.
    :type time_zone_id: str
    :param provisioning_state: The provisioning status of the resource.
    :type provisioning_state: str
    :param id: The identifier of the resource.
    :type id: str
    :param name: The name of the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'status': {'key': 'properties.status', 'type': 'str'},
        'task_type': {'key': 'properties.taskType', 'type': 'str'},
        'weekly_recurrence': {'key': 'properties.weeklyRecurrence', 'type': 'WeekDetails'},
        'daily_recurrence': {'key': 'properties.dailyRecurrence', 'type': 'DayDetails'},
        'hourly_recurrence': {'key': 'properties.hourlyRecurrence', 'type': 'HourDetails'},
        'time_zone_id': {'key': 'properties.timeZoneId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Schedule, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.task_type = kwargs.get('task_type', None)
        self.weekly_recurrence = kwargs.get('weekly_recurrence', None)
        self.daily_recurrence = kwargs.get('daily_recurrence', None)
        self.hourly_recurrence = kwargs.get('hourly_recurrence', None)
        self.time_zone_id = kwargs.get('time_zone_id', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
