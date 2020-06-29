#! /opt/cfy/embedded/bin/python

import argparse
from cloudify_cli.cli.cfy import pass_client
from cloudify_rest_client import CloudifyClient

@pass_client()

def update(client, node_instance_id):
    ni = client.node_instances.get(node_instance_id)
    ni_rt = ni.runtime_properties
    ni_new_rt = ni_rt
    ni_new_rt['cloudify_agent']['broker_ip'] = '10.10.0.125'
    client.node_instances.update(
        node_instance_id,
        runtime_properties=ni_new_rt,
        version=ni.version)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--node-instance-id')
    args = parser.parse_args()
    update(node_instance_id=args.node_instance_id)
