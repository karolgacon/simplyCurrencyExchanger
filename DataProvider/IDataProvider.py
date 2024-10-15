from abc import ABC, abstractmethod


class IDataProvider(ABC):
    @abstractmethod
    def acquireData(self):
        pass
