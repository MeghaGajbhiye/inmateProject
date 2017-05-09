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


class X12FramingSettings(Model):
    """X12FramingSettings.

    :param data_element_separator: The data element separator.
    :type data_element_separator: int
    :param component_separator: The component separator.
    :type component_separator: int
    :param replace_separators_in_payload: The value indicating whether to
     replace separators in payload.
    :type replace_separators_in_payload: bool
    :param replace_character: The replacement character.
    :type replace_character: int
    :param segment_terminator: The segment terminator.
    :type segment_terminator: int
    :param character_set: The X12 character set. Possible values include:
     'NotSpecified', 'Basic', 'Extended', 'UTF8'
    :type character_set: str or :class:`X12CharacterSet
     <azure.mgmt.logic.models.X12CharacterSet>`
    :param segment_terminator_suffix: The segment terminator suffix. Possible
     values include: 'NotSpecified', 'None', 'CR', 'LF', 'CRLF'
    :type segment_terminator_suffix: str or :class:`SegmentTerminatorSuffix
     <azure.mgmt.logic.models.SegmentTerminatorSuffix>`
    """ 

    _attribute_map = {
        'data_element_separator': {'key': 'dataElementSeparator', 'type': 'int'},
        'component_separator': {'key': 'componentSeparator', 'type': 'int'},
        'replace_separators_in_payload': {'key': 'replaceSeparatorsInPayload', 'type': 'bool'},
        'replace_character': {'key': 'replaceCharacter', 'type': 'int'},
        'segment_terminator': {'key': 'segmentTerminator', 'type': 'int'},
        'character_set': {'key': 'characterSet', 'type': 'X12CharacterSet'},
        'segment_terminator_suffix': {'key': 'segmentTerminatorSuffix', 'type': 'SegmentTerminatorSuffix'},
    }

    def __init__(self, data_element_separator=None, component_separator=None, replace_separators_in_payload=None, replace_character=None, segment_terminator=None, character_set=None, segment_terminator_suffix=None):
        self.data_element_separator = data_element_separator
        self.component_separator = component_separator
        self.replace_separators_in_payload = replace_separators_in_payload
        self.replace_character = replace_character
        self.segment_terminator = segment_terminator
        self.character_set = character_set
        self.segment_terminator_suffix = segment_terminator_suffix
