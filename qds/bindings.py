from ctypes import byref, c_uint32

from .lib import load
from .structs import CGRect, CGSize
from .types import Point, Rect, Size

quartz = load()


def main_display_id() -> int:
    return quartz.CGMainDisplayID()


def get_online_display_count() -> int:
    max_displays = c_uint32(5)
    display_count = c_uint32()

    while True:
        quartz.CGGetOnlineDisplayList(max_displays, None, byref(display_count))
        if display_count.value != max_displays.value:
            break
        max_displays *= 2

    return display_count.value


def get_online_display_list() -> list[int]:
    max_displays = c_uint32(get_online_display_count())
    online_displays = (c_uint32 * max_displays.value)()

    quartz.CGGetOnlineDisplayList(max_displays, online_displays, None)

    return list(online_displays)


def get_active_display_count() -> int:
    max_displays = c_uint32(5)
    display_count = c_uint32()

    while True:
        quartz.CGGetActiveDisplayList(max_displays, None, byref(display_count))
        if display_count.value != max_displays.value:
            break
        max_displays *= 2

    return display_count.value


def get_active_display_list() -> list[int]:
    max_displays = c_uint32(get_active_display_count())
    active_displays = (c_uint32 * max_displays.value)()

    quartz.CGGetActiveDisplayList(max_displays, active_displays, None)

    return list(active_displays)


def get_displays_with_point() -> list[int]:
    pass


def is_display_builtin(display_id: int) -> bool:
    return bool(quartz.CGDisplayIsBuiltin(c_uint32(display_id)))


def is_display_active(display_id: int) -> bool:
    return bool(quartz.CGDisplayIsActive(c_uint32(display_id)))


def is_display_online(display_id: int) -> bool:
    return bool(quartz.CGDisplayIsOnline(c_uint32(display_id)))


def display_screen_size(display_id: int) -> Size:
    quartz.CGDisplayScreenSize.restype = CGSize
    size = quartz.CGDisplayScreenSize(c_uint32(display_id))
    return Size(width=size.width, height=size.height)


def display_bounds(display_id: int) -> Rect:
    quartz.CGDisplayBounds.restype = CGRect
    rect = quartz.CGDisplayBounds(c_uint32(display_id))
    return Rect(
        origin=Point(
            x=rect.origin.x,
            y=rect.origin.y,
        ),
        size=Size(
            width=rect.size.width,
            height=rect.size.height,
        ),
    )


def display_pixels_wide(display_id: int) -> int:
    return quartz.CGDisplayPixelsWide(c_uint32(display_id))


def display_pixels_high(display_id: int) -> int:
    return quartz.CGDisplayPixelsHigh(c_uint32(display_id))
