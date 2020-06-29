#! /opt/cfy/embedded/bin/python

from cloudify_cli.cli.cfy import pass_client
from cloudify_rest_client import CloudifyClient

@pass_client()

mySecret = client.secrets.get('my-secret')
print mySecret.value

