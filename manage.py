#!/usr/bin/env python

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
