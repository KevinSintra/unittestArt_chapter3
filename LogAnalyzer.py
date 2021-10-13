from abc import ABCMeta, abstractmethod
from typing import ClassVar  # 提供抽象行為


class IExtensionManager(metaclass=ABCMeta):  # 介面
    '''為了讓測試能進行, 所以重構程式時增加該介面'''
    @abstractmethod
    def isValid(self, fileName: str) -> bool:
        pass


class LogAnalyzer:
    __manager: IExtensionManager

    def __init__(self):
        self.__manager = ExtensionManagerFactory().create()
        pass

    def isValidLogFileName(self, fileName):
        return self.__manager.isValid(fileName)

    @property
    def manager(self):  # getter
        return self.__manager

    @manager.setter
    def manager(self, mgr: IExtensionManager):  # setter
        self.__manager = mgr
        pass


class FileExtensionManager(IExtensionManager):  # 繼承
    def isValid(self, fileName: str) -> bool:
        # 這裡是要讀取外部檔案, 先不進行實作
        return True


class ExtensionManagerFactory:
    '''工廠模式: 產生指定類別的實例 達到關注點分離並各司其職.'''
    __manager: IExtensionManager = None

    def create(self):
        if(self.__manager != None):
            return self.__manager
        else:
            mgr: IExtensionManager = FileExtensionManager()
            self.__manager = mgr
            return self.__manager

    def setManager(self, mgr: IExtensionManager):
        self.__manager = mgr
        pass
