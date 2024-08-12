from abc import ABC, abstractmethod


class BaseCryptoAPI(ABC):

    @abstractmethod
    def get_category_list(self): 
        pass

    @abstractmethod
    def get_category_info(self): 
        pass

    @abstractmethod
    def get_cryptocurrency_list(self): 
        pass

    @abstractmethod
    def get_cryptocurrency_info(self): 
        pass