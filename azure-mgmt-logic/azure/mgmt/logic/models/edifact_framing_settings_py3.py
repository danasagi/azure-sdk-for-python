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


class EdifactFramingSettings(Model):
    """The Edifact agreement framing settings.

    All required parameters must be populated in order to send to Azure.

    :param service_code_list_directory_version: The service code list
     directory version.
    :type service_code_list_directory_version: str
    :param character_encoding: The character encoding.
    :type character_encoding: str
    :param protocol_version: Required. The protocol version.
    :type protocol_version: int
    :param data_element_separator: Required. The data element separator.
    :type data_element_separator: int
    :param component_separator: Required. The component separator.
    :type component_separator: int
    :param segment_terminator: Required. The segment terminator.
    :type segment_terminator: int
    :param release_indicator: Required. The release indicator.
    :type release_indicator: int
    :param repetition_separator: Required. The repetition separator.
    :type repetition_separator: int
    :param character_set: Required. The EDIFACT frame setting characterSet.
     Possible values include: 'NotSpecified', 'UNOB', 'UNOA', 'UNOC', 'UNOD',
     'UNOE', 'UNOF', 'UNOG', 'UNOH', 'UNOI', 'UNOJ', 'UNOK', 'UNOX', 'UNOY',
     'KECA'
    :type character_set: str or ~azure.mgmt.logic.models.EdifactCharacterSet
    :param decimal_point_indicator: Required. The EDIFACT frame setting
     decimal indicator. Possible values include: 'NotSpecified', 'Comma',
     'Decimal'
    :type decimal_point_indicator: str or
     ~azure.mgmt.logic.models.EdifactDecimalIndicator
    :param segment_terminator_suffix: Required. The EDIFACT frame setting
     segment terminator suffix. Possible values include: 'NotSpecified',
     'None', 'CR', 'LF', 'CRLF'
    :type segment_terminator_suffix: str or
     ~azure.mgmt.logic.models.SegmentTerminatorSuffix
    """

    _validation = {
        'protocol_version': {'required': True},
        'data_element_separator': {'required': True},
        'component_separator': {'required': True},
        'segment_terminator': {'required': True},
        'release_indicator': {'required': True},
        'repetition_separator': {'required': True},
        'character_set': {'required': True},
        'decimal_point_indicator': {'required': True},
        'segment_terminator_suffix': {'required': True},
    }

    _attribute_map = {
        'service_code_list_directory_version': {'key': 'serviceCodeListDirectoryVersion', 'type': 'str'},
        'character_encoding': {'key': 'characterEncoding', 'type': 'str'},
        'protocol_version': {'key': 'protocolVersion', 'type': 'int'},
        'data_element_separator': {'key': 'dataElementSeparator', 'type': 'int'},
        'component_separator': {'key': 'componentSeparator', 'type': 'int'},
        'segment_terminator': {'key': 'segmentTerminator', 'type': 'int'},
        'release_indicator': {'key': 'releaseIndicator', 'type': 'int'},
        'repetition_separator': {'key': 'repetitionSeparator', 'type': 'int'},
        'character_set': {'key': 'characterSet', 'type': 'str'},
        'decimal_point_indicator': {'key': 'decimalPointIndicator', 'type': 'EdifactDecimalIndicator'},
        'segment_terminator_suffix': {'key': 'segmentTerminatorSuffix', 'type': 'SegmentTerminatorSuffix'},
    }

    def __init__(self, *, protocol_version: int, data_element_separator: int, component_separator: int, segment_terminator: int, release_indicator: int, repetition_separator: int, character_set, decimal_point_indicator, segment_terminator_suffix, service_code_list_directory_version: str=None, character_encoding: str=None, **kwargs) -> None:
        super(EdifactFramingSettings, self).__init__(**kwargs)
        self.service_code_list_directory_version = service_code_list_directory_version
        self.character_encoding = character_encoding
        self.protocol_version = protocol_version
        self.data_element_separator = data_element_separator
        self.component_separator = component_separator
        self.segment_terminator = segment_terminator
        self.release_indicator = release_indicator
        self.repetition_separator = repetition_separator
        self.character_set = character_set
        self.decimal_point_indicator = decimal_point_indicator
        self.segment_terminator_suffix = segment_terminator_suffix
