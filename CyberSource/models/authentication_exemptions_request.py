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


class AuthenticationExemptionsRequest(object):
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
        'client_reference_information': 'PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation',
        'order_information': 'Riskv1authenticationexemptionsOrderInformation',
        'payment_information': 'Riskv1authenticationexemptionsPaymentInformation',
        'device_information': 'Riskv1authenticationexemptionsDeviceInformation',
        'merchant_information': 'Riskv1authenticationexemptionsMerchantInformation',
        'acquirer_information': 'Riskv1authenticationexemptionsAcquirerInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation',
        'device_information': 'deviceInformation',
        'merchant_information': 'merchantInformation',
        'acquirer_information': 'acquirerInformation'
    }

    def __init__(self, client_reference_information=None, order_information=None, payment_information=None, device_information=None, merchant_information=None, acquirer_information=None):
        """
        AuthenticationExemptionsRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._order_information = None
        self._payment_information = None
        self._device_information = None
        self._merchant_information = None
        self._acquirer_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information
        if device_information is not None:
          self.device_information = device_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if acquirer_information is not None:
          self.acquirer_information = acquirer_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this AuthenticationExemptionsRequest.

        :return: The client_reference_information of this AuthenticationExemptionsRequest.
        :rtype: PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this AuthenticationExemptionsRequest.

        :param client_reference_information: The client_reference_information of this AuthenticationExemptionsRequest.
        :type: PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def order_information(self):
        """
        Gets the order_information of this AuthenticationExemptionsRequest.

        :return: The order_information of this AuthenticationExemptionsRequest.
        :rtype: Riskv1authenticationexemptionsOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this AuthenticationExemptionsRequest.

        :param order_information: The order_information of this AuthenticationExemptionsRequest.
        :type: Riskv1authenticationexemptionsOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this AuthenticationExemptionsRequest.

        :return: The payment_information of this AuthenticationExemptionsRequest.
        :rtype: Riskv1authenticationexemptionsPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this AuthenticationExemptionsRequest.

        :param payment_information: The payment_information of this AuthenticationExemptionsRequest.
        :type: Riskv1authenticationexemptionsPaymentInformation
        """

        self._payment_information = payment_information

    @property
    def device_information(self):
        """
        Gets the device_information of this AuthenticationExemptionsRequest.

        :return: The device_information of this AuthenticationExemptionsRequest.
        :rtype: Riskv1authenticationexemptionsDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this AuthenticationExemptionsRequest.

        :param device_information: The device_information of this AuthenticationExemptionsRequest.
        :type: Riskv1authenticationexemptionsDeviceInformation
        """

        self._device_information = device_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this AuthenticationExemptionsRequest.

        :return: The merchant_information of this AuthenticationExemptionsRequest.
        :rtype: Riskv1authenticationexemptionsMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this AuthenticationExemptionsRequest.

        :param merchant_information: The merchant_information of this AuthenticationExemptionsRequest.
        :type: Riskv1authenticationexemptionsMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def acquirer_information(self):
        """
        Gets the acquirer_information of this AuthenticationExemptionsRequest.

        :return: The acquirer_information of this AuthenticationExemptionsRequest.
        :rtype: Riskv1authenticationexemptionsAcquirerInformation
        """
        return self._acquirer_information

    @acquirer_information.setter
    def acquirer_information(self, acquirer_information):
        """
        Sets the acquirer_information of this AuthenticationExemptionsRequest.

        :param acquirer_information: The acquirer_information of this AuthenticationExemptionsRequest.
        :type: Riskv1authenticationexemptionsAcquirerInformation
        """

        self._acquirer_information = acquirer_information

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
        if not isinstance(other, AuthenticationExemptionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
