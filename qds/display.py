from qds import api


class Display:
    def __init__(self, id: int) -> None:
        self._id = id

    @classmethod
    def from_id(cls, id: int) -> "Display":
        if id not in api.get_online_display_list():
            raise ValueError("Invalid display ID.")
        return cls(id)

    @property
    def is_main(self) -> bool:
        return self._id == api.get_main_display_id()

    @property
    def is_active(self) -> bool:
        return api.is_display_active(self._id)

    @property
    def is_builtin(self) -> bool:
        return api.is_display_builtin(self._id)

    @property
    def is_online(self) -> bool:
        return api.is_display_online(self._id)

    @property
    def width(self) -> int:
        return api.get_display_pixels_wide(self._id)

    @property
    def height(self) -> int:
        return api.get_display_pixels_high(self._id)
