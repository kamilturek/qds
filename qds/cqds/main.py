from ctypes import CDLL, POINTER, c_bool, c_int, c_uint32
from ctypes.util import find_library

from .types import CGDirectDisplayID, CGError


def _load_lib():
    LIBNAME = "ApplicationServices"

    if libpath := find_library(LIBNAME):
        lib = CDLL(libpath)
        lib.CGMainDisplayID()  # Precheck
        return lib

    raise OSError(f"Library {LIBNAME} not found.")


class Quartz:
    """
    A low-level, ctypes interface for accessing Quartz Display Services.
    Specifies the required argument types and return types.

    https://developer.apple.com/documentation/coregraphics/quartz_display_services
    """

    def __init__(self) -> None:
        self._lib = _load_lib()

    # Finding Displays

    def CGMainDisplayID(self) -> int:
        self._lib.CGMainDisplayID.argtypes = []
        self._lib.CGMainDisplayID.restype = c_int
        return self._lib.CGMainDisplayID()

    def CGGetOnlineDisplayList(self, maxDisplays, onlineDisplays, displayCount) -> int:
        self._lib.CGGetOnlineDisplayList.argtypes = [
            c_uint32,
            POINTER(CGDirectDisplayID),
            POINTER(c_uint32),
        ]
        self._lib.CGGetOnlineDisplayList.restype = CGError
        return self._lib.CGGetOnlineDisplayList(
            maxDisplays,
            onlineDisplays,
            displayCount,
        )

    def CGGetActiveDisplayList(self, maxDisplays, activeDisplays, displayCount) -> int:
        self._lib.CGGetActiveDisplayList.argtypes = [
            c_uint32,
            POINTER(CGDirectDisplayID),
            POINTER(c_uint32),
        ]
        self._lib.CGGetActiveDisplayList.restype = CGError
        return self._lib.CGGetActiveDisplayList(
            maxDisplays,
            activeDisplays,
            displayCount,
        )

    # Getting the Display Configuration

    def CGDisplayIsActive(self, display) -> bool:
        self._lib.CGDisplayIsActive.argtypes = [CGDirectDisplayID]
        self._lib.CGDisplayIsActive.restype = c_bool
        return self._lib.CGDisplayIsActive(display)

    def CGDisplayIsBuiltin(self, display) -> bool:
        self._lib.CGDisplayIsBuiltin.argtypes = [CGDirectDisplayID]
        self._lib.CGDisplayIsBuiltin.restype = c_bool
        return self._lib.CGDisplayIsBuiltin(display)

    def CGDisplayIsOnline(self, display) -> bool:
        self._lib.CGDisplayIsOnline.argtypes = [CGDirectDisplayID]
        self._lib.CGDisplayIsOnline.restype = c_bool
        return self._lib.CGDisplayIsOnline(display)

    # Retrieving Display Parameters

    def CGDisplayPixelsHigh(self, display) -> int:
        self._lib.CGDisplayPixelsHigh.argtypes = [CGDirectDisplayID]
        self._lib.CGDisplayPixelsHigh.restype = c_int
        return self._lib.CGDisplayPixelsHigh(display)

    def CGDisplayPixelsWide(self, display) -> int:
        self._lib.CGDisplayPixelsWide.argtypes = [CGDirectDisplayID]
        self._lib.CGDisplayPixelsWide.restype = c_int
        return self._lib.CGDisplayPixelsWide(display)
