# buffer_autohide
Weechat script to automatically hide read IRC buffers (and to unhide them on new activity)

## Install
Place `buffer_autohide.py` into your `~/.weechat/python/` folder and enable it in weechat with `/script load buffer_autohide.py`.

## Configuration
The behaviour of buffer_autohide can be altered via `plugins.conf`:
* `python.buffer_autohide.hide_inactive`: Hide inactive buffers (default: `off`)
* `python.buffer_autohide.hide_private`: Hide private buffers (default: `off`)
* `python.buffer_autohide.unhide_low`: Unhide a buffer when a low message (JOIN, PART, etc.) has been received (default: `off`)
* `python.buffer_autohide.exemptions`: An enumeration of buffers that should not become hidden (default: `""`)
* `python.buffer_autohide.keep_open`: Keep a buffer open for a short amount of time (default: "off")
* `python.buffer_autohide.keep_open_timeout`: Timeout in milliseconds for how long a selected buffer should be kept around (default: "60 * 1000")

