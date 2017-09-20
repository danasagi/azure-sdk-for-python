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


class ResumeClusterUpgradeDescription(Model):
    """Describes the parameters for resuming a cluster upgrade.

    :param upgrade_domain: The next upgrade domain for this cluster upgrade.
    :type upgrade_domain: str
    """ 

    _validation = {
        'upgrade_domain': {'required': True},
    }

    _attribute_map = {
        'upgrade_domain': {'key': 'UpgradeDomain', 'type': 'str'},
    }

    def __init__(self, upgrade_domain):
        self.upgrade_domain = upgrade_domain