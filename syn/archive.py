# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

import tarfile
import os.path

from syn.errors import NotImplementedException


class Tarball:
    def __init__(self, file_path):
        self._process_filename(file_path)
        self._fp = file_path
        self._startup_hook()

    def _process_filename(self, file_path):
        pass

    def _startup_hook(self):
        pass

    def _extract_hook(self):
        pass

    def _checksum_hook(self):
        pass

    def _root_folder(self):
        with tarfile.open(self._fp, mode='r') as fd:
            members = fd.getmembers()
            directories = []
            for member in members:
                directories.append(member.name)
            root_folder = os.path.commonprefix(directories)
            return root_folder

    def extract_to(self, file_path):
        self._extract_hook()
        with tarfile.open(self._fp, mode='r') as fd:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(fd, file_path)

    def checksum(self):
        self._checksum_hook()
        raise NotImplementedException("Sorry! :)")
        pass


def create_archive(source, archive_name):
    with tarfile.open(archive_name, 'w|gz') as tf:
        tf.add(source, recursive=True)
