from abc import ABC, abstractmethod

class IDataProvider(ABC):
    @abstractmethod
    def acquire_data(self):
        pass

