import sys
import os

# Import common configuration
sys.path.insert(0, os.path.abspath('..'))
from common_conf import *  # noqa: F401, F403

# Project-specific configuration
project = "NVIDIA GPU Operator on Red Hat OpenShift Container Platform"
release = "25.10"

# Project-specific theme options (extends common html_theme_options)
html_theme_options = html_theme_options.copy()  # type: ignore[name-defined]
html_theme_options.update({
    "switcher": {
        "json_url": "../versions1.json",
        "version_match": release,
    },
})

exclude_patterns = ['get-entitlement.rst']
