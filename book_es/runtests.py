#!/usr/bin/env python
import os
import sys

import pytest


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.testing")
    sys.path.insert(0, "src")
    sys.path.insert(0, "/")
    return pytest.main()


if __name__ == '__main__':
    sys.exit(main())
