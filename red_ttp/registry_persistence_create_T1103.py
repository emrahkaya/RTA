# Name: Registry persistence creation
# rta: registry_persistence_create_T1103.py
# ATT&CK: T1103
# Description: Creates registry persistence for mock malware in Run and RunOnce keys, Services and debuggers.

import _winreg as wreg
import time
import common

TARGET_APP = common.get_path("bin", "myapp.exe")


def pause():
    time.sleep(0.5)


def write_reg_string(hive, key, value, data, delete=True):
    hkey = wreg.CreateKey(hive, key)
    key = key.rstrip('\\')
    common.log("Writing to registry %s\\%s -> %s" % (key, value, data))
    wreg.SetValueEx(hkey, value, 0, wreg.REG_SZ, data)
    stored, code = wreg.QueryValueEx(hkey, value)
    if data != stored:
        common.log("Wrote %s but retrieved %s" % (data, stored), log_type="-")

    if delete:
        pause()
        common.log("Removing %s\\%s" % (key, value), log_type="-")
        wreg.DeleteValue(hkey, value)

    hkey.Close()
    pause()
    print("")


@common.dependencies(TARGET_APP)
def main():
    # Additional persistence
    hklm = wreg.HKEY_LOCAL_MACHINE
    common.log("Adding AppInit DLL")
    windows_base = "Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\"
    write_reg_string(hklm, windows_base, "AppInit_Dlls", "evil.dll", delete=False)
    write_reg_string(hklm, windows_base, "AppInit_Dlls", "", delete=False)

if __name__ == "__main__":
    exit(main())
