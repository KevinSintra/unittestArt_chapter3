class LogAnalyzer:
    def isValidLogFileName(self, fileName):
        mgr = FileExtensionManager()
        return mgr.IsValid(fileName)


class FileExtensionManager:
    def IsValid(self, fileName):
        # 這裡是要讀取外部檔案, 先不進行實作
        return True
