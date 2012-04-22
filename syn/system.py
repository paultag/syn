# Copyright

from contextlib import contextmanager
import subprocess
import os.path
import shutil
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


def mkdir(folder, destroy_old=False):
    try:
        os.mkdir(folder)
    except OSError as e:
        if e.errno == 17:
            rmdir(folder)
            return mkdir(folder, destroy_old=False)


def rmdir(path):
    shutil.rmtree(path)

def abspath(folder):
    return os.path.abspath(folder)


def putenv(key, value):
    os.environ[key] = value
