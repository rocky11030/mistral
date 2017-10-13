"""
CheckNovaCOmputeAction: - custom action.

This action for filtering compute node which nova-compute service
is stop.
"""
from mistral.actions.openstack.actions import NovaAction
from mistral.workflow.utils import Result

class CheckNovaComputeException(Exception):
    pass

class CheckNovaComputeAction(NovaAction):
    """
    """
    
    def run(self):
        """Entry point for the action execution."""
        client = self._get_client()
        hosts_list = []

        def is_nova_compute_down(service):
            return (service.state == 'down') and \
                   (service.binary == 'nova-compute')

        try:
            hosts = filter(
                is_nova_compute_down,
                client.services.list()
            )

            if hosts:
                for i in hosts:
                    hosts_list.append(i.host)

        except Exception as e:
            raise CheckNovaComputeException("Failed to get services list" + ":   " + e)
        
        return Result(data = {'host_list':hosts_list})

