from __future__ import print_function as _

import os as _os
import sys as _sys
import json

from pkg_resources import get_distribution, DistributionNotFound

import dash as _dash

from ._imports_ import *
from ._imports_ import __all__

from .wrapped_components import *
from .wrapped_components import __all__ as wrapped_components

__all__ += wrapped_components

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass

if not hasattr(_dash, "development"):
    print(
        "Dash was not successfully imported. "
        "Make sure you don't have a file "
        "named 'dash.py' in your current directory.",
        file=_sys.stderr,
    )
    _sys.exit(1)

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, "package.json"))
with open(_filepath, encoding="utf8") as f:
    package = json.load(f)

package_name = (
    package["name"]
    .replace(" ", "_")
    .replace("-", "_")
    .replace("/", "_")
    .replace("@", "")
)

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_this_module = _sys.modules[__name__]


_js_dist = [
    {
        "relative_package_path": "webviz_core_components.min.js",
        "dev_package_path": "webviz_core_components.dev.js",
        "namespace": package_name,
    },
]

_css_dist = [
    {
        "relative_package_path": "webviz_core_components.css",
        "namespace": package_name,
    }
]


for _component in __all__:
    setattr(locals()[_component], "_js_dist", _js_dist)
    setattr(locals()[_component], "_css_dist", _css_dist)
