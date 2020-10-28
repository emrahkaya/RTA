# Name: Common Enumeration Commands
# RTA: enum_commands_T1049.py
# ATT&CK: T1049
# Description: Executes a list of administration tools commonly used by attackers for enumeration.

import argparse
import common
import random


long_commands = [

]

commands = [
    "net use",
    "net session",
    "netstat -nao",
    "netsh wlan show networks mode = bssid",
    "netsh wlan show interfaces",
    "net file",
    "arp -a",
    "net view"
] + long_commands


def main(args=None):
    common.log_important("STARTING TECHNIQUE")

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sample', dest="sample", default=len(commands), type=int,
                        help="Number of commands to run, choosen at random from the list of enumeration commands")
    args = parser.parse_args(args)
    sample = min(len(commands), args.sample)

    if sample < len(commands):
        random.shuffle(commands)

    common.log("Running {} out of {} enumeration commands\n". format(sample, len(commands)))
    for command in commands[0:sample]:
        common.log("About to call {}".format(command))
        if command in long_commands:
            common.execute(command, kill=True, timeout=15)
            common.log("[output surpressed]", log_type='-')
        else:
            common.execute(command)

if __name__ == "__main__":
    exit(main())
