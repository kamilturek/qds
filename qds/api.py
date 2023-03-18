from ctypes import byref, c_uint32, c_void_p

from qds.clib import lib


def get_main_display_id() -> int:
    return lib.CGMainDisplayID()


def get_online_display_count() -> int:
    max_displays = 5
    display_count = c_uint32()

    while True:
        lib.CGGetOnlineDisplayList(c_uint32(max_displays), None, byref(display_count))
        if display_count.value != max_displays:
            break
        max_displays *= 2

    return display_count.value


def get_online_display_list() -> list[int]:
    max_displays = c_uint32(get_online_display_count())
    online_displays = (c_uint32 * max_displays.value)()

    lib.CGGetOnlineDisplayList(max_displays, online_displays, None)

    return list(online_displays)


def get_active_display_count() -> int:
    max_displays = 5
    display_count = c_uint32()

    while True:
        lib.CGGetActiveDisplayList(c_uint32(max_displays), None, byref(display_count))
        if display_count.value != max_displays:
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


def get_display_origin(display_id: int) -> tuple[int, int]:
    bounds = lib.CGDisplayBounds(display_id)
    return int(bounds.x), int(bounds.y)


def get_display_pixels_wide(display_id: int) -> int:
    return lib.CGDisplayPixelsWide(display_id)


def get_display_pixels_high(display_id: int) -> int:
    return lib.CGDisplayPixelsHigh(display_id)


class DisplayConfigurator:
    _display_configuration: c_void_p | None

    def __init__(self, display_id: int) -> None:
        self._display_id = display_id

    def __enter__(self):
        self._begin_configuration()
        return self

    def __exit__(self, exc, value, traceback):
        if exc:
            self._cancel_configuration()
        else:
            self._complete_configuration()

    def _begin_configuration(self) -> None:
        display_configuration = c_void_p()

        if lib.CGBeginDisplayConfiguration(display_configuration) != 0:
            raise Exception("begin error")

        self._display_configuration = display_configuration

    def _cancel_configuration(self) -> None:
        if lib.CGCancelDisplayConfiguration(self._display_configuration) != 0:
            raise Exception("cancel error")

        self._display_configuration = None

    def _complete_configuration(self) -> None:
        FOR_SESSION = 1

        if (
            lib.CGCompleteDisplayConfiguration(self._display_configuration, FOR_SESSION)
            != 0
        ):
            raise Exception("complete error")

        self._display_configuration = None

    def set_origin(self, x: int, y: int) -> None:
        if (
            lib.CGConfigureDisplayOrigin(
                self._display_configuration, self._display_id, x, y
            )
            != 0
        ):
            raise Exception("configure origin error")
