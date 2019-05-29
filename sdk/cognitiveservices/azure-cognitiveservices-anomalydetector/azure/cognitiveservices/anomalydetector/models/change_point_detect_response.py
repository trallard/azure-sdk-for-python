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


class ChangePointDetectResponse(Model):
    """ChangePointDetectResponse.

    All required parameters must be populated in order to send to Azure.

    :param period: Required. Frequency extracted from the series, zero means
     no recurrent pattern has been found.
    :type period: int
    :param is_change_point: Required. isChangePoint contains change point
     properties for each input point. True means an anomaly either negative or
     positive has been detected. The index of the array is consistent with the
     input series.
    :type is_change_point: list[bool]
    :param confidence_scores: Required. the change point confidence of each
     point
    :type confidence_scores: list[float]
    """

    _validation = {
        'period': {'required': True},
        'is_change_point': {'required': True},
        'confidence_scores': {'required': True},
    }

    _attribute_map = {
        'period': {'key': 'period', 'type': 'int'},
        'is_change_point': {'key': 'isChangePoint', 'type': '[bool]'},
        'confidence_scores': {'key': 'confidenceScores', 'type': '[float]'},
    }

    def __init__(self, **kwargs):
        super(ChangePointDetectResponse, self).__init__(**kwargs)
        self.period = kwargs.get('period', None)
        self.is_change_point = kwargs.get('is_change_point', None)
        self.confidence_scores = kwargs.get('confidence_scores', None)
