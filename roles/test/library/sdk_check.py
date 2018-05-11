#!/usr/bin/python



from ansible.module_utils.basic import *

try:

    from algosec.api_client import FirewallAnalyzerAPIClient

    HAS_SDK = True

except ImportError:

    HAS_SDK = False

if not HAS_SDK:

    print 'This requires the Algosec SDK module, so no action will be taken'

    sys.exit(0)





def run_module():

    module_args = dict(

        ip=dict(type='str', required=True),

        username=dict(type='str', required=True),

        password=dict(type='str', required=True, no_log=True),

    )



    module = AnsibleModule(

        argument_spec=module_args

    )



    ip = module.params['ip']

    username = module.params['username']

    password = module.params['password']



    client = FirewallAnalyzerAPIClient(ip, username, password, verify_ssl=False)

    query_result = client.run_traffic_simulation_query(

        '0.0.0.0',

        '0.0.0.0',

        'http'

    )



    result = dict(

        changed=False,

        result=str(query_result)

    )

    module.exit_json(**result)





def main():

    run_module()





if __name__ == '__main__':

    main()
