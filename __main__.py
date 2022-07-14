import pulumi
import pulumi_gcp as gcp

default_network = gcp.compute.Network("vpc-name")
default_subnetwork = gcp.compute.Subnetwork("sub-name",
    ip_cidr_range="10.127.0.0/20",
    region="us-central1",
    network=default_network.id)
internal_with_subnet_and_address = gcp.compute.Address("name-of-ip",
    subnetwork=default_subnetwork.id,
    address_type="INTERNAL",
    address="10.127.0.3",
    region="us-central1")



