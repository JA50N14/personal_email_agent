from abc import ABC, abstractmethod


class EmailProvider(ABC):

    @abstractmethod
    def get_messages(self):
        pass