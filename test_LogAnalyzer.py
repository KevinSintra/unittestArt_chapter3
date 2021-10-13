from LogAnalyzer import FileExtensionManager, LogAnalyzer


class FakeExtensionManager(FileExtensionManager): # 命名為 Fake 開頭, 不容易讓人混淆
    '''假物件最好放在對應的測試底下'''
    willBeValid = False

    def isValid(self, fileName: str) -> bool:
        # 這裡是要讀取外部檔案, 先不進行實作
        return self.willBeValid


class TestLogAnalyzer:
    def test_IsValidLogFileName_NameSupportedExtension_ReturnTrue(self):
        fakeMgr = FakeExtensionManager()
        fakeMgr.willBeValid = True
        log = LogAnalyzer(fakeMgr)
        result = log.isValidLogFileName("short.ext")
        assert result == True
