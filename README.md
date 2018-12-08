# buffer_autohide
Weechat script to automatically hide read IRC buffers (and to unhide them on new activity)

## Install
Place `buffer_autohide.py` into your `~/.weechat/python/` folder and enable it in weechat with `/script load buffer_autohide.py`.

## Configuration
The behaviour of buffer_autohide can be altered via `plugins.conf`:
* `python.buffer_autohide.hide_inactive`: Hide inactive buffers (default: `off`)
* `python.buffer_autohide.hide_private`: Hide private buffers (default: `off`)
* `python.buffer_autohide.unhide_low`: Unhide a buffer when a low message (JOIN, PART, etc.) has been received (default: `off`)
* `python.buffer_autohide.excemptions`: An enumeration of buffers that should not become hidden (default: `""`)

