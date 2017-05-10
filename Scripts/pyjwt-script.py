#!C:\Users\megha\Desktop\autum\autum1\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyjwt==1.5.0','console_scripts','pyjwt'
__requires__ = 'pyjwt==1.5.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyjwt==1.5.0', 'console_scripts', 'pyjwt')()
    )
