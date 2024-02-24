# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType


class CognitoUserPoolConfiguration(AWSProperty):
    """
    `CognitoUserPoolConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration.html>`__
    """

    props: PropsDictType = {
        "ClientIds": ([str], False),
        "UserPoolArn": (str, True),
    }


class IdentitySourceConfiguration(AWSProperty):
    """
    `IdentitySourceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration.html>`__
    """

    props: PropsDictType = {
        "CognitoUserPoolConfiguration": (CognitoUserPoolConfiguration, True),
    }


class IdentitySource(AWSObject):
    """
    `IdentitySource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html>`__
    """

    resource_type = "AWS::VerifiedPermissions::IdentitySource"

    props: PropsDictType = {
        "Configuration": (IdentitySourceConfiguration, True),
        "PolicyStoreId": (str, True),
        "PrincipalEntityType": (str, False),
    }


class StaticPolicyDefinition(AWSProperty):
    """
    `StaticPolicyDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-staticpolicydefinition.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "Statement": (str, True),
    }


class EntityIdentifier(AWSProperty):
    """
    `EntityIdentifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-entityidentifier.html>`__
    """

    props: PropsDictType = {
        "EntityId": (str, True),
        "EntityType": (str, True),
    }


class TemplateLinkedPolicyDefinition(AWSProperty):
    """
    `TemplateLinkedPolicyDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html>`__
    """

    props: PropsDictType = {
        "PolicyTemplateId": (str, True),
        "Principal": (EntityIdentifier, False),
        "Resource": (EntityIdentifier, False),
    }


class PolicyDefinition(AWSProperty):
    """
    `PolicyDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-policydefinition.html>`__
    """

    props: PropsDictType = {
        "Static": (StaticPolicyDefinition, False),
        "TemplateLinked": (TemplateLinkedPolicyDefinition, False),
    }


class Policy(AWSObject):
    """
    `Policy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.html>`__
    """

    resource_type = "AWS::VerifiedPermissions::Policy"

    props: PropsDictType = {
        "Definition": (PolicyDefinition, True),
        "PolicyStoreId": (str, True),
    }


class SchemaDefinition(AWSProperty):
    """
    `SchemaDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-schemadefinition.html>`__
    """

    props: PropsDictType = {
        "CedarJson": (str, False),
    }


class ValidationSettings(AWSProperty):
    """
    `ValidationSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-validationsettings.html>`__
    """

    props: PropsDictType = {
        "Mode": (str, True),
    }


class PolicyStore(AWSObject):
    """
    `PolicyStore <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.html>`__
    """

    resource_type = "AWS::VerifiedPermissions::PolicyStore"

    props: PropsDictType = {
        "Description": (str, False),
        "Schema": (SchemaDefinition, False),
        "ValidationSettings": (ValidationSettings, True),
    }


class PolicyTemplate(AWSObject):
    """
    `PolicyTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html>`__
    """

    resource_type = "AWS::VerifiedPermissions::PolicyTemplate"

    props: PropsDictType = {
        "Description": (str, False),
        "PolicyStoreId": (str, True),
        "Statement": (str, True),
    }


class IdentitySourceDetails(AWSProperty):
    """
    `IdentitySourceDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html>`__
    """

    props: PropsDictType = {
        "ClientIds": ([str], False),
        "DiscoveryUrl": (str, False),
        "OpenIdIssuer": (str, False),
        "UserPoolArn": (str, False),
    }
