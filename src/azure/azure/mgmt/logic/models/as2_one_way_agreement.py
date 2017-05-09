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


class AS2OneWayAgreement(Model):
    """AS2OneWayAgreement.

    :param sender_business_identity: The sender business identity
    :type sender_business_identity: :class:`BusinessIdentity
     <azure.mgmt.logic.models.BusinessIdentity>`
    :param receiver_business_identity: The receiver business identity
    :type receiver_business_identity: :class:`BusinessIdentity
     <azure.mgmt.logic.models.BusinessIdentity>`
    :param protocol_settings: The AS2 protocol settings.
    :type protocol_settings: :class:`AS2ProtocolSettings
     <azure.mgmt.logic.models.AS2ProtocolSettings>`
    """ 

    _attribute_map = {
        'sender_business_identity': {'key': 'senderBusinessIdentity', 'type': 'BusinessIdentity'},
        'receiver_business_identity': {'key': 'receiverBusinessIdentity', 'type': 'BusinessIdentity'},
        'protocol_settings': {'key': 'protocolSettings', 'type': 'AS2ProtocolSettings'},
    }

    def __init__(self, sender_business_identity=None, receiver_business_identity=None, protocol_settings=None):
        self.sender_business_identity = sender_business_identity
        self.receiver_business_identity = receiver_business_identity
        self.protocol_settings = protocol_settings
