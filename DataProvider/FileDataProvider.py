from interfaces.IDataProvider import IDataProvider

class FileDataProvider(IDataProvider):
    def __init__(self, file_path: str):
        self.file_path: str = file_path

    def acquire_data(self) -> str:
        with open(self.file_path, 'r', encoding='UTF-8') as file:
            return file.read()