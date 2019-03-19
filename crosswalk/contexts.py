from ._core import reroute, UndefinedRouting

from . import time
from . import query
from . import scene


# ------------------------------------------------------------------------------
@reroute
class RetainedSelection(object):
    """
    Cache selection on entering and re-select on exit
    """

    # --------------------------------------------------------------------------
    def __enter__(self):
        self._selected = query.selected()

    # --------------------------------------------------------------------------
    def __exit__(self, *exc_info):
        if self._selected:
            element.select(self._selected)


# ------------------------------------------------------------------------------
class RetainedTime(object):
    """
    Cache selection on entering and re-select on exit
    """

    # --------------------------------------------------------------------------
    def __enter__(self):
        self._start = time.start()
        self._end = time.end()

    # --------------------------------------------------------------------------
    def __exit__(self, *exc_info):
        time.set_start(self._start)
        time.set_end(self._end)


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)