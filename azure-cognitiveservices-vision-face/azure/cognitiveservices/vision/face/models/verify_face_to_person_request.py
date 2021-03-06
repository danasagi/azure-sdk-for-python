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


class VerifyFaceToPersonRequest(Model):
    """Request body for face to person verification.

    All required parameters must be populated in order to send to Azure.

    :param face_id: Required. FaceId of the face, comes from Face - Detect
    :type face_id: str
    :param person_group_id: Using existing personGroupId and personId for fast
     loading a specified person. personGroupId is created in PersonGroup -
     Create. Parameter personGroupId and largePersonGroupId should not be
     provided at the same time.
    :type person_group_id: str
    :param large_person_group_id: Using existing largePersonGroupId and
     personId for fast loading a specified person. largePersonGroupId is
     created in LargePersonGroup - Create. Parameter personGroupId and
     largePersonGroupId should not be provided at the same time.
    :type large_person_group_id: str
    :param person_id: Required. Specify a certain person in a person group or
     a large person group. personId is created in PersonGroup Person - Create
     or LargePersonGroup Person - Create.
    :type person_id: str
    """

    _validation = {
        'face_id': {'required': True},
        'person_group_id': {'max_length': 64, 'pattern': r'^[a-z0-9-_]+$'},
        'large_person_group_id': {'max_length': 64, 'pattern': r'^[a-z0-9-_]+$'},
        'person_id': {'required': True},
    }

    _attribute_map = {
        'face_id': {'key': 'faceId', 'type': 'str'},
        'person_group_id': {'key': 'personGroupId', 'type': 'str'},
        'large_person_group_id': {'key': 'largePersonGroupId', 'type': 'str'},
        'person_id': {'key': 'personId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VerifyFaceToPersonRequest, self).__init__(**kwargs)
        self.face_id = kwargs.get('face_id', None)
        self.person_group_id = kwargs.get('person_group_id', None)
        self.large_person_group_id = kwargs.get('large_person_group_id', None)
        self.person_id = kwargs.get('person_id', None)
