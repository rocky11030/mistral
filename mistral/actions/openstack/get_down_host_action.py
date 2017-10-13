"""
"""
from mistral.workflow.utils import Result
from mistral.actions import base

class GetDownHostException(Exception):
    pass

class GetDownHostAction(base.Action):
    """
    """
    def __init__(self, nova_down_list, neutron_down_list):
        """init."""
        self._nova_down_list = nova_down_list
        self._neutron_down_list = neutron_down_list

    def run(self):
        """Get the host in both nova_down_list and neutron_down_list"""
        host_list = [host for host in self._nova_down_list \
                     if host in self._neutron_down_list]

        return Result(data={'host': host_list})
