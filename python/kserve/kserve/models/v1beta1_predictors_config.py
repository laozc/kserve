# Copyright 2021 The KServe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KServe

    Python SDK for KServe  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kserve.configuration import Configuration


class V1beta1PredictorsConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'lightgbm': 'V1beta1PredictorConfig',
        'onnx': 'V1beta1PredictorConfig',
        'paddle': 'V1beta1PredictorConfig',
        'pmml': 'V1beta1PredictorConfig',
        'pytorch': 'V1beta1PredictorConfig',
        'sklearn': 'V1beta1PredictorProtocols',
        'tensorflow': 'V1beta1PredictorConfig',
        'triton': 'V1beta1PredictorConfig',
        'xgboost': 'V1beta1PredictorProtocols'
    }

    attribute_map = {
        'lightgbm': 'lightgbm',
        'onnx': 'onnx',
        'paddle': 'paddle',
        'pmml': 'pmml',
        'pytorch': 'pytorch',
        'sklearn': 'sklearn',
        'tensorflow': 'tensorflow',
        'triton': 'triton',
        'xgboost': 'xgboost'
    }

    def __init__(self, lightgbm=None, onnx=None, paddle=None, pmml=None, pytorch=None, sklearn=None, tensorflow=None, triton=None, xgboost=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1PredictorsConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._lightgbm = None
        self._onnx = None
        self._paddle = None
        self._pmml = None
        self._pytorch = None
        self._sklearn = None
        self._tensorflow = None
        self._triton = None
        self._xgboost = None
        self.discriminator = None

        if lightgbm is not None:
            self.lightgbm = lightgbm
        if onnx is not None:
            self.onnx = onnx
        if paddle is not None:
            self.paddle = paddle
        if pmml is not None:
            self.pmml = pmml
        if pytorch is not None:
            self.pytorch = pytorch
        if sklearn is not None:
            self.sklearn = sklearn
        if tensorflow is not None:
            self.tensorflow = tensorflow
        if triton is not None:
            self.triton = triton
        if xgboost is not None:
            self.xgboost = xgboost

    @property
    def lightgbm(self):
        """Gets the lightgbm of this V1beta1PredictorsConfig.  # noqa: E501


        :return: The lightgbm of this V1beta1PredictorsConfig.  # noqa: E501
        :rtype: V1beta1PredictorConfig
        """
        return self._lightgbm

    @lightgbm.setter
    def lightgbm(self, lightgbm):
        """Sets the lightgbm of this V1beta1PredictorsConfig.


        :param lightgbm: The lightgbm of this V1beta1PredictorsConfig.  # noqa: E501
        :type: V1beta1PredictorConfig
        """

        self._lightgbm = lightgbm

    @property
    def onnx(self):
        """Gets the onnx of this V1beta1PredictorsConfig.  # noqa: E501


        :return: The onnx of this V1beta1PredictorsConfig.  # noqa: E501
        :rtype: V1beta1PredictorConfig
        """
        return self._onnx

    @onnx.setter
    def onnx(self, onnx):
        """Sets the onnx of this V1beta1PredictorsConfig.


        :param onnx: The onnx of this V1beta1PredictorsConfig.  # noqa: E501
        :type: V1beta1PredictorConfig
        """

        self._onnx = onnx

    @property
    def paddle(self):
        """Gets the paddle of this V1beta1PredictorsConfig.  # noqa: E501


        :return: The paddle of this V1beta1PredictorsConfig.  # noqa: E501
        :rtype: V1beta1PredictorConfig
        """
        return self._paddle

    @paddle.setter
    def paddle(self, paddle):
        """Sets the paddle of this V1beta1PredictorsConfig.


        :param paddle: The paddle of this V1beta1PredictorsConfig.  # noqa: E501
        :type: V1beta1PredictorConfig
        """

        self._paddle = paddle

    @property
    def pmml(self):
        """Gets the pmml of this V1beta1PredictorsConfig.  # noqa: E501


        :return: The pmml of this V1beta1PredictorsConfig.  # noqa: E501
        :rtype: V1beta1PredictorConfig
        """
        return self._pmml

    @pmml.setter
    def pmml(self, pmml):
        """Sets the pmml of this V1beta1PredictorsConfig.


        :param pmml: The pmml of this V1beta1PredictorsConfig.  # noqa: E501
        :type: V1beta1PredictorConfig
        """

        self._pmml = pmml

    @property
    def pytorch(self):
        """Gets the pytorch of this V1beta1PredictorsConfig.  # noqa: E501


        :return: The pytorch of this V1beta1PredictorsConfig.  # noqa: E501
        :rtype: V1beta1PredictorConfig
        """
        return self._pytorch

    @pytorch.setter
    def pytorch(self, pytorch):
        """Sets the pytorch of this V1beta1PredictorsConfig.


        :param pytorch: The pytorch of this V1beta1PredictorsConfig.  # noqa: E501
        :type: V1beta1PredictorConfig
        """

        self._pytorch = pytorch

    @property
    def sklearn(self):
        """Gets the sklearn of this V1beta1PredictorsConfig.  # noqa: E501


        :return: The sklearn of this V1beta1PredictorsConfig.  # noqa: E501
        :rtype: V1beta1PredictorProtocols
        """
        return self._sklearn

    @sklearn.setter
    def sklearn(self, sklearn):
        """Sets the sklearn of this V1beta1PredictorsConfig.


        :param sklearn: The sklearn of this V1beta1PredictorsConfig.  # noqa: E501
        :type: V1beta1PredictorProtocols
        """

        self._sklearn = sklearn

    @property
    def tensorflow(self):
        """Gets the tensorflow of this V1beta1PredictorsConfig.  # noqa: E501


        :return: The tensorflow of this V1beta1PredictorsConfig.  # noqa: E501
        :rtype: V1beta1PredictorConfig
        """
        return self._tensorflow

    @tensorflow.setter
    def tensorflow(self, tensorflow):
        """Sets the tensorflow of this V1beta1PredictorsConfig.


        :param tensorflow: The tensorflow of this V1beta1PredictorsConfig.  # noqa: E501
        :type: V1beta1PredictorConfig
        """

        self._tensorflow = tensorflow

    @property
    def triton(self):
        """Gets the triton of this V1beta1PredictorsConfig.  # noqa: E501


        :return: The triton of this V1beta1PredictorsConfig.  # noqa: E501
        :rtype: V1beta1PredictorConfig
        """
        return self._triton

    @triton.setter
    def triton(self, triton):
        """Sets the triton of this V1beta1PredictorsConfig.


        :param triton: The triton of this V1beta1PredictorsConfig.  # noqa: E501
        :type: V1beta1PredictorConfig
        """

        self._triton = triton

    @property
    def xgboost(self):
        """Gets the xgboost of this V1beta1PredictorsConfig.  # noqa: E501


        :return: The xgboost of this V1beta1PredictorsConfig.  # noqa: E501
        :rtype: V1beta1PredictorProtocols
        """
        return self._xgboost

    @xgboost.setter
    def xgboost(self, xgboost):
        """Sets the xgboost of this V1beta1PredictorsConfig.


        :param xgboost: The xgboost of this V1beta1PredictorsConfig.  # noqa: E501
        :type: V1beta1PredictorProtocols
        """

        self._xgboost = xgboost

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1PredictorsConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1PredictorsConfig):
            return True

        return self.to_dict() != other.to_dict()
