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


class AvailableSkuRequest(Model):
    """The filters for showing the available skus.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar transfer_type: Required. Type of the transfer. Default value:
     "ImportToAzure" .
    :vartype transfer_type: str
    :param country: Required. ISO country code. Country for hardware shipment.
     For codes check:
     https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements
    :type country: str
    :param location: Required. Location for data transfer. For locations
     check:
     https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-90-90
    :type location: str
    :param sku_names: Sku Names to filter for available skus
    :type sku_names: list[str or ~azure.mgmt.databox.models.SkuName]
    """

    _validation = {
        'transfer_type': {'required': True, 'constant': True},
        'country': {'required': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'transfer_type': {'key': 'transferType', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'sku_names': {'key': 'skuNames', 'type': '[SkuName]'},
    }

    transfer_type = "ImportToAzure"

    def __init__(self, *, country: str, location: str, sku_names=None, **kwargs) -> None:
        super(AvailableSkuRequest, self).__init__(**kwargs)
        self.country = country
        self.location = location
        self.sku_names = sku_names
