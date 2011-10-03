from fabric.tasks import task
from fabric.contrib import files
from fabric.api import sudo

# bundler related

@task
def gem_install(gem):
    run("gem install %s --no-ri --no-rdoc" % gem)

@task
def setup_bundler():
    gem_install("bundler")

@task
def bundle_install():
    run("bundle install")

@task
def bundle_exec(cmd):
    run("bundle exec %s" % cmd)

# rvm related

@task
def setup_rvm():
    run("bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)")
    run("echo '[[ -s \"$HOME/.rvm/scripts/rvm\" ]] && . \"$HOME/.rvm/scripts/rvm\" # Load RVM function' >> ~/.bash_profile")
    run("source ~/.bash_profile")
    run("type rvm")

@task
def setup_rvm_multi():
    run("sudo bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)")
    # TODO: add user to rvm group
    # TODO: relogin
    run("type rvm")

@task
def rvm(cmd):
    run("rvm %s" % cmd)

@task
def install_ruby_19():
    rvm("install 1.9.2")

@task
def install_ruby_18():
    rvm("install 1.8.7")

@task
def install_ree():
    rvm("install ree")
