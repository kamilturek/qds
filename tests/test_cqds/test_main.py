import pytest

from qds.cqds.main import Quartz


@pytest.mark.integration
class TestQuartz:
    def test_CGMainDisplayID(self):
        assert isinstance(Quartz().CGMainDisplayID(), int)

    def test_CGGetOnlineDisplayList(self):
        assert isinstance(Quartz().CGGetOnlineDisplayList(0, None, None), int)

    def test_CGGetActiveDisplayList(self):
        assert isinstance(Quartz().CGGetActiveDisplayList(0, None, None), int)

    def test_CGDisplayIsActive(self):
        assert isinstance(Quartz().CGDisplayIsActive(1), bool)

    def test_CGDisplayIsBuiltin(self):
        assert isinstance(Quartz().CGDisplayIsBuiltin(1), bool)

    def test_CGDisplayIsOnline(self):
        assert isinstance(Quartz().CGDisplayIsOnline(1), bool)

    def test_CGDisplayPixelsHigh(self):
        assert isinstance(Quartz().CGDisplayPixelsHigh(1), int)

    def test_CGDisplayPixelsWide(self):
        assert isinstance(Quartz().CGDisplayPixelsWide(1), int)
