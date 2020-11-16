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


CREATE_ROUTE_RESPONSE = """
<CreateRouteResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</CreateRouteResponse>
"""

REPLACE_ROUTE_RESPONSE = """
<ReplaceRouteResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</ReplaceRouteResponse>
"""

CREATE_ROUTE_TABLE_RESPONSE = """
<CreateRouteTableResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <routeTable>
      <routeTableId>{{ route_table.id }}</routeTableId>
      <vpcId>{{ route_table.vpc_id }}</vpcId>
      <routeSet>
         {% for route in route_table.routes.values() %}
           {% if route.local %}
           <item>
             <destinationCidrBlock>{{ route.destination_cidr_block }}</destinationCidrBlock>
             <gatewayId>local</gatewayId>
             <state>active</state>
           </item>
           {% endif %}
         {% endfor %}
      </routeSet>
      <associationSet/>
      <tagSet>
      {% for tag in route_table.get_tags() %}
        <item>
          <resourceId>{{ tag.resource_id }}</resourceId>
          <resourceType>{{ tag.resource_type }}</resourceType>
          <key>{{ tag.key }}</key>
          <value>{{ tag.value }}</value>
        </item>
      {% endfor %}
      </tagSet>
   </routeTable>
</CreateRouteTableResponse>
"""

DESCRIBE_ROUTE_TABLES_RESPONSE = """
<DescribeRouteTablesResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>6f570b0b-9c18-4b07-bdec-73740dcf861a</requestId>
   <routeTableSet>
     {% for route_table in route_tables %}
       <item>
          <routeTableId>{{ route_table.id }}</routeTableId>
          <vpcId>{{ route_table.vpc_id }}</vpcId>
          <routeSet>
            {% for route in route_table.routes.values() %}
              <item>
                <destinationCidrBlock>{{ route.destination_cidr_block }}</destinationCidrBlock>
                {% if route.local %}
                  <gatewayId>local</gatewayId>
                  <origin>CreateRouteTable</origin>
                  <state>active</state>
                {% endif %}
                {% if route.gateway %}
                  <gatewayId>{{ route.gateway.id }}</gatewayId>
                  <origin>CreateRoute</origin>
                  <state>active</state>
                {% endif %}
                {% if route.instance %}
                  <instanceId>{{ route.instance.id }}</instanceId>
                  <origin>CreateRoute</origin>
                  <state>active</state>
                {% endif %}
                {% if route.vpc_pcx %}
                  <vpcPeeringConnectionId>{{ route.vpc_pcx.id }}</vpcPeeringConnectionId>
                  <origin>CreateRoute</origin>
                  <state>blackhole</state>
                {% endif %}
                {% if route.nat_gateway %}
                  <natGatewayId>{{ route.nat_gateway.id }}</natGatewayId>
                  <state>active</state>
                {% endif %}
              </item>
            {% endfor %}
          </routeSet>
          <associationSet>
            {% for association_id,subnet_id in route_table.associations.items() %}
              <item>
                <routeTableAssociationId>{{ association_id }}</routeTableAssociationId>
                <routeTableId>{{ route_table.id }}</routeTableId>
                <main>false</main>
                <subnetId>{{ subnet_id }}</subnetId>
              </item>
            {% endfor %}
          </associationSet>
         <tagSet>
          {% for tag in route_table.get_tags() %}
           <item>
             <resourceId>{{ tag.resource_id }}</resourceId>
             <resourceType>{{ tag.resource_type }}</resourceType>
             <key>{{ tag.key }}</key>
             <value>{{ tag.value }}</value>
           </item>
          {% endfor %}
         </tagSet>
       </item>
     {% endfor %}
   </routeTableSet>
</DescribeRouteTablesResponse>
"""

DELETE_ROUTE_RESPONSE = """
<DeleteRouteResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</DeleteRouteResponse>
"""

DELETE_ROUTE_TABLE_RESPONSE = """
<DeleteRouteTableResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</DeleteRouteTableResponse>
"""

ASSOCIATE_ROUTE_TABLE_RESPONSE = """
<AssociateRouteTableResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <associationId>{{ association_id }}</associationId>
</AssociateRouteTableResponse>
"""

DISASSOCIATE_ROUTE_TABLE_RESPONSE = """
<DisassociateRouteTableResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</DisassociateRouteTableResponse>
"""

REPLACE_ROUTE_TABLE_ASSOCIATION_RESPONSE = """
<ReplaceRouteTableAssociationResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <newAssociationId>{{ association_id }}</newAssociationId>
</ReplaceRouteTableAssociationResponse>
"""
