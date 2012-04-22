# Copyright header

from syn.system import cd
import os

def build_source_package(root):
    with cd(root):
        print os.getcwd()
