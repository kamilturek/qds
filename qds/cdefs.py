from ctypes import CDLL, POINTER, c_bool, c_int, c_uint32


def precheck(lib: CDLL) -> None:
    lib.CGMainDisplayID()


def define_api(lib: CDLL) -> None:
    """
    Define Quartz Display Services API.

    https://developer.apple.com/documentation/coregraphics/quartz_display_services
    """

    CGDirectDisplayID = c_uint32
    CGError = int

    lib.CGMainDisplayID.argtypes = []
    lib.CGMainDisplayID.restype = c_int

    lib.CGGetOnlineDisplayList.argtypes = [
        c_uint32,
        POINTER(CGDirectDisplayID),
        POINTER(c_uint32),
    ]
    lib.CGGetOnlineDisplayList.restype = CGError

    lib.CGGetActiveDisplayList.argtypes = [
        c_uint32,
        POINTER(CGDirectDisplayID),
        POINTER(c_uint32),
    ]
    lib.CGGetActiveDisplayList.restype = CGError

    lib.CGDisplayIsActive.argtypes = [CGDirectDisplayID]
    lib.CGDisplayIsActive.restype = c_bool

    lib.CGDisplayIsBuiltin.argtypes = [CGDirectDisplayID]
    lib.CGDisplayIsBuiltin.restype = c_bool

    lib.CGDisplayIsOnline.argtypes = [CGDirectDisplayID]
    lib.CGDisplayIsOnline.restype = c_bool

    lib.CGDisplayPixelsHigh.argtypes = [CGDirectDisplayID]
    lib.CGDisplayPixelsHigh.restype = c_int

    lib.CGDisplayPixelsWide.argtypes = [CGDirectDisplayID]
    lib.CGDisplayPixelsWide.restype = c_int
