import sys
import os

# Import common configuration
sys.path.insert(0, os.path.abspath('..'))
from common_conf import *  # noqa: F401, F403

# Project-specific configuration
project = "NVIDIA Container Toolkit"
release = "1.18.1"

# Project-specific MyST substitutions
myst_substitutions = {
    'version': 'v1.18.1',
}

# Project-specific theme options (extends common html_theme_options)
html_theme_options = html_theme_options.copy()  # type: ignore[name-defined]
html_theme_options.update({
    "switcher": {
        "json_url": "../versions1.json",
        "version_match": release,
    },
})

redirects = {
    "concepts": "index.html",
    "distro/amazon-linux": "install-guide.html",
    "distro/centos8": "install-guide.html",
    "distro/rhel7": "install-guide.html",
    "distro/suse15": "install-guide.html",
    "distro/ubuntu": "install-guide.html",
    "install/nvidia-container-toolkit": "install-guide.html",
    "install/repo-apt": "install-guide.html",
    "install/repo-yum": "install-guide.html",
    "install/repo-zypper": "install-guide.html",
    "nvidia-containerd": "install-guide.html",
    "nvidia-docker": "install-guide.html",
    "nvidia-podman": "install-guide.html",
    "overview": "index.html",
    "runtime/docker": "docker-specialized.html",
    "user-guide": "install-guide.html",
}
