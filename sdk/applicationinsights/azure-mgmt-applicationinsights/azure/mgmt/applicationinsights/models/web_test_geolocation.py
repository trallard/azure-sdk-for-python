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


class WebTestGeolocation(Model):
    """Geo-physical location to run a web test from. You must specify one or more
    locations for the test to run from.

    :param location: Location ID for the webtest to run from.
    :type location: str
    """

    _attribute_map = {
        'location': {'key': 'Id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WebTestGeolocation, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
