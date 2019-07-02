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


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Location(Model):
    """Location information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID of the location. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000/locations/westus.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    :ivar name: The location name.
    :vartype name: str
    :ivar display_name: The display name of the location.
    :vartype display_name: str
    :ivar latitude: The latitude of the location.
    :vartype latitude: str
    :ivar longitude: The longitude of the location.
    :vartype longitude: str
    """

    _validation = {
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'name': {'readonly': True},
        'display_name': {'readonly': True},
        'latitude': {'readonly': True},
        'longitude': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'latitude': {'key': 'latitude', 'type': 'str'},
        'longitude': {'key': 'longitude', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Location, self).__init__(**kwargs)
        self.id = None
        self.subscription_id = None
        self.name = None
        self.display_name = None
        self.latitude = None
        self.longitude = None


class Operation(Model):
    """Microsoft.Resources operation.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that represents the operation.
    :type display:
     ~azure.mgmt.resource.subscriptions.v2018_06_01.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OperationDisplay(Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.Resources
    :type provider: str
    :param resource: Resource on which the operation is performed: Profile,
     endpoint, etc.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    :param description: Description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class Subscription(Model):
    """Subscription information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID for the subscription. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    :ivar display_name: The subscription display name.
    :vartype display_name: str
    :ivar tenant_id: The subscription tenant ID.
    :vartype tenant_id: str
    :ivar state: The subscription state. Possible values are Enabled, Warned,
     PastDue, Disabled, and Deleted. Possible values include: 'Enabled',
     'Warned', 'PastDue', 'Disabled', 'Deleted'
    :vartype state: str or
     ~azure.mgmt.resource.subscriptions.v2018_06_01.models.SubscriptionState
    :param subscription_policies: The subscription policies.
    :type subscription_policies:
     ~azure.mgmt.resource.subscriptions.v2018_06_01.models.SubscriptionPolicies
    :param authorization_source: The authorization source of the request.
     Valid values are one or more combinations of Legacy, RoleBased, Bypassed,
     Direct and Management. For example, 'Legacy, RoleBased'.
    :type authorization_source: str
    """

    _validation = {
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'display_name': {'readonly': True},
        'tenant_id': {'readonly': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'SubscriptionState'},
        'subscription_policies': {'key': 'subscriptionPolicies', 'type': 'SubscriptionPolicies'},
        'authorization_source': {'key': 'authorizationSource', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Subscription, self).__init__(**kwargs)
        self.id = None
        self.subscription_id = None
        self.display_name = None
        self.tenant_id = None
        self.state = None
        self.subscription_policies = kwargs.get('subscription_policies', None)
        self.authorization_source = kwargs.get('authorization_source', None)


class SubscriptionPolicies(Model):
    """Subscription policies.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar location_placement_id: The subscription location placement ID. The
     ID indicates which regions are visible for a subscription. For example, a
     subscription with a location placement Id of Public_2014-09-01 has access
     to Azure public regions.
    :vartype location_placement_id: str
    :ivar quota_id: The subscription quota ID.
    :vartype quota_id: str
    :ivar spending_limit: The subscription spending limit. Possible values
     include: 'On', 'Off', 'CurrentPeriodOff'
    :vartype spending_limit: str or
     ~azure.mgmt.resource.subscriptions.v2018_06_01.models.SpendingLimit
    """

    _validation = {
        'location_placement_id': {'readonly': True},
        'quota_id': {'readonly': True},
        'spending_limit': {'readonly': True},
    }

    _attribute_map = {
        'location_placement_id': {'key': 'locationPlacementId', 'type': 'str'},
        'quota_id': {'key': 'quotaId', 'type': 'str'},
        'spending_limit': {'key': 'spendingLimit', 'type': 'SpendingLimit'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionPolicies, self).__init__(**kwargs)
        self.location_placement_id = None
        self.quota_id = None
        self.spending_limit = None


class TenantIdDescription(Model):
    """Tenant Id information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID of the tenant. For example,
     /tenants/00000000-0000-0000-0000-000000000000.
    :vartype id: str
    :ivar tenant_id: The tenant ID. For example,
     00000000-0000-0000-0000-000000000000.
    :vartype tenant_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TenantIdDescription, self).__init__(**kwargs)
        self.id = None
        self.tenant_id = None
