#!C:\Users\megha\Desktop\autum\autum1\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'keyring==10.3','console_scripts','keyring'
__requires__ = 'keyring==10.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('keyring==10.3', 'console_scripts', 'keyring')()
    )
