# Copyright

from contextlib import contextmanager
import subprocess
import os.path
import os

@contextmanager
def cd(path):
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)


def run(command):
    return subprocess.check_call(command)


def mkdir(folder):
    os.mkdir(folder)


def abspath(folder):
    return os.path.abspath(folder)


def putenv(key, value):
    os.environ[key] = value
