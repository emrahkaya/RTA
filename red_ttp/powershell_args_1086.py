# Name: Powershell with Suspicious Arguments
# RTA: powershell_args.py
# ATT&CK: T1086 (PowerShell)
# Description: Calls PowerShell with suspicious command line arguments.

import os
import common
import base64


def main():
    common.log("PowerShell Suspicious Commands")
    temp_script = os.path.abspath("tmp.ps1")

    # Create an empty script     
    with open(temp_script, "wb") as f:
        f.write("whoami.exe\n")

    powershell_commands = [
        'powershell.exe -ExecutionPol Bypass %s' % temp_script,
        'powershell.exe iex Get-Process',
    ]

    for command in powershell_commands:
        common.execute(command)

    common.remove_file(temp_script)


if __name__ == "__main__":
    exit(main())
