# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.dynamodb import (
    attribute_type_validator,
    billing_mode_validator,
    key_type_validator,
    projection_type_validator,
    table_class_validator,
    validate_table,
)


class AttributeDefinition(AWSProperty):
    """
    `AttributeDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-attributedefinition.html>`__
    """

    props: PropsDictType = {
        "AttributeName": (str, True),
        "AttributeType": (attribute_type_validator, True),
    }


class KeySchema(AWSProperty):
    """
    `KeySchema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-keyschema.html>`__
    """

    props: PropsDictType = {
        "AttributeName": (str, True),
        "KeyType": (key_type_validator, True),
    }


class Projection(AWSProperty):
    """
    `Projection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-projection.html>`__
    """

    props: PropsDictType = {
        "NonKeyAttributes": ([str], False),
        "ProjectionType": (projection_type_validator, False),
    }


class TargetTrackingScalingPolicyConfiguration(AWSProperty):
    """
    `TargetTrackingScalingPolicyConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html>`__
    """

    props: PropsDictType = {
        "DisableScaleIn": (boolean, False),
        "ScaleInCooldown": (integer, False),
        "ScaleOutCooldown": (integer, False),
        "TargetValue": (double, True),
    }


class CapacityAutoScalingSettings(AWSProperty):
    """
    `CapacityAutoScalingSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html>`__
    """

    props: PropsDictType = {
        "MaxCapacity": (integer, True),
        "MinCapacity": (integer, True),
        "SeedCapacity": (integer, False),
        "TargetTrackingScalingPolicyConfiguration": (
            TargetTrackingScalingPolicyConfiguration,
            True,
        ),
    }


class WriteProvisionedThroughputSettings(AWSProperty):
    """
    `WriteProvisionedThroughputSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html>`__
    """

    props: PropsDictType = {
        "WriteCapacityAutoScalingSettings": (CapacityAutoScalingSettings, False),
    }


class GlobalTableGlobalSecondaryIndex(AWSProperty):
    """
    `GlobalTableGlobalSecondaryIndex <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html>`__
    """

    props: PropsDictType = {
        "IndexName": (str, True),
        "KeySchema": ([KeySchema], True),
        "Projection": (Projection, True),
        "WriteProvisionedThroughputSettings": (
            WriteProvisionedThroughputSettings,
            False,
        ),
    }


class GlobalTableSSESpecification(AWSProperty):
    """
    `GlobalTableSSESpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html>`__
    """

    props: PropsDictType = {
        "SSEEnabled": (boolean, True),
        "SSEType": (str, False),
    }


class LocalSecondaryIndex(AWSProperty):
    """
    `LocalSecondaryIndex <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-localsecondaryindex.html>`__
    """

    props: PropsDictType = {
        "IndexName": (str, True),
        "KeySchema": ([KeySchema], True),
        "Projection": (Projection, True),
    }


class ContributorInsightsSpecification(AWSProperty):
    """
    `ContributorInsightsSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-contributorinsightsspecification.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class KinesisStreamSpecification(AWSProperty):
    """
    `KinesisStreamSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-kinesisstreamspecification.html>`__
    """

    props: PropsDictType = {
        "ApproximateCreationDateTimePrecision": (str, False),
        "StreamArn": (str, True),
    }


class PointInTimeRecoverySpecification(AWSProperty):
    """
    `PointInTimeRecoverySpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html>`__
    """

    props: PropsDictType = {
        "PointInTimeRecoveryEnabled": (boolean, False),
    }


class ReadProvisionedThroughputSettings(AWSProperty):
    """
    `ReadProvisionedThroughputSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html>`__
    """

    props: PropsDictType = {
        "ReadCapacityAutoScalingSettings": (CapacityAutoScalingSettings, False),
        "ReadCapacityUnits": (integer, False),
    }


class ReplicaGlobalSecondaryIndexSpecification(AWSProperty):
    """
    `ReplicaGlobalSecondaryIndexSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html>`__
    """

    props: PropsDictType = {
        "ContributorInsightsSpecification": (ContributorInsightsSpecification, False),
        "IndexName": (str, True),
        "ReadProvisionedThroughputSettings": (ReadProvisionedThroughputSettings, False),
    }


class ReplicaSSESpecification(AWSProperty):
    """
    `ReplicaSSESpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html>`__
    """

    props: PropsDictType = {
        "KMSMasterKeyId": (str, True),
    }


class ResourcePolicy(AWSProperty):
    """
    `ResourcePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-resourcepolicy.html>`__
    """

    props: PropsDictType = {
        "PolicyDocument": (dict, True),
    }


class ReplicaStreamSpecification(AWSProperty):
    """
    `ReplicaStreamSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicastreamspecification.html>`__
    """

    props: PropsDictType = {
        "ResourcePolicy": (ResourcePolicy, True),
    }


class ReplicaSpecification(AWSProperty):
    """
    `ReplicaSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html>`__
    """

    props: PropsDictType = {
        "ContributorInsightsSpecification": (ContributorInsightsSpecification, False),
        "DeletionProtectionEnabled": (boolean, False),
        "GlobalSecondaryIndexes": ([ReplicaGlobalSecondaryIndexSpecification], False),
        "KinesisStreamSpecification": (KinesisStreamSpecification, False),
        "PointInTimeRecoverySpecification": (PointInTimeRecoverySpecification, False),
        "ReadProvisionedThroughputSettings": (ReadProvisionedThroughputSettings, False),
        "Region": (str, True),
        "ReplicaStreamSpecification": (ReplicaStreamSpecification, False),
        "ResourcePolicy": (ResourcePolicy, False),
        "SSESpecification": (ReplicaSSESpecification, False),
        "TableClass": (str, False),
        "Tags": (Tags, False),
    }


class StreamSpecification(AWSProperty):
    """
    `StreamSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-streamspecification.html>`__
    """

    props: PropsDictType = {
        "ResourcePolicy": (ResourcePolicy, False),
        "StreamViewType": (str, True),
    }


class TimeToLiveSpecification(AWSProperty):
    """
    `TimeToLiveSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-timetolivespecification.html>`__
    """

    props: PropsDictType = {
        "AttributeName": (str, False),
        "Enabled": (boolean, True),
    }


class GlobalTable(AWSObject):
    """
    `GlobalTable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html>`__
    """

    resource_type = "AWS::DynamoDB::GlobalTable"

    props: PropsDictType = {
        "AttributeDefinitions": ([AttributeDefinition], True),
        "BillingMode": (str, False),
        "GlobalSecondaryIndexes": ([GlobalTableGlobalSecondaryIndex], False),
        "KeySchema": ([KeySchema], True),
        "LocalSecondaryIndexes": ([LocalSecondaryIndex], False),
        "Replicas": ([ReplicaSpecification], True),
        "SSESpecification": (GlobalTableSSESpecification, False),
        "StreamSpecification": (StreamSpecification, False),
        "TableName": (str, False),
        "TimeToLiveSpecification": (TimeToLiveSpecification, False),
        "WriteProvisionedThroughputSettings": (
            WriteProvisionedThroughputSettings,
            False,
        ),
    }


class ProvisionedThroughput(AWSProperty):
    """
    `ProvisionedThroughput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-provisionedthroughput.html>`__
    """

    props: PropsDictType = {
        "ReadCapacityUnits": (integer, True),
        "WriteCapacityUnits": (integer, True),
    }


class GlobalSecondaryIndex(AWSProperty):
    """
    `GlobalSecondaryIndex <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-globalsecondaryindex.html>`__
    """

    props: PropsDictType = {
        "ContributorInsightsSpecification": (ContributorInsightsSpecification, False),
        "IndexName": (str, True),
        "KeySchema": ([KeySchema], True),
        "Projection": (Projection, True),
        "ProvisionedThroughput": (ProvisionedThroughput, False),
    }


class Csv(AWSProperty):
    """
    `Csv <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-csv.html>`__
    """

    props: PropsDictType = {
        "Delimiter": (str, False),
        "HeaderList": ([str], False),
    }


class InputFormatOptions(AWSProperty):
    """
    `InputFormatOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-inputformatoptions.html>`__
    """

    props: PropsDictType = {
        "Csv": (Csv, False),
    }


class S3BucketSource(AWSProperty):
    """
    `S3BucketSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-s3bucketsource.html>`__
    """

    props: PropsDictType = {
        "S3Bucket": (str, True),
        "S3BucketOwner": (str, False),
        "S3KeyPrefix": (str, False),
    }


class ImportSourceSpecification(AWSProperty):
    """
    `ImportSourceSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-importsourcespecification.html>`__
    """

    props: PropsDictType = {
        "InputCompressionType": (str, False),
        "InputFormat": (str, True),
        "InputFormatOptions": (InputFormatOptions, False),
        "S3BucketSource": (S3BucketSource, True),
    }


class SSESpecification(AWSProperty):
    """
    `SSESpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html>`__
    """

    props: PropsDictType = {
        "KMSMasterKeyId": (str, False),
        "SSEEnabled": (boolean, True),
        "SSEType": (str, False),
    }


class Table(AWSObject):
    """
    `Table <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html>`__
    """

    resource_type = "AWS::DynamoDB::Table"

    props: PropsDictType = {
        "AttributeDefinitions": ([AttributeDefinition], False),
        "BillingMode": (billing_mode_validator, False),
        "ContributorInsightsSpecification": (ContributorInsightsSpecification, False),
        "DeletionProtectionEnabled": (boolean, False),
        "GlobalSecondaryIndexes": ([GlobalSecondaryIndex], False),
        "ImportSourceSpecification": (ImportSourceSpecification, False),
        "KeySchema": ([KeySchema], True),
        "KinesisStreamSpecification": (KinesisStreamSpecification, False),
        "LocalSecondaryIndexes": ([LocalSecondaryIndex], False),
        "PointInTimeRecoverySpecification": (PointInTimeRecoverySpecification, False),
        "ProvisionedThroughput": (ProvisionedThroughput, False),
        "ResourcePolicy": (ResourcePolicy, False),
        "SSESpecification": (SSESpecification, False),
        "StreamSpecification": (StreamSpecification, False),
        "TableClass": (table_class_validator, False),
        "TableName": (str, False),
        "Tags": (Tags, False),
        "TimeToLiveSpecification": (TimeToLiveSpecification, False),
    }

    def validate(self):
        validate_table(self)
