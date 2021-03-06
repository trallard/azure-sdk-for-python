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

from .arm_base_model import ARMBaseModel


class SecuritySettings(ARMBaseModel):
    """The security settings of a device.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The path ID that uniquely identifies the object.
    :vartype id: str
    :ivar name: The object name.
    :vartype name: str
    :ivar type: The hierarchical type of the object.
    :vartype type: str
    :param device_admin_password: Required. Device administrator password as
     an encrypted string (encrypted using RSA PKCS #1) is used to sign into the
     local web UI of the device. The Actual password should have at least 8
     characters that are a combination of  uppercase, lowercase, numeric, and
     special characters.
    :type device_admin_password:
     ~azure.mgmt.edgegateway.models.AsymmetricEncryptedSecret
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'device_admin_password': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'device_admin_password': {'key': 'properties.deviceAdminPassword', 'type': 'AsymmetricEncryptedSecret'},
    }

    def __init__(self, **kwargs):
        super(SecuritySettings, self).__init__(**kwargs)
        self.device_admin_password = kwargs.get('device_admin_password', None)
