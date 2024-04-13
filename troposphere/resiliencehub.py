# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import integer
from .validators.resiliencehub import (
    validate_resiliencypolicy_policy,
    validate_resiliencypolicy_tier,
)


class EventSubscription(AWSProperty):
    """
    `EventSubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-eventsubscription.html>`__
    """

    props: PropsDictType = {
        "EventType": (str, True),
        "Name": (str, True),
        "SnsTopicArn": (str, False),
    }


class PermissionModel(AWSProperty):
    """
    `PermissionModel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-permissionmodel.html>`__
    """

    props: PropsDictType = {
        "CrossAccountRoleArns": ([str], False),
        "InvokerRoleName": (str, False),
        "Type": (str, True),
    }


class PhysicalResourceId(AWSProperty):
    """
    `PhysicalResourceId <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html>`__
    """

    props: PropsDictType = {
        "AwsAccountId": (str, False),
        "AwsRegion": (str, False),
        "Identifier": (str, True),
        "Type": (str, True),
    }


class ResourceMapping(AWSProperty):
    """
    `ResourceMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html>`__
    """

    props: PropsDictType = {
        "EksSourceName": (str, False),
        "LogicalStackName": (str, False),
        "MappingType": (str, True),
        "PhysicalResourceId": (PhysicalResourceId, True),
        "ResourceName": (str, False),
        "TerraformSourceName": (str, False),
    }


class App(AWSObject):
    """
    `App <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html>`__
    """

    resource_type = "AWS::ResilienceHub::App"

    props: PropsDictType = {
        "AppAssessmentSchedule": (str, False),
        "AppTemplateBody": (str, True),
        "Description": (str, False),
        "EventSubscriptions": ([EventSubscription], False),
        "Name": (str, True),
        "PermissionModel": (PermissionModel, False),
        "ResiliencyPolicyArn": (str, False),
        "ResourceMappings": ([ResourceMapping], True),
        "Tags": (dict, False),
    }


class FailurePolicy(AWSProperty):
    """
    `FailurePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html>`__
    """

    props: PropsDictType = {
        "RpoInSecs": (integer, True),
        "RtoInSecs": (integer, True),
    }


class PolicyMap(AWSProperty):
    """
    `PolicyMap <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-policymap.html>`__
    """

    props: PropsDictType = {
        "AZ": (FailurePolicy, True),
        "Hardware": (FailurePolicy, True),
        "Region": (FailurePolicy, False),
        "Software": (FailurePolicy, True),
    }


class ResiliencyPolicy(AWSObject):
    """
    `ResiliencyPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html>`__
    """

    resource_type = "AWS::ResilienceHub::ResiliencyPolicy"

    props: PropsDictType = {
        "DataLocationConstraint": (str, False),
        "Policy": (validate_resiliencypolicy_policy, True),
        "PolicyDescription": (str, False),
        "PolicyName": (str, True),
        "Tags": (dict, False),
        "Tier": (validate_resiliencypolicy_tier, True),
    }
