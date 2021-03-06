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


class CertificateVerificationDescription(Model):
    """The JSON-serialized leaf certificate.

    :param certificate: base-64 representation of X509 certificate .cer file
     or just .pem file content.
    :type certificate: str
    """

    _attribute_map = {
        'certificate': {'key': 'certificate', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CertificateVerificationDescription, self).__init__(**kwargs)
        self.certificate = kwargs.get('certificate', None)
