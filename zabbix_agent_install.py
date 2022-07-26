import subprocess

system = str(subprocess.check_output("cat /etc/*-release | grep PRETTY", shell=True))
so = system.lower()
print(so)

if "ubuntu" in so:
    subprocess.call(["ansible-playbook", "ubuntu-agent.yaml", "-K"])
elif "debian" in so:
    subprocess.call(["ansible-playbook", "debian-agent.yaml", "-K"])
elif "redhat" in so: 
    subprocess.call(["ansible-playbook", "rhel-agent.yaml", "-K"])
elif "red hat" in so: 
    subprocess.call(["ansible-playbook", "rhel-agent.yaml", "-K"])
elif "centos" in so:
    subprocess.call(["ansible-playbook", "centos-agent.yaml", "-K"])
elif "suse" in so:
    subprocess.call(["ansible-playbook", "suse-agent.yaml", "-K"])
else:
    ("SO non supported")
