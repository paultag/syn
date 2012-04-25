# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

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


tmp_inc = 0
def mktmp():
    global tmp_inc
    unique_string = "/tmp/syn/%s.%s" % (
        os.getpid(),
        tmp_inc
    )
    tmp_inc += 1
    mkdir(unique_string, True)
    return unique_string


def mkdir(folder, destroy_old=False):
    try:
        os.mkdir(folder)
    except OSError as e:
        if e.errno == 17:
            rmdir(folder)
            return mkdir(folder, destroy_old=False)


@contextmanager
def workin_tmp():
    tmpdir = mktmp()
    with cd(tmpdir):
        yield
    rmdir(tmpdir)


def cp(source, dest):
    if os.path.isdir(source):
        new_name = os.path.basename(source)
        return shutil.copytree(source, "%s/%s" % (dest, new_name))
    else:
        return shutil.copy2(source, dest)


def link(source, dest):
    return os.symlink(source, dest)


def rm(file_name):
    return os.remove(file_name)


def mv(source, dest):
    return os.rename(source, dest)


def rmdir(path):
    return shutil.rmtree(path)


def abspath(folder):
    return os.path.abspath(folder)


def putenv(key, value):
    os.environ[key] = value


def getenv(key):
    return os.environ[key]
