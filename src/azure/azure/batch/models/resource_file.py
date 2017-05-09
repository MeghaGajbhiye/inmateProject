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


class ResourceFile(Model):
    """A file to be downloaded from Azure blob storage to a compute node.

    :param blob_source: The URL of the file within Azure Blob Storage. This
     URL should include a shared access signature if the blob is not publicly
     readable.
    :type blob_source: str
    :param file_path: The location to which to download the file, relative to
     the task's working directory.
    :type file_path: str
    :param file_mode: The file mode attribute in octal format. This property
     will be ignored if it is specified for a resourceFile which will be
     downloaded to a Windows compute node.
    :type file_mode: str
    """ 

    _validation = {
        'blob_source': {'required': True},
        'file_path': {'required': True},
    }

    _attribute_map = {
        'blob_source': {'key': 'blobSource', 'type': 'str'},
        'file_path': {'key': 'filePath', 'type': 'str'},
        'file_mode': {'key': 'fileMode', 'type': 'str'},
    }

    def __init__(self, blob_source, file_path, file_mode=None):
        self.blob_source = blob_source
        self.file_path = file_path
        self.file_mode = file_mode
