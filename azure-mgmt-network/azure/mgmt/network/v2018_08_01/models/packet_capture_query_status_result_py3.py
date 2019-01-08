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


class PacketCaptureQueryStatusResult(Model):
    """Status of packet capture session.

    :param name: The name of the packet capture resource.
    :type name: str
    :param id: The ID of the packet capture resource.
    :type id: str
    :param capture_start_time: The start time of the packet capture session.
    :type capture_start_time: datetime
    :param packet_capture_status: The status of the packet capture session.
     Possible values include: 'NotStarted', 'Running', 'Stopped', 'Error',
     'Unknown'
    :type packet_capture_status: str or
     ~azure.mgmt.network.v2018_08_01.models.PcStatus
    :param stop_reason: The reason the current packet capture session was
     stopped.
    :type stop_reason: str
    :param packet_capture_error: List of errors of packet capture session.
    :type packet_capture_error: list[str or
     ~azure.mgmt.network.v2018_08_01.models.PcError]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'capture_start_time': {'key': 'captureStartTime', 'type': 'iso-8601'},
        'packet_capture_status': {'key': 'packetCaptureStatus', 'type': 'str'},
        'stop_reason': {'key': 'stopReason', 'type': 'str'},
        'packet_capture_error': {'key': 'packetCaptureError', 'type': '[str]'},
    }

    def __init__(self, *, name: str=None, id: str=None, capture_start_time=None, packet_capture_status=None, stop_reason: str=None, packet_capture_error=None, **kwargs) -> None:
        super(PacketCaptureQueryStatusResult, self).__init__(**kwargs)
        self.name = name
        self.id = id
        self.capture_start_time = capture_start_time
        self.packet_capture_status = packet_capture_status
        self.stop_reason = stop_reason
        self.packet_capture_error = packet_capture_error
