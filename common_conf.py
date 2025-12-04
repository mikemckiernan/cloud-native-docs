"""
Common Sphinx configuration for NVIDIA Cloud Native documentation projects.

This file contains shared configuration that can be imported by project-specific
conf.py files. Project-specific conf.py files should:
1. Import this file
2. Override project-specific settings (project, release, myst_substitutions, etc.)
"""

import os

here = os.path.dirname(os.path.abspath(__file__))

# Common Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",  # include documentation from docstrings
    "sphinx.ext.ifconfig",  # conditional include of text
    "sphinx.ext.napoleon",  # support for NumPy and Google style docstrings
    "sphinx.ext.intersphinx",  # link to other projects' documentation
    "sphinx.ext.extlinks",  # add roles to shorten external links
    "myst_parser",  # markdown parsing
    "sphinxcontrib.mermaid",  # create diagrams using text and code
    "sphinx_design",
    "sphinx_reredirects",
    "linuxdoc.rstFlatTable",
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton",
]

# Copy button configuration
copybutton_exclude = '.linenos, .gp, .go'

# MyST configuration
myst_heading_anchors = 4  # automatically add section level labels, up to level 4

myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "substitution",
]

# General configuration
templates_path = [os.path.join(here, 'templates')]
suppress_warnings = ['autosectionlabel.*']
pygments_style = 'sphinx'
highlight_language = 'console'

# HTML output configuration
html_theme = "nvidia_sphinx_theme"
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False
html_domain_indices = False
html_use_index = False

html_extra_path = ["versions1.json"]

# HTML theme options (common defaults)
html_theme_options = {
    "icon_links": [],
    "copyright_override": {"start": 2020},
}

# Intersphinx mapping for cross-project references
intersphinx_mapping = {
    "dcgm": ("https://docs.nvidia.com/datacenter/dcgm/latest/", os.path.join(here, "work/dcgm-offline.inv")),
    "gpuop": ("https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/",
              (os.path.join(here, "_build/docs/gpu-operator/objects.inv"), None)),
    "ctk": ("https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/",
            (os.path.join(here, "_build/docs/container-toolkit/objects.inv"), None)),
    "drv": ("https://docs.nvidia.com/datacenter/cloud-native/driver-containers/latest/",
            (os.path.join(here, "_build/docs/driver-containers/objects.inv"), None)),
    "ocp": ("https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/",
            (os.path.join(here, "_build/docs/openshift/objects.inv"), None)),
    "edge": ("https://docs.nvidia.com/datacenter/cloud-native/edge/latest/",
            (os.path.join(here, "_build/docs/edge/objects.inv"), None)),
}
