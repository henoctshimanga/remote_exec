from fabric.api import *

def greetings(msg):
    print(f"Good {msg}")

def system_info():
    print("Disk Space.")
    local("df -h")
    print("########################################")
    print()

    print("Memory Info.")
    local("free -m")
    print("########################################")
    print()

    print("System Uptime.")
    local("uptime")
    print("########################################")
    print()

def remote_exec():
    run("hostname")
    run("df -h")
    run("free -m")
    run("uptime")

    sudo("yum install unzip zip wget -y")

def web_server_setup(WEBURL, DIRNAME):
    print("####################################################")
    print("Installing Dependencies")
    print("####################################################")
    print()
    sudo("yum install httpd unzip wget -y")
    print()

    print("####################################################")
    print("Start & Enable Service")
    print("####################################################")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    print()

    print("####################################################")
    local("apt install zip unzip -y")

    print("####################################################")
    print("Downloading and pushing artifact to webserver.")
    print("####################################################")  
    local(("wget -O website.zip %s") % WEBURL)
    local("unzip -O website.zip")

    print("####################################################")
    with lcd(DIRNAME):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html/", use_sudo=True)
        
    with cd("/var/www/html/"):
        sudo("unzip -o tooplate.zip")


    print("####################################################")
    sudo("systemctl restart httpd")

    print("####################################################")
    print("Web_server setup is done.")