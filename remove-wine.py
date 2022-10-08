#!/bin/python3

import os
import sys

USER = os.environ.get("SUDO_USER")
HOME = f'/home/{USER}'
RED = "\033[31m"


def remove_from_packages():
    try:
        os.system('apt-get purge wine-devel -y')
        os.system('apt-get purge wine-stable -y')
        os.system('apt-get purge wine-staging -y')
        os.system('apt-get purge wine -y')
        os.system('apt autoremove -y')
        os.system('apt-get update')
        os.system('apt-get upgrade -y')
    except:
        print(f"\n{RED} Failed on remove packages! \n")


def remove_files():
    try:
        os.system('rm -rf /opt/wine*')
        os.system('rm -rf /usr/bin/wine')
        os.system(f'rm -rf {HOME}/.cache/wine')
        os.system(f'rm -rf {HOME}/.local/share/applications/wine*')
        os.system(f'rm -rf {HOME}/.wine')
        os.system('rm -rf /usr/share/bash-completion/completions/wine')
        os.system('rm -rf /etc/apt/keyrings/winehq-archive.key')
        os.system('rm -rf /etc/apt/sources.list.d/wine*')

    except:
        print(f"\n{RED} Failed on remove files! \n")


def main():
    remove_from_packages()
    remove_files()


if __name__ == '__main__':
    user_type = os.getuid()

    if(user_type != 0):
        print(f"\n{RED} Please Run as Root! \n")
        sys.exit(1)

    main()
