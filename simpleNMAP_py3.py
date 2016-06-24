#!/usr/bin/env python3

"""
    written by Slacker007 of www.cybersyndicates.com

    Simple python script written for the commandline challenged.  Quick and
    dirty.  And before you complain about whether or not it's suitable for a
    certain situation, ask yourself if the person performing the task SHOULD
    even need a script to get this info...
"""

import os
import subprocess
from collections import OrderedDict


def host_discovery():
    """Host Discovery"""

    target = input("[*] Please enter the network cidr"
                   " or IP address to be scanned: ")

    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n', '-v', '-Pn', '-sn', '-PE', '-PP', '-T4',
         '-ohostlist.UP', target])
    print('-' * 80)


def port_discovery_one():
    """Port & Service Discovery (top ports only)"""

    target = input("[*] Please enter the network cidr or "
                   " IP address to be scanned: ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n', '-v', '-Pn', '-sV', '-oservices2', target])
    print('-' * 80)


def port_discovery_two():
    """Port & Service Discovery (All 65536)"""

    target = input("[*] Please enter the network cidr or IP address to be"
                   " scanned: ")

    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n', '-v', '-Pn', '-sV', '-p 1-65535', '-oservices3',
         target])
    print('-' * 80)


def os_discovery():
    """OS Discovery"""

    target = input("[*] Please enter the network cidr "
                   "or IP address to be scanned: ")

    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n', '-v', '-Pn', '-O', '-oosversions', target])
    print('-' * 80)


def run_all():
    """Run All"""

    target = input("[*] Please enter the network cidr or "
                   " IP address to be scanned: ")

    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n', '-v', '-Pn', '-sn', '-PE', '-PP', '-T4',
         '-ohostlist.UP', target])
    subprocess.check_call(
        ['nmap', '-n', '-v', '-Pn', '-sV', '-p 1-65535', '-oservices3',
         target])
    subprocess.check_call(
        ['nmap', '-n', '-v', '-Pn', '-O', '-oosversions', target])
    print('-' * 80)


def quit_program():
    """Quit"""

    quit()


def clear():
    """Clear the screen"""

    os.system('cls' if os.name == 'nt' else 'clear')


def menu_loop():
    """Show menu"""

    choice = None

    while True:
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        try:
            choice = input('Action: ').lower().strip()

        except (TypeError, AttributeError, SyntaxError, NameError, EOFError):
            err_msg = "Invalid Entry. Please choose from the provided options."
            print('-' * len(err_msg))
            print(err_msg)
            print('-' * len(err_msg))
        except KeyboardInterrupt:
            print("Good Bye")
            # make it wait a few seconds before quitting
            quit()
        finally:
            clear()
            if choice in menu:
                menu[choice]()



menu = OrderedDict([
    ('h', host_discovery),
    ('o', port_discovery_one),
    ('t', port_discovery_two),
    ('s', os_discovery),
    ('a', run_all),
    ('q', quit_program)
])

if __name__ == '__main__':
    menu_loop()
