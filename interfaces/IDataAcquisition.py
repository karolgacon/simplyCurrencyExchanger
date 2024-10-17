from abc import ABC, abstractmethod

class IDataAcquisition(ABC):
    @abstractmethod
    def acquire_data(self):
        pass

