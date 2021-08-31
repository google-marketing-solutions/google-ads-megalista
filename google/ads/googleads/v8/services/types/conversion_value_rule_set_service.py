# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.ads.googleads.v8.enums.types import (
    response_content_type as gage_response_content_type,
)
from google.ads.googleads.v8.resources.types import (
    conversion_value_rule_set as gagr_conversion_value_rule_set,
)
from google.protobuf import field_mask_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v8.services",
    marshal="google.ads.googleads.v8",
    manifest={
        "GetConversionValueRuleSetRequest",
        "MutateConversionValueRuleSetsRequest",
        "ConversionValueRuleSetOperation",
        "MutateConversionValueRuleSetsResponse",
        "MutateConversionValueRuleSetResult",
    },
)


class GetConversionValueRuleSetRequest(proto.Message):
    r"""Request message for
    [ConversionValueRuleSetService.GetConversionValueRuleSet][google.ads.googleads.v8.services.ConversionValueRuleSetService.GetConversionValueRuleSet].

    Attributes:
        resource_name (str):
            Required. The resource name of the conversion
            value rule set to fetch.
    """

    resource_name = proto.Field(proto.STRING, number=1,)


class MutateConversionValueRuleSetsRequest(proto.Message):
    r"""Request message for
    [ConversionValueRuleSetService.MutateConversionValueRuleSets][google.ads.googleads.v8.services.ConversionValueRuleSetService.MutateConversionValueRuleSets].

    Attributes:
        customer_id (str):
            Required. The ID of the customer whose
            conversion value rule sets are being modified.
        operations (Sequence[google.ads.googleads.v8.services.types.ConversionValueRuleSetOperation]):
            Required. The list of operations to perform
            on individual conversion value rule sets.
        partial_failure (bool):
            If true, successful operations will be
            carried out and invalid operations will return
            errors. If false, all operations will be carried
            out in one transaction if and only if they are
            all valid. Default is false.
        validate_only (bool):
            If true, the request is validated but not
            executed. Only errors are returned, not results.
        response_content_type (google.ads.googleads.v8.enums.types.ResponseContentTypeEnum.ResponseContentType):
            The response content type setting. Determines
            whether the mutable resource or just the
            resource name should be returned post mutation.
    """

    customer_id = proto.Field(proto.STRING, number=1,)
    operations = proto.RepeatedField(
        proto.MESSAGE, number=2, message="ConversionValueRuleSetOperation",
    )
    partial_failure = proto.Field(proto.BOOL, number=5,)
    validate_only = proto.Field(proto.BOOL, number=3,)
    response_content_type = proto.Field(
        proto.ENUM,
        number=4,
        enum=gage_response_content_type.ResponseContentTypeEnum.ResponseContentType,
    )


class ConversionValueRuleSetOperation(proto.Message):
    r"""A single operation (create, update, remove) on a conversion
    value rule set.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
        create (google.ads.googleads.v8.resources.types.ConversionValueRuleSet):
            Create operation: No resource name is
            expected for the new conversion value rule set.
        update (google.ads.googleads.v8.resources.types.ConversionValueRuleSet):
            Update operation: The conversion action is
            expected to have a valid resource name.
        remove (str):
            Remove operation: A resource name for the removed conversion
            action is expected, in this format:

            ``customers/{customer_id}/conversionValueRuleSets/{conversion_value_rule_set_id}``
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=4, message=field_mask_pb2.FieldMask,
    )
    create = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=gagr_conversion_value_rule_set.ConversionValueRuleSet,
    )
    update = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="operation",
        message=gagr_conversion_value_rule_set.ConversionValueRuleSet,
    )
    remove = proto.Field(proto.STRING, number=3, oneof="operation",)


class MutateConversionValueRuleSetsResponse(proto.Message):
    r"""Response message for
    [ConversionValueRuleSetService.MutateConversionValueRuleSets][google.ads.googleads.v8.services.ConversionValueRuleSetService.MutateConversionValueRuleSets].

    Attributes:
        results (Sequence[google.ads.googleads.v8.services.types.MutateConversionValueRuleSetResult]):
            All results for the mutate.
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (e.g. auth errors), we return an RPC
            level error.
    """

    results = proto.RepeatedField(
        proto.MESSAGE, number=1, message="MutateConversionValueRuleSetResult",
    )
    partial_failure_error = proto.Field(
        proto.MESSAGE, number=2, message=status_pb2.Status,
    )


class MutateConversionValueRuleSetResult(proto.Message):
    r"""The result for the conversion value rule set mutate.
    Attributes:
        resource_name (str):
            Returned for successful operations.
        conversion_value_rule_set (google.ads.googleads.v8.resources.types.ConversionValueRuleSet):
            The mutated conversion value rule set with only mutable
            fields after mutate. The field will only be returned when
            response_content_type is set to "MUTABLE_RESOURCE".
    """

    resource_name = proto.Field(proto.STRING, number=1,)
    conversion_value_rule_set = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gagr_conversion_value_rule_set.ConversionValueRuleSet,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
