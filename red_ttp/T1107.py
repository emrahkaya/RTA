# Name: USN Journal Deletion with fsutil.exe
# RTA: delete_usnjrnl.py + delete_catalogs.py
# ATT&CK: T1107
# Description: Uses fsutil to delete the USN journal.

import common
import time

def main():
    message = "Deleting the USN journal may have unintended consequences"
    common.log("WARNING: %s" % message, log_type="!")
    common.execute(["fsutil", "usn", "deletejournal", "/d", "C:"])
    time.sleep(5)

    warning = "Deleting the backup catalog may have unexpected consequences. Operational issues are unknown."
    common.log("WARNING: %s" % warning, log_type="!")
    time.sleep(5)

    common.execute(["wbadmin", "delete", "catalog", "-quiet"])

if __name__ == "__main__":
    exit(main())
