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


class StorageAccountUpdateParameters(Model):
    """The parameters to provide for the account.

    :param sku: Gets or sets the sku type. Note that sku cannot be updated to
     StandardZRS or ProvisionedLRS, nor can accounts of that sku type be
     updated to any other value.
    :type sku: :class:`Sku <azure.mgmt.storage.models.Sku>`
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict
    :param custom_domain: User domain assigned to the storage account. Name
     is the CNAME source. Only one custom domain is supported per storage
     account at this time. To clear the existing custom domain, use an empty
     string for the custom domain name property.
    :type custom_domain: :class:`CustomDomain
     <azure.mgmt.storage.models.CustomDomain>`
    :param encryption: Provides the encryption settings on the account. The
     default setting is unencrypted.
    :type encryption: :class:`Encryption
     <azure.mgmt.storage.models.Encryption>`
    :param access_tier: The access tier used for billing. Access tier cannot
     be changed more than once every 7 days (168 hours). Access tier cannot
     be set for StandardLRS, StandardGRS, StandardRAGRS, or PremiumLRS
     account types. Possible values include: 'Hot', 'Cool'
    :type access_tier: str or :class:`AccessTier
     <azure.mgmt.storage.models.AccessTier>`
    """ 

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'encryption': {'key': 'properties.encryption', 'type': 'Encryption'},
        'access_tier': {'key': 'properties.accessTier', 'type': 'AccessTier'},
    }

    def __init__(self, sku=None, tags=None, custom_domain=None, encryption=None, access_tier=None):
        self.sku = sku
        self.tags = tags
        self.custom_domain = custom_domain
        self.encryption = encryption
        self.access_tier = access_tier
