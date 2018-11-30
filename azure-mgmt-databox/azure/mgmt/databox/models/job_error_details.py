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


class JobErrorDetails(Model):
    """Job Error Details for providing the information and recommended action.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar error_message: Message for the error.
    :vartype error_message: str
    :ivar error_code: Code for the error.
    :vartype error_code: int
    :ivar recommended_action: Recommended action for the error.
    :vartype recommended_action: str
    :ivar exception_message: Contains the non localized exception message
    :vartype exception_message: str
    """

    _validation = {
        'error_message': {'readonly': True},
        'error_code': {'readonly': True},
        'recommended_action': {'readonly': True},
        'exception_message': {'readonly': True},
    }

    _attribute_map = {
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'int'},
        'recommended_action': {'key': 'recommendedAction', 'type': 'str'},
        'exception_message': {'key': 'exceptionMessage', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(JobErrorDetails, self).__init__(**kwargs)
        self.error_message = None
        self.error_code = None
        self.recommended_action = None
        self.exception_message = None
