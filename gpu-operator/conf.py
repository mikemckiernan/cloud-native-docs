import sys
import os

# Import common configuration
sys.path.insert(0, os.path.abspath('..'))
from common_conf import *  # noqa: F401, F403

# Project-specific configuration
project = "NVIDIA GPU Operator"
release = "25.10"

# Project-specific MyST substitutions
myst_substitutions = {
    'minor_version': '25.10',
    'version': 'v25.10.0',
    'recommended': '580.95.05'
}

# Project-specific theme options (extends common html_theme_options)
html_theme_options = html_theme_options.copy()  # type: ignore[name-defined]
html_theme_options.update({
    "switcher": {
        "json_url": "../versions1.json",
        "version_match": release,
    },
})

exclude_patterns = ['life-cycle-policy.rst']
