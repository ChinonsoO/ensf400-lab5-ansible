import ansible_runner
import requests

def run_playbook():
    # directory of our invenory file
    inventory_dir = '.'

    # Run the Ansible playbook
    response = ansible_runner.run(
        private_data_dir=inventory_dir,
        playbook='hello.yml',  # playbook file
        inventory='hosts.yml',  # inventory file
        # below command if you need admin
        #become=True,
    )

    # Check response, print results
    if response.status == 'successful':
        print("Playbook execution: SUCCESS")
        print(response.stdout.read())

        # Verify the response of NodeJS servers
        for host, port in [('0.0.0.0', 3000), ('0.0.0.0', 3001), ('0.0.0.0', 3002)]:
            try:
                url = f"http://{host}:{port}"
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"{host}:{port}: NodeJS server is running")
                    print("Page content:")
                    print(response.text)
                    print("\n")
                else:
                    print(f"{host}:{port}: NodeJS server is not responding")
            except requests.exceptions.RequestException as e:
                print(f"{host}:{port}: Error connecting to NodeJS server - {e}")
    else:
        print("Playbook execution: FAILED")
        print(response.stdout.read())

if __name__ == "__main__":
    run_playbook()