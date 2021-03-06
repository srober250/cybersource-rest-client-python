# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'strong_authentication': 'RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformationStrongAuthentication'
    }

    attribute_map = {
        'strong_authentication': 'strongAuthentication'
    }

    def __init__(self, strong_authentication=None):
        """
        RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation - a model defined in Swagger
        """

        self._strong_authentication = None

        if strong_authentication is not None:
          self.strong_authentication = strong_authentication

    @property
    def strong_authentication(self):
        """
        Gets the strong_authentication of this RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation.

        :return: The strong_authentication of this RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation.
        :rtype: RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformationStrongAuthentication
        """
        return self._strong_authentication

    @strong_authentication.setter
    def strong_authentication(self, strong_authentication):
        """
        Sets the strong_authentication of this RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation.

        :param strong_authentication: The strong_authentication of this RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation.
        :type: RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformationStrongAuthentication
        """

        self._strong_authentication = strong_authentication

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
