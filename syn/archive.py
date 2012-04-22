# Copyright

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
            fd.extractall(file_path)

    def checksum(self):
        self._checksum_hook()
        raise NotImplementedException("Sorry! :)")
        pass


class UpstreamTarball(Tarball):
    def _process_filename(self, file_path):
        pass

    def _startup_hook(self):
        pass

    def _extract_hook(self):
        pass

    def _checksum_hook(self):
        pass


class SynSourceTarball(Tarball):
    def _process_filename(self, file_path):
        pass

    def _startup_hook(self):
        pass

    def _extract_hook(self):
        pass

    def _checksum_hook(self):
        pass


class SynBinaryTarball(Tarball):
    def _process_filename(self, file_path):
        pass

    def _startup_hook(self):
        pass

    def _extract_hook(self):
        pass

    def _checksum_hook(self):
        pass
