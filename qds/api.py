from ctypes import byref, c_uint32

from .clib import lib


def get_main_display_id() -> int:
    return lib.CGMainDisplayID()


def get_online_display_count() -> int:
    max_displays = c_uint32(5)
    display_count = c_uint32()

    while True:
        lib.CGGetOnlineDisplayList(max_displays, None, byref(display_count))
        if display_count.value != max_displays.value:
            break
        max_displays *= 2

    return display_count.value


def get_online_display_list() -> list[int]:
    max_displays = c_uint32(get_online_display_count())
    online_displays = (c_uint32 * max_displays.value)()

    lib.CGGetOnlineDisplayList(max_displays, online_displays, None)

    return list(online_displays)


def get_active_display_count() -> int:
    max_displays = c_uint32(5)
    display_count = c_uint32()

    while True:
        lib.CGGetActiveDisplayList(max_displays, None, byref(display_count))
        if display_count.value != max_displays.value:
            break
        max_displays *= 2

    return display_count.value


def get_active_display_list() -> list[int]:
    max_displays = c_uint32(get_active_display_count())
    active_displays = (c_uint32 * max_displays.value)()

    lib.CGGetActiveDisplayList(max_displays, active_displays, None)

    return list(active_displays)


def is_display_active(display_id: int) -> bool:
    return lib.CGDisplayIsActive(display_id)


def is_display_builtin(display_id: int) -> bool:
    return lib.CGDisplayIsBuiltin(display_id)


def is_display_online(display_id: int) -> bool:
    return lib.CGDisplayIsOnline(display_id)


def get_display_bounds(display_id: int):
    return lib.CGDisplayBounds(display_id)


def get_display_pixels_wide(display_id: int) -> int:
    return lib.CGDisplayPixelsWide(display_id)


def get_display_pixels_high(display_id: int) -> int:
    return lib.CGDisplayPixelsHigh(display_id)
