# -*- coding: utf-8 -*-

#!/usr/bin/env python
import os
import sys

sys.path.append("./yolov5")     # module 로드할 때 굳이 yolov5 안 붙여도 되도록!


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'implantify.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
