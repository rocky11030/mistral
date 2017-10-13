"""
"""
from mistral.actions.openstack.actions import NovaAction
from mistral.workflow.utils import Result

class ListVmsException(Exception):
    pass

class ListVmsAction(NovaAction):
    """
    """

    def __init__(self, host_list):
        self._host_list = host_list

    def run(self):
        """Entry point for the action execution."""
        client = self._get_client()
        vms = []

        try:
            for host in self._host_list:
                vms.extend(client.servers.list(search_opts={'host':host, 'all_tenants': 1}))
        except Exception as e:
            raise ListVmsException("Failed to list servers:  " + e)

        return Result(data = {'vms': vms})
