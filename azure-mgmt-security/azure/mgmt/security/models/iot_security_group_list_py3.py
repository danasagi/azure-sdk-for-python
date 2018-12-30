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


class IotSecurityGroupList(Model):
    """List of IoT security groups.

    :param value: List of IoT security group objects
    :type value: list[~azure.mgmt.security.models.IotSecurityGroup]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[IotSecurityGroup]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(IotSecurityGroupList, self).__init__(**kwargs)
        self.value = value