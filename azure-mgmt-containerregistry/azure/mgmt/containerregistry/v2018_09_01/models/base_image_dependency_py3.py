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


class BaseImageDependency(Model):
    """Properties that describe a base image dependency.

    :param type: The type of the base image dependency. Possible values
     include: 'BuildTime', 'RunTime'
    :type type: str or
     ~azure.mgmt.containerregistry.v2018_09_01.models.BaseImageDependencyType
    :param registry: The registry login server.
    :type registry: str
    :param repository: The repository name.
    :type repository: str
    :param tag: The tag name.
    :type tag: str
    :param digest: The sha256-based digest of the image manifest.
    :type digest: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'registry': {'key': 'registry', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'str'},
        'tag': {'key': 'tag', 'type': 'str'},
        'digest': {'key': 'digest', 'type': 'str'},
    }

    def __init__(self, *, type=None, registry: str=None, repository: str=None, tag: str=None, digest: str=None, **kwargs) -> None:
        super(BaseImageDependency, self).__init__(**kwargs)
        self.type = type
        self.registry = registry
        self.repository = repository
        self.tag = tag
        self.digest = digest
