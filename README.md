# QDS

A Python wrapper for [Quartz Display Services](https://developer.apple.com/documentation/coregraphics/quartz_display_services).

Supported Python versions are 3.10 and 3.11.

## Installation

```bash
pip install python-qds
```

## Usage

You can use a low-level C API bindings from the `qds.api` module.

```python
>>> import qds.api
>>> qds.api.get_online_display_list()
[1]
>>> qds.api.is_display_active(1)
True
>>> qds.api.get_display_pixels_wide(1)
1440
```

Or use the high-level `qds.display.Display` class being a convenience wrapper for
the low-level functions.

```python
>>> from qds.display import Display
>>> d = Display.from_id(1)
>>> d.is_online
True
>>> d.width
1440
```
