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


class ServiceLevelObjectiveCapability(Model):
    """The service objectives capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The unique ID of the service objective.
    :vartype id: str
    :ivar name: The service objective name.
    :vartype name: str
    :ivar supported_max_sizes: The list of supported maximum database sizes
     for this service objective.
    :vartype supported_max_sizes:
     list[~azure.mgmt.sql.models.MaxSizeCapability]
    :ivar performance_level: The performance level of the service objective
     capability.
    :vartype performance_level:
     ~azure.mgmt.sql.models.PerformanceLevelCapability
    :ivar included_max_size: The included (free) max size for this service
     level objective.
    :vartype included_max_size: ~azure.mgmt.sql.models.MaxSizeCapability
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :param reason: The reason for the capability not being available.
    :type reason: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'supported_max_sizes': {'readonly': True},
        'performance_level': {'readonly': True},
        'included_max_size': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'supported_max_sizes': {'key': 'supportedMaxSizes', 'type': '[MaxSizeCapability]'},
        'performance_level': {'key': 'performanceLevel', 'type': 'PerformanceLevelCapability'},
        'included_max_size': {'key': 'includedMaxSize', 'type': 'MaxSizeCapability'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, *, reason: str=None, **kwargs) -> None:
        super(ServiceLevelObjectiveCapability, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.supported_max_sizes = None
        self.performance_level = None
        self.included_max_size = None
        self.status = None
        self.reason = reason