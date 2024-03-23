import ansible_runner

def ping_hosts():
    # directory of our invenory file
    inventory_dir = '.'

    # Run the Ansible ping module directly on all hosts in the inventory
    response = ansible_runner.run(
        private_data_dir=inventory_dir,
        inventory='hosts.yml',  # Inventory file
        host_pattern='all',  # Targets all hosts
        module='ping',  # Uses the ping module
        # if you need admin prvileges uncomment below line
        #become=True,
    )

    # Check the response and print results
    if response.status == 'successful':
        print("Ping Results: SUCCESS")
        for host in response.events:
            if host['event'] == 'runner_on_ok':
                print(f"{host['event_data']['host']}: {host['event_data']['res']}\n")
    else:
        print("Ping Results: FAILED")
        print(response.stdout.read())

if __name__ == "__main__":
    ping_hosts()