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


class TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard(object):
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
        'state': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'type': 'str',
        'card': 'TmsV1InstrumentIdentifiersPost200ResponseTokenizedCardCard'
    }

    attribute_map = {
        'state': 'state',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'type': 'type',
        'card': 'card'
    }

    def __init__(self, state=None, expiration_month=None, expiration_year=None, type=None, card=None):
        """
        TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard - a model defined in Swagger
        """

        self._state = None
        self._expiration_month = None
        self._expiration_year = None
        self._type = None
        self._card = None

        if state is not None:
          self.state = state
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if type is not None:
          self.type = type
        if card is not None:
          self.card = card

    @property
    def state(self):
        """
        Gets the state of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        Issuer state for the Network Token Valid values: - ACTIVE - SUSPENDED - DELETED 

        :return: The state of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        Issuer state for the Network Token Valid values: - ACTIVE - SUSPENDED - DELETED 

        :param state: The state of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :type: str
        """

        self._state = state

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        The Network Token expiration month, automatically updated

        :return: The expiration_month of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        The Network Token expiration month, automatically updated

        :param expiration_month: The expiration_month of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :type: str
        """
        if expiration_month is not None and len(expiration_month) > 2:
            raise ValueError("Invalid value for `expiration_month`, length must be less than or equal to `2`")
        if expiration_month is not None and len(expiration_month) < 2:
            raise ValueError("Invalid value for `expiration_month`, length must be greater than or equal to `2`")

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        The Network Token expiration year, automatically updated

        :return: The expiration_year of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        The Network Token expiration year, automatically updated

        :param expiration_year: The expiration_year of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :type: str
        """
        if expiration_year is not None and len(expiration_year) > 4:
            raise ValueError("Invalid value for `expiration_year`, length must be less than or equal to `4`")
        if expiration_year is not None and len(expiration_year) < 4:
            raise ValueError("Invalid value for `expiration_year`, length must be greater than or equal to `4`")

        self._expiration_year = expiration_year

    @property
    def type(self):
        """
        Gets the type of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        The Network Token brand Valid values: - visa - mastercard 

        :return: The type of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        The Network Token brand Valid values: - visa - mastercard 

        :param type: The type of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :type: str
        """

        self._type = type

    @property
    def card(self):
        """
        Gets the card of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.

        :return: The card of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseTokenizedCardCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.

        :param card: The card of this TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard.
        :type: TmsV1InstrumentIdentifiersPost200ResponseTokenizedCardCard
        """

        self._card = card

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
        if not isinstance(other, TmsV1InstrumentIdentifiersPost200ResponseTokenizedCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
