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

from enum import Enum


class ZoneType(str, Enum):

    public = "Public"
    private = "Private"


class RecordType(str, Enum):

    a = "A"
    aaaa = "AAAA"
    caa = "CAA"
    cname = "CNAME"
    mx = "MX"
    ns = "NS"
    ptr = "PTR"
    soa = "SOA"
    srv = "SRV"
    txt = "TXT"
