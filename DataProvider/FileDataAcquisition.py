from interfaces.IDataAcquisition import IDataAcquisition

class FileDataAcquisition(IDataAcquisition):
    def __init__(self, file_path: str):
        self.file_path: str = file_path

    def acquire_data(self) -> str:
        with open(self.file_path, 'r') as file:
            return file.read()