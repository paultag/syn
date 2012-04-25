# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

from syn.system import cd, run, mkdir, putenv, abspath, workin_tmp, cp
from syn.archive import Tarball
from syn.db import Database
import os.path


def preform_step(step_name):
    return run(["synd/build", step_name])


def compose_source_archive(unpacked_root, upstream_tarball):
    """
    Generate a signing Database, correctly named tarball and
    a syn local tarball.

     - Head over to tmp/<something/
     - Create new archive with the synd/
     - Rename upstream tarball correctly
     - Create new DB, hash tarballs
     - Move back to where we want
    """
    unpacked_root = os.path.abspath(unpacked_root)
    upstream_tarball = os.path.abspath(upstream_tarball)
    root_name = os.path.basename(unpacked_root)
    tarball_name = os.path.basename(upstream_tarball)
    # XXX: Generate the source targz

    tb = Tarball(upstream_tarball)
    tb_root = tb._root_folder()
    if root_name != tb_root:
        print "The archive's root is wrong. Fix the syn root."
        # XXX: Fix this print
        raise Exception("Bad archive")  # XXX: Fix this Exception

    with workin_tmp():
        cp(unpacked_root, "./")
        cp(upstream_tarball, "./")


def extract_source_archive(signed_database, root):
    """
    Verify the SHA sums, and compose a correctly formed
    unpacked syn source directory using the archives noted
    in the signed db.

     - Extract to /tmp/<something>/
     - Move root directory/* to new root
     - Extract synd on top of new root
     - Move back to where we want
    """
    pass


def build_source_package(root, steps):
    """Run the build targets, and create a binary package."""
    with cd(root):
        metainf = Database("synd/metainf")
        mkdir("synd/tmp", destroy_old=True)
        putenv("SYN_DESTDIR", abspath("synd/tmp"))
        for step in steps:
            preform_step(step)
        # We've now got our tree (magically) in synd/tmp
        # Let's package it nicely.
