# Copyright header

from syn.system import cd, run, mkdir, putenv, abspath
import os

def preform_step(step_name):
    return run(["synd/build", step_name])


def build_source_package(root, steps):
    with cd(root):
        mkdir("synd/tmp")
        putenv("SYN_DESTDIR", abspath("synd/tmp"))
        for step in steps:
            preform_step(step)
