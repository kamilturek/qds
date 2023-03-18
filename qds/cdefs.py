from ctypes import CDLL, POINTER, c_bool, c_int, c_int32, c_uint32, c_void_p

from qds.cstructs import CGRect


def precheck(lib: CDLL) -> None:
    lib.CGMainDisplayID()


def define_api(lib: CDLL) -> None:
    """
    Define Quartz Display Services API.

    https://developer.apple.com/documentation/coregraphics/quartz_display_services
    """

    lib.CGMainDisplayID.argtypes = []
    lib.CGMainDisplayID.restype = c_int

    lib.CGGetOnlineDisplayList.argtypes = [
        c_uint32,
        POINTER(c_uint32),
        POINTER(c_uint32),
    ]
    lib.CGGetOnlineDisplayList.restype = c_int32

    lib.CGGetActiveDisplayList.argtypes = [
        c_uint32,
        POINTER(c_uint32),
        POINTER(c_uint32),
    ]
    lib.CGGetActiveDisplayList.restype = c_int32

    lib.CGDisplayIsActive.argtypes = [c_uint32]
    lib.CGDisplayIsActive.restype = c_bool

    lib.CGDisplayIsBuiltin.argtypes = [c_uint32]
    lib.CGDisplayIsBuiltin.restype = c_bool

    lib.CGDisplayIsOnline.argtypes = [c_uint32]
    lib.CGDisplayIsOnline.restype = c_bool

    # Configuring Displays
    lib.CGBeginDisplayConfiguration.argtypes = [POINTER(c_void_p)]
    lib.CGBeginDisplayConfiguration.restype = c_int32

    lib.CGConfigureDisplayOrigin.argtypes = [
        POINTER(c_void_p),
        c_uint32,
        c_int32,
        c_int32,
    ]
    lib.CGConfigureDisplayOrigin.restype = c_int32

    lib.CGCompleteDisplayConfiguration.argtypes = [
        c_void_p,
        c_uint32,
    ]
    lib.CGCompleteDisplayConfiguration.restype = c_int32

    lib.CGCancelDisplayConfiguration.argtypes = [c_void_p]
    lib.CGCancelDisplayConfiguration.restype = c_int32

    lib.CGConfigureDisplayOrigin.argtypes = [
        c_void_p,
        c_uint32,
        c_int32,
        c_int32,
    ]
    lib.CGConfigureDisplayOrigin.restype = c_int32

    # Retrieving Display Parameters
    lib.CGDisplayBounds.argtypes = [c_uint32]
    lib.CGDisplayBounds.restype = CGRect

    lib.CGDisplayPixelsHigh.argtypes = [c_uint32]
    lib.CGDisplayPixelsHigh.restype = c_int

    lib.CGDisplayPixelsWide.argtypes = [c_uint32]
    lib.CGDisplayPixelsWide.restype = c_int
