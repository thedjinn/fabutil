from fabric.tasks import task
from fabric.contrib import files
from fabric.api import sudo

has_aptitude = False
has_updated = False

@task
def apt(cmd):
    global has_aptitude, has_updated
    if not has_aptitude:
        if not files.exists("/usr/bin/aptitude"):
            sudo("apt-get update")
            has_updated = True
            sudo("apt-get -y install aptitude")
        has_aptitude = True
    sudo("aptitude %s" % cmd)

@task
def update():
    global has_updated
    if not has_updated:
        apt("update")
        has_updated = True

@task
def upgrade():
    update()
    apt("-y safe-upgrade")

@task
def install(packages):
    update()
    apt("-y install %s" % packages)

@task
def create_deploy_user():
    run("adduser deploy")
    run("echo \"deploy ALL=(ALL) ALL\" >> /etc/sudoers")
    run("mkdir -p /home/deploy/.ssh")
    run("chown -R deploy:deploy /home/deploy/.ssh")
    run("chmod 700 /home/deploy/.ssh")
    print("Now don't forget to copy the public SSH key!")
