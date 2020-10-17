# Name: Common Enumeration Commands
# RTA: enum_commands_T1069.py
# ATT&CK: T1069
# Description: Executes a list of administration tools commonly used by attackers for enumeration.

import argparse
import common
import random


long_commands = [
    "gpresult.exe /z"  # group policy view
]

commands = [
    "net localgroup administrators",
    "net localgroup",
    "net group",
    "net group \"Domain Admins\" /domain",
   "net accounts",
] + long_commands


def main(args=None):

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
