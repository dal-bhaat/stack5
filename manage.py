#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line
try:
    import settings # Assumed to be in the same directory.
except ImportError, e:
    import traceback
    traceback.print_exc()
    import sys
    sys.stderr.write("Error: Can't find the file 'forms.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file forms.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings") #path to the settings py file
    execute_from_command_line(sys.argv)