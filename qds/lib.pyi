from ctypes import c_uint32, pointer

from .structs import CGRect, CGSize

def load() -> QuartzDisplayServices: ...

class QuartzDisplayServices:
    def CGMainDisplayID(self) -> int: ...
    def CGGetOnlineDisplayList(
        self,
        maxDisplays: c_uint32,
        onlineDisplays: pointer[c_uint32],
        displayCount: pointer[c_uint32],
    ): ...
    def CGGetActiveDisplayList(
        self,
        maxDisplays: c_uint32,
        activeDisplays: pointer[c_uint32],
        displayCount: pointer[c_uint32],
    ): ...
    def CGGetDisplaysWithPoint(
        self,
        point,
        maxDisplays: c_uint32,
        displays: pointer[c_uint32],
        matchingDisplayCount: pointer[c_uint32],
    ): ...
    def CGDisplayIsActive(
        self,
        display: c_uint32,
    ) -> bool: ...
    def CGDisplayIsBuiltin(
        self,
        display: c_uint32,
    ) -> bool: ...
    def CGDisplayIsOnline(
        self,
        display: c_uint32,
    ) -> bool: ...
    def CGDisplayScreenSize(
        self,
        display: c_uint32,
    ) -> CGSize: ...

    # Retrieving Display Parameters
    def CGDisplayBounds(
        self,
        display: c_uint32,
    ) -> CGRect: ...
    def CGDisplayPixelsHigh(
        self,
        display: c_uint32,
    ) -> int: ...
    def CGDisplayPixelsWide(
        self,
        display: c_uint32,
    ) -> int: ...
