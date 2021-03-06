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


class Riskv1liststypeentriesPaymentInformationCard(object):
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
        'number': 'str',
        'type': 'str',
        'bin': 'str'
    }

    attribute_map = {
        'number': 'number',
        'type': 'type',
        'bin': 'bin'
    }

    def __init__(self, number=None, type=None, bin=None):
        """
        Riskv1liststypeentriesPaymentInformationCard - a model defined in Swagger
        """

        self._number = None
        self._type = None
        self._bin = None

        if number is not None:
          self.number = number
        if type is not None:
          self.type = type
        if bin is not None:
          self.bin = bin

    @property
    def number(self):
        """
        Gets the number of this Riskv1liststypeentriesPaymentInformationCard.
        The customer’s payment card number, also known as the Primary Account Number (PAN). You can also use this field for encoded account numbers.  For processor-specific information, see the `customer_cc_number` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The number of this Riskv1liststypeentriesPaymentInformationCard.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Riskv1liststypeentriesPaymentInformationCard.
        The customer’s payment card number, also known as the Primary Account Number (PAN). You can also use this field for encoded account numbers.  For processor-specific information, see the `customer_cc_number` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param number: The number of this Riskv1liststypeentriesPaymentInformationCard.
        :type: str
        """
        if number is not None and len(number) > 20:
            raise ValueError("Invalid value for `number`, length must be less than or equal to `20`")

        self._number = number

    @property
    def type(self):
        """
        Gets the type of this Riskv1liststypeentriesPaymentInformationCard.
        Three-digit value that indicates the card type.  Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover - 005: Diners Club - 007: JCB - 024: Maestro (UK Domestic) - 036: Cartes Bancaires - 039 Encoded account number - 042: Maestro (International)  For the complete list of possible values, see `card_type` field description in the [Credit Card Services Using the SCMP API Guide.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The type of this Riskv1liststypeentriesPaymentInformationCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Riskv1liststypeentriesPaymentInformationCard.
        Three-digit value that indicates the card type.  Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover - 005: Diners Club - 007: JCB - 024: Maestro (UK Domestic) - 036: Cartes Bancaires - 039 Encoded account number - 042: Maestro (International)  For the complete list of possible values, see `card_type` field description in the [Credit Card Services Using the SCMP API Guide.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param type: The type of this Riskv1liststypeentriesPaymentInformationCard.
        :type: str
        """

        self._type = type

    @property
    def bin(self):
        """
        Gets the bin of this Riskv1liststypeentriesPaymentInformationCard.
        description: The BIN is the first six digits of the card's Primary Account Number (PAN). 

        :return: The bin of this Riskv1liststypeentriesPaymentInformationCard.
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """
        Sets the bin of this Riskv1liststypeentriesPaymentInformationCard.
        description: The BIN is the first six digits of the card's Primary Account Number (PAN). 

        :param bin: The bin of this Riskv1liststypeentriesPaymentInformationCard.
        :type: str
        """
        if bin is not None and len(bin) > 6:
            raise ValueError("Invalid value for `bin`, length must be less than or equal to `6`")

        self._bin = bin

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
        if not isinstance(other, Riskv1liststypeentriesPaymentInformationCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
