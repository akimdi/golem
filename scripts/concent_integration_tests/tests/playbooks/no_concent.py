from scripts.concent_integration_tests.tests.playbooks.base import NodeTestPlaybook


class NoConcent(NodeTestPlaybook):
    provider_node_script = 'provider/no_concent'
    requestor_node_script = 'requestor/no_concent'
