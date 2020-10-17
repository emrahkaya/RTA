# Name: Powershell with Suspicious Arguments
# RTA: powershell_args.py
# ATT&CK: T1140
# Description: Calls PowerShell with suspicious command line arguments.

import os
import common
import base64


def encode(command):
    return base64.b64encode(command.encode('utf-16le'))


def main():
    powershell_commands = [
        'powershell -encoded %s' % encode('ping google.com'),
        'powershell.exe -ec %s' % encode('Get-Process' + ' ' * 1000),
    ]

    for command in powershell_commands:
        common.execute(command)



if __name__ == "__main__":
    exit(main())
