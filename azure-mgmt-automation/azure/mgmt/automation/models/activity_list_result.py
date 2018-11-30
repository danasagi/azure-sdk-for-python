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


class ActivityListResult(Model):
    """The response model for the list activity operation.

    :param value: Gets or sets a list of activities.
    :type value: list[~azure.mgmt.automation.models.Activity]
    :param next_link: Gets or sets the next link.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Activity]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ActivityListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)