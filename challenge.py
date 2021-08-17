import boto3
import csv

ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')
network_acl = ec2.NetworkAcl('id')
security_group = ec2.SecurityGroup('id')
vpcs = ec2.Vpc('id')
route_table = ec2.RouteTable('id')
client = boto3.client('ec2')
Myec2 = client.describe_instances()
security_group_rules = client.describe_security_group_rules
response = client.describe_security_groups
valuefinal = 0

conn = boto3.resource('ec2')
instances = conn.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','stopped']}])
my_list = [instance for instance in instances]; len(my_list)
volumes = conn.volumes.filter()

my_list = [instance for instance in instances]; len(my_list)

for i, instance in enumerate(instances, start=1): pass
print(f"No momento há {i} Ec2 rodando")


for ec2info in Myec2['Reservations']:
    for ec2info1 in ec2info['Instances']:
        for securitygroup in ec2info1['SecurityGroups']:
            print(ec2info1['State']['Name'])

for instance in ec2.instances.all():
    print("\nInstância EC2 \n\nId: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\nVPC Id: {6}\nSubnet: {7}\nSecurity Group: {8}\nPublic DNS: {9}\nTags: {10}\nNetwork Interfaces: {11}"
        .format(instance.id, instance.platform, instance.instance_type, instance.public_ip_address, 
                instance.image.id, instance.state, instance.vpc_id, instance.subnet_id, instance.security_groups, 
                instance.public_dns_name, instance.tags, instance.network_interfaces))
    
    print("\nNaCL\n")

    for nacl in ec2.network_acls.all():
        print("Nacl Id: {0}\nTags: {1}\nEntries: {2}"
            .format(nacl.id, nacl.tags, nacl.entries))
        
    print("\nSecurity Group\n")

    for sg in ec2.security_groups.all():
        print("Security Group Id: {0}\nTags: {1}\nEntries: {2}"
            .format(sg.id, sg.tags, sg.ip_permissions))

    print("\nRoute Table\n")

    for rt in ec2.route_tables.all():
            print("Route Table Id: {0}\nTags: {1}"
                .format(rt.id, rt.tags))


for instance in ec2.instances.all():
    header = ['InstanceID', 'InstanceType', 'State', 'SG_ID','SG_Name','SG_Inbound/Outbound','Nacl_ID','RT_ID']
    data = [instance.id, instance.instance_type, ec2info1['State']['Name'], securitygroup['GroupId'], securitygroup['GroupName'],sg.ip_permissions, nacl.id,rt.id]

        #print(Myec2)

with open('ec2info.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)


output = {
                'InstanceID': instance.id,
                'InstanceType': instance.instance_type, 
                'State': ec2info1['State']['Name'], 
                'SG_ID': securitygroup['GroupId'], 
                'SG_Name': securitygroup['GroupName'], 
                'SG_Inbound/Outbound': sg.ip_permissions,
                'Nacl_ID': nacl.id,
                'RT_ID':  rt.id,
}



with open('ec2_list.csv', 'w', newline='') as csvfile:
                    header = ['InstanceID', 'InstanceType', 'State', 'SG_ID','SG_Name','SG_Inbound/Outbound','Nacl_ID','RT_ID']
                    writer = csv.DictWriter(csvfile, fieldnames=header)
                    writer.writeheader()
                    writer.writerow(output)
