"""
CheckNeutronAgentAction - custom action.

This action will filtering compute host which neutron-openvswitch-agent
service is stop. The input host list is from CheckNovaComputeAction,
finally this action will return host with ovs agent and compute service
stop status.
"""
from mistral.actions.openstack.actions import NeutronAction
from mistral.workflow.utils import Result

class CheckNeutronAgentException(Exception):
    pass

class CheckNeutronAgentAction(NeutronAction):
    """
    """
    
    def run(self):
        """Entry point for the action execution."""
        client = self._get_client()
        hosts_list = []

        def is_ovs_agent_down(agent):
            return (agent['binary'] == 'neutron-openvswitch-agent') and \
                   not agent['alive']

        try:
            hosts = filter(
                is_ovs_agent_down,
                client.list_agents()['agents']
            )

            if hosts:
                for i in hosts:
                    hosts_list.append(i['host'])

        except Exception as e:
            raise CheckNeutronAgentException("Failed to get services list" + ":   " + e)
        
        return Result(data={'host_list': hosts_list})
