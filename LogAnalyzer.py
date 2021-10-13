from abc import ABCMeta, abstractmethod  # 提供抽象行為


class IExtensionManager(metaclass=ABCMeta):  # 介面
    '''為了讓測試能進行, 所以重構程式時增加該介面'''
    @abstractmethod
    def isValid(self, fileName: str) -> bool:
        pass


class LogAnalyzer:
    __manager: IExtensionManager

    def __init__(self):
        self.__manager = FileExtensionManager()
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
