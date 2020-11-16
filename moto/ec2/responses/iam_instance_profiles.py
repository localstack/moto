from __future__ import unicode_literals
from moto.core.responses import BaseResponse
from moto.ec2.utils import filters_from_querystring


class IamInstanceProfiles(BaseResponse):
    def associate_iam_instance_profile(self):
        instance_id = self._get_param("InstanceId")
        iam_instance_profile_name = self._get_param("IamInstanceProfile.Name")
        iam_instance_profile_arn = self._get_param("IamInstanceProfile.Arn")
        iam_association = self.ec2_backend.associate_iam_instance_profile(
            instance_id, iam_instance_profile_name, iam_instance_profile_arn
        )
        template = self.response_template(ASSOCIATE_IAM_INSTANCE_PROFILE_RESPONSE)
        return template.render(iam_association=iam_association)


ASSOCIATE_IAM_INSTANCE_PROFILE_RESPONSE = """
<AssociateIamInstanceProfileResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>e10deeaf-7cda-48e7-950b-example</requestId>
    <iamInstanceProfileAssociation>
        <associationId>{{ iam_association.id }}</associationId>
        <iamInstanceProfile>
            <arn>{{ iam_association.iam_instance_profile.arn }}</arn>
            <id>{{ iam_association.iam_instance_profile.id }}</id>
        </iamInstanceProfile>
        <instanceId>{{ iam_association.instance.id }}</instanceId>
        <state>{{ iam_association.state }}</state>
    </iamInstanceProfileAssociation>
</AssociateIamInstanceProfileResponse>
"""


DESCRIBE_IAM_INSTANCE_PROFILE_RESPONSE = """
<DescribeIamInstanceProfileAssociationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>84c2d2a6-12dc-491f-a9ee-example</requestId>
    <iamInstanceProfileAssociations>
         {% for iam_association in iam_associations %}
            <item>
                <associationId>{{ iam_association.id }}</associationId>
                <iamInstanceProfile>
                    <arn>{{ iam_association.iam_instance_profile.arn }}</arn>
                    <id>{{ iam_association.iam_instance_profile.id }}</id>
                </iamInstanceProfile>
                <instanceId>{{ iam_association.instance.id }}</instanceId>
                <state>{{ iam_association.state }}</state>
            </item>
        {% endfor %}
    </iamInstanceProfileAssociations>
</DescribeIamInstanceProfileAssociationsResponse>
"""
