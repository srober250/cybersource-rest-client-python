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


class EmbeddedInstrumentIdentifierRequest(object):
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
        'id': 'str',
        'card': 'TmsV1InstrumentIdentifiersPost200ResponseCard',
        'bank_account': 'Tmsv1instrumentidentifiersBankAccount'
    }

    attribute_map = {
        'id': 'id',
        'card': 'card',
        'bank_account': 'bankAccount'
    }

    def __init__(self, id=None, card=None, bank_account=None):
        """
        EmbeddedInstrumentIdentifierRequest - a model defined in Swagger
        """

        self._id = None
        self._card = None
        self._bank_account = None

        if id is not None:
          self.id = id
        if card is not None:
          self.card = card
        if bank_account is not None:
          self.bank_account = bank_account

    @property
    def id(self):
        """
        Gets the id of this EmbeddedInstrumentIdentifierRequest.
        The ID of the existing instrument identifier to be linked to the newly created payment instrument.

        :return: The id of this EmbeddedInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EmbeddedInstrumentIdentifierRequest.
        The ID of the existing instrument identifier to be linked to the newly created payment instrument.

        :param id: The id of this EmbeddedInstrumentIdentifierRequest.
        :type: str
        """
        if id is not None and len(id) > 32:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `32`")
        if id is not None and len(id) < 16:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `16`")

        self._id = id

    @property
    def card(self):
        """
        Gets the card of this EmbeddedInstrumentIdentifierRequest.

        :return: The card of this EmbeddedInstrumentIdentifierRequest.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this EmbeddedInstrumentIdentifierRequest.

        :param card: The card of this EmbeddedInstrumentIdentifierRequest.
        :type: TmsV1InstrumentIdentifiersPost200ResponseCard
        """

        self._card = card

    @property
    def bank_account(self):
        """
        Gets the bank_account of this EmbeddedInstrumentIdentifierRequest.

        :return: The bank_account of this EmbeddedInstrumentIdentifierRequest.
        :rtype: Tmsv1instrumentidentifiersBankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """
        Sets the bank_account of this EmbeddedInstrumentIdentifierRequest.

        :param bank_account: The bank_account of this EmbeddedInstrumentIdentifierRequest.
        :type: Tmsv1instrumentidentifiersBankAccount
        """

        self._bank_account = bank_account

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
        if not isinstance(other, EmbeddedInstrumentIdentifierRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
