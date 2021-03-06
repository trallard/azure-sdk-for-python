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

from .azure_workload_sql_recovery_point import AzureWorkloadSQLRecoveryPoint


class AzureWorkloadSQLPointInTimeRecoveryPoint(AzureWorkloadSQLRecoveryPoint):
    """Recovery point specific to PointInTime.

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_point_time_in_utc: UTC time at which recovery point was
     created
    :type recovery_point_time_in_utc: datetime
    :param type: Type of restore point. Possible values include: 'Invalid',
     'Full', 'Log', 'Differential'
    :type type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RestorePointType
    :param extended_info: Extended Info that provides data directory details.
     Will be populated in two cases:
     When a specific recovery point is accessed using GetRecoveryPoint
     Or when ListRecoveryPoints is called for Log RP only with ExtendedInfo
     query filter
    :type extended_info:
     ~azure.mgmt.recoveryservicesbackup.models.AzureWorkloadSQLRecoveryPointExtendedInfo
    :param time_ranges: List of log ranges
    :type time_ranges:
     list[~azure.mgmt.recoveryservicesbackup.models.PointInTimeRange]
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_point_time_in_utc': {'key': 'recoveryPointTimeInUTC', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'str'},
        'extended_info': {'key': 'extendedInfo', 'type': 'AzureWorkloadSQLRecoveryPointExtendedInfo'},
        'time_ranges': {'key': 'timeRanges', 'type': '[PointInTimeRange]'},
    }

    def __init__(self, **kwargs):
        super(AzureWorkloadSQLPointInTimeRecoveryPoint, self).__init__(**kwargs)
        self.time_ranges = kwargs.get('time_ranges', None)
        self.object_type = 'AzureWorkloadSQLPointInTimeRecoveryPoint'
