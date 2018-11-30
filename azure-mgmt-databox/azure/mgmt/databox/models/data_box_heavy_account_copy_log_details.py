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

from .copy_log_details import CopyLogDetails


class DataBoxHeavyAccountCopyLogDetails(CopyLogDetails):
    """Copy log details for a storage account for Databox heavy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param copy_log_details_type: Required. Constant filled by server.
    :type copy_log_details_type: str
    :ivar account_name: Destination account name.
    :vartype account_name: str
    :ivar copy_log_link: Link for copy logs.
    :vartype copy_log_link: list[str]
    """

    _validation = {
        'copy_log_details_type': {'required': True},
        'account_name': {'readonly': True},
        'copy_log_link': {'readonly': True},
    }

    _attribute_map = {
        'copy_log_details_type': {'key': 'copyLogDetailsType', 'type': 'str'},
        'account_name': {'key': 'accountName', 'type': 'str'},
        'copy_log_link': {'key': 'copyLogLink', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(DataBoxHeavyAccountCopyLogDetails, self).__init__(**kwargs)
        self.account_name = None
        self.copy_log_link = None
        self.copy_log_details_type = 'DataBoxHeavy'
