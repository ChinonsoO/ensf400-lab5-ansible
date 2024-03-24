import ansible_runner

def ping_hosts():
    inventory_dir = '.'

    # Use the get_inventory function to fetch inventory details
    inventory_output, inventory_error = ansible_runner.get_inventory(
        action='list',
        inventories=[f'{inventory_dir}/hosts.yml'],
        response_format='json'
    )

    # Run the Ansible ping module
    response = ansible_runner.run(
        private_data_dir=inventory_dir,
        inventory=f'{inventory_dir}/hosts.yml',
        host_pattern='all',
        module='ping',
    )

    # Check the response and print results
    if response.status == 'successful':
        print("Ping Results: SUCCESS")
        for host in response.events:
            if host['event'] == 'runner_on_ok':
                host_name = host['event_data']['host']

                # Retrieve group and IP information from inventory_output
                host_group = next((g for g, details in inventory_output.items() if 'hosts' in details and host_name in details['hosts']), 'Unknown')
                ip_address = inventory_output.get('_meta', {}).get('hostvars', {}).get(host_name, {}).get('ansible_host', 'No IP found')
                
                # Check if the ping was successful before printing the host details
                if host['event_data']['res'].get('ping') == 'pong':
                    print(f"{host_name} (GROUP: {host_group}, IP: {ip_address}): {host['event_data']['res']}\n")
    else:
        print("Ping Results: FAILED")
        print(response.stdout.read())

if __name__ == "__main__":
    ping_hosts()