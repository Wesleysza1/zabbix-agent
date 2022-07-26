import subprocess

system = str(subprocess.check_output("cat /etc/*-release | grep PRETTY", shell=True))
so = system.lower()
print(so)

if "ubuntu" in so:
    subprocess.call(["ansible-playbook", "ubuntu-agent.yaml"])
elif "debian" in so:
    subprocess.call(["ansible-playbook", "debian-agent.yaml"])
elif "redhat" in so: 
    subprocess.call(["ansible-playbook", "rhel-agent.yaml"])
elif "red hat" in so: 
    subprocess.call(["ansible-playbook", "rhel-agent.yaml"])
elif "centos" in so:
    subprocess.call(["ansible-playbook", "centos-agent.yaml"])
elif "suse" in so:
    subprocess.call(["ansible-playbook", "suse-agent.yaml"])
else:
    ("SO non supported")
