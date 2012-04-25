# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

from syn.system import cd, run, mkdir, putenv, abspath, workin_tmp
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

    with workin_tmp():
        pass


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
