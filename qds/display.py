from qds import api


class Display:
    def __init__(self, id: int) -> None:
        self.id = id

    @classmethod
    def from_id(cls, id: int) -> "Display":
        if id not in api.get_online_display_list():
            raise ValueError("Invalid display ID.")
        return cls(id)

    @classmethod
    def all(cls) -> list["Display"]:
        return [cls.from_id(display_id) for display_id in api.get_online_display_list()]

    @property
    def is_main(self) -> bool:
        return self.id == api.get_main_display_id()

    @property
    def is_active(self) -> bool:
        return api.is_display_active(self.id)

    @property
    def is_builtin(self) -> bool:
        return api.is_display_builtin(self.id)

    @property
    def is_online(self) -> bool:
        return api.is_display_online(self.id)

    @property
    def origin(self) -> tuple[int, int]:
        return api.get_display_origin(self.id)

    @property
    def width(self) -> int:
        return api.get_display_pixels_wide(self.id)

    @property
    def height(self) -> int:
        return api.get_display_pixels_high(self.id)

    def configure(self) -> api.DisplayConfigurator:
        return api.DisplayConfigurator(self.id)

    def __repr__(self) -> str:
        return f"<Display {self.id}>"
