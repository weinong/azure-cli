# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class ComputeDataDisk(Model):
    """ComputeDataDisk.

    :param name: Gets data disk name.
    :type name: str
    :param disk_uri: When backed by a blob, the URI of underlying blob.
    :type disk_uri: str
    :param managed_disk_id: When backed by managed disk, this is the ID of the
     compute disk resource.
    :type managed_disk_id: str
    :param disk_size_gi_b: Gets data disk size in GiB.
    :type disk_size_gi_b: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'disk_uri': {'key': 'diskUri', 'type': 'str'},
        'managed_disk_id': {'key': 'managedDiskId', 'type': 'str'},
        'disk_size_gi_b': {'key': 'diskSizeGiB', 'type': 'int'},
    }

    def __init__(self, name=None, disk_uri=None, managed_disk_id=None, disk_size_gi_b=None):
        self.name = name
        self.disk_uri = disk_uri
        self.managed_disk_id = managed_disk_id
        self.disk_size_gi_b = disk_size_gi_b
