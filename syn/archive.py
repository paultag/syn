# Copyright


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

    def extract_to(self, file_path):
        self._extract_hook()
        with tarfile.open(file_path, mode='r') as fd:
            pass


    def checksum(self):
        self._checksum_hook()
        pass

class UpstreamTarball(Tarball):
    pass


class SynSourceTarball(Tarball):
    pass


class SynBinaryTarball(Tarball):
    pass
