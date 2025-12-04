import sys
import os

# Import common configuration
sys.path.insert(0, os.path.abspath('..'))
from common_conf import *  # noqa: F401, F403

# Project-specific configuration
project = "NVIDIA Driver Containers"
release = "1.0.0"

root_doc = "redirected"
redirects = {
  "index": "../../gpu-operator/latest/index.html",
  "overview": "../../gpu-operator/latest/index.html",
}

# Project-specific MyST substitutions
myst_substitutions = {
    'version': '1.0.0',
}

# Project-specific theme options (extends common html_theme_options)
html_theme_options = html_theme_options.copy()  # type: ignore[name-defined]
html_theme_options.update({
    "switcher": {
        "json_url": "../versions1.json",
        "version_match": release,
    },
})
