﻿#-------------------------------------------------------------------------
# Copyright (c) Microsoft.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#--------------------------------------------------------------------------
from ._common_conversion import _to_str
from azure.common import (
    AzureHttpError,
    AzureConflictHttpError,
    AzureMissingResourceHttpError,
    AzureException,
)
from ._constants import (
    _ENCRYPTION_PROTOCOL_V1,
)
_ERROR_CONFLICT = 'Conflict ({0})'
_ERROR_NOT_FOUND = 'Not found ({0})'
_ERROR_UNKNOWN = 'Unknown error ({0})'
_ERROR_STORAGE_MISSING_INFO = \
    'You need to provide an account name and either an account_key or sas_token when creating a storage service.'
_ERROR_EMULATOR_DOES_NOT_SUPPORT_FILES = \
    'The emulator does not support the file service.'
_ERROR_ACCESS_POLICY = \
    'share_access_policy must be either SignedIdentifier or AccessPolicy ' + \
    'instance'
_ERROR_PARALLEL_NOT_SEEKABLE = 'Parallel operations require a seekable stream.'
_ERROR_VALUE_SHOULD_BE_BYTES = '{0} should be of type bytes.'
_ERROR_VALUE_NONE = '{0} should not be None.'
_ERROR_VALUE_NONE_OR_EMPTY = '{0} should not be None or empty.'
_ERROR_VALUE_NEGATIVE = '{0} should not be negative.'
_ERROR_NO_SINGLE_THREAD_CHUNKING = \
    'To use {0} chunk downloader more than 1 thread must be ' + \
    'used since get_{0}_to_bytes should be called for single threaded ' + \
    '{0} downloads.'
_ERROR_START_END_NEEDED_FOR_MD5 = \
    'Both end_range and start_range need to be specified ' + \
    'for getting content MD5.'
_ERROR_RANGE_TOO_LARGE_FOR_MD5 = \
    'Getting content MD5 for a range greater than 4MB ' + \
    'is not supported.'
_ERROR_MD5_MISMATCH = \
    'MD5 mismatch. Expected value is \'{0}\', computed value is \'{1}\'.'
_ERROR_TOO_MANY_ACCESS_POLICIES = \
    'Too many access policies provided. The server does not support setting more than 5 access policies on a single resource.'
_ERROR_OBJECT_INVALID = \
    '{0} does not define a complete interface. Value of {1} is either missing or invalid.'
_ERROR_UNSUPPORTED_ENCRYPTION_VERSION = \
    'Encryption version is not supported.'
_ERROR_DECRYPTION_FAILURE = \
    'Decryption failed' 
_ERROR_ENCRYPTION_REQUIRED = \
    'Encryption required but no key was provided.'
_ERROR_DECRYPTION_REQUIRED = \
    'Decryption required but neither key nor resolver was provided.' + \
    ' If you do not want to decypt, please do not set the require encryption flag.'
_ERROR_INVALID_KID = \
    'Provided or resolved key-encryption-key does not match the id of key used to encrypt.'
_ERROR_UNSUPPORTED_ENCRYPTION_ALGORITHM = \
    'Specified encryption algorithm is not supported.'
_ERROR_UNSUPPORTED_METHOD_FOR_ENCRYPTION = 'The require_encryption flag is set, but encryption is not supported' + \
    ' for this method.'
_ERROR_UNKNOWN_KEY_WRAP_ALGORITHM = 'Unknown key wrap algorithm.'
_ERROR_DATA_NOT_ENCRYPTED = 'Encryption required, but received data does not contain appropriate metatadata.' + \
    'Data was either not encrypted or metadata has been lost.'

def _dont_fail_on_exist(error):
    ''' don't throw exception if the resource exists.
    This is called by create_* APIs with fail_on_exist=False'''
    if isinstance(error, AzureConflictHttpError):
        return False
    else:
        raise error


def _dont_fail_not_exist(error):
    ''' don't throw exception if the resource doesn't exist.
    This is called by create_* APIs with fail_on_exist=False'''
    if isinstance(error, AzureMissingResourceHttpError):
        return False
    else:
        raise error


def _http_error_handler(http_error):
    ''' Simple error handler for azure.'''
    message = str(http_error)
    if http_error.respbody is not None:
        message += '\n' + http_error.respbody.decode('utf-8-sig')
    raise AzureHttpError(message, http_error.status)


def _validate_type_bytes(param_name, param):
    if not isinstance(param, bytes):
        raise TypeError(_ERROR_VALUE_SHOULD_BE_BYTES.format(param_name))

def _validate_not_none(param_name, param):
    if param is None:
        raise ValueError(_ERROR_VALUE_NONE.format(param_name))

def _validate_content_match(server_md5, computed_md5):
    if server_md5 != computed_md5:
        raise AzureException(_ERROR_MD5_MISMATCH.format(server_md5, computed_md5))

def _validate_access_policies(identifiers):
    if identifiers and len(identifiers) > 5:
        raise AzureException(_ERROR_TOO_MANY_ACCESS_POLICIES)
def _validate_key_encryption_key_wrap(kek):
    # Note that None is not callable and so will fail the second clause of each check.
    if not hasattr(kek, 'wrap_key') or not callable(kek.wrap_key):
        raise AttributeError(_ERROR_OBJECT_INVALID.format('key encryption key', 'wrap_key'))
    if not hasattr(kek, 'get_kid') or not callable(kek.get_kid):
        raise AttributeError(_ERROR_OBJECT_INVALID.format('key encryption key', 'get_kid'))
    if not hasattr(kek, 'get_key_wrap_algorithm') or not callable(kek.get_key_wrap_algorithm):
        raise AttributeError(_ERROR_OBJECT_INVALID.format('key encryption key', 'get_key_wrap_algorithm'))

def _validate_key_encryption_key_unwrap(kek):
    if not hasattr(kek, 'get_kid') or not callable(kek.get_kid):
        raise AttributeError(_ERROR_OBJECT_INVALID.format('key encryption key', 'get_kid'))
    if not hasattr(kek, 'unwrap_key') or not callable(kek.unwrap_key):
        raise AttributeError(_ERROR_OBJECT_INVALID.format('key encryption key', 'unwrap_key'))

def _validate_encryption_required(require_encryption, kek):
     if require_encryption and (kek is None):
            raise ValueError(_ERROR_ENCRYPTION_REQUIRED)

def _validate_decryption_required(require_encryption, kek, resolver):
    if(require_encryption and (kek is None) and 
           (resolver is None)):
            raise ValueError(_ERROR_DECRYPTION_REQUIRED)

def _validate_encryption_protocol_version(encryption_protocol):
    if not (_ENCRYPTION_PROTOCOL_V1 == encryption_protocol):
        raise ValueError(_ERROR_UNSUPPORTED_ENCRYPTION_VERSION)

def _validate_kek_id(kid, resolved_id):
    if not (kid == resolved_id):
        raise ValueError(_ERROR_INVALID_KID)

def _validate_encryption_unsupported(require_encryption, key_encryption_key):
    if require_encryption or (key_encryption_key is not None):
        raise ValueError(_ERROR_UNSUPPORTED_METHOD_FOR_ENCRYPTION)