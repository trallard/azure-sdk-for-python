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


class Inconsistency(Model):
    """Inconsistency.

    All required parameters must be populated in order to send to Azure.

    :param inconsistent_series_ids: Required. IDs of inconsistent series in
     the time series group.
    :type inconsistent_series_ids: list[str]
    :param confidence_scores: Required. Scores of inconsistent series in the
     time series group.
    :type confidence_scores: list[float]
    :param begin: Required. Start time of the time series group.
    :type begin: datetime
    :param end: Required. End time of the time series group.
    :type end: datetime
    :param epsilon: Parameter to be tuned to get inconsistency.
    :type epsilon: float
    """

    _validation = {
        'inconsistent_series_ids': {'required': True},
        'confidence_scores': {'required': True},
        'begin': {'required': True},
        'end': {'required': True},
    }

    _attribute_map = {
        'inconsistent_series_ids': {'key': 'inconsistentSeriesIds', 'type': '[str]'},
        'confidence_scores': {'key': 'confidenceScores', 'type': '[float]'},
        'begin': {'key': 'begin', 'type': 'iso-8601'},
        'end': {'key': 'end', 'type': 'iso-8601'},
        'epsilon': {'key': 'epsilon', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(Inconsistency, self).__init__(**kwargs)
        self.inconsistent_series_ids = kwargs.get('inconsistent_series_ids', None)
        self.confidence_scores = kwargs.get('confidence_scores', None)
        self.begin = kwargs.get('begin', None)
        self.end = kwargs.get('end', None)
        self.epsilon = kwargs.get('epsilon', None)
