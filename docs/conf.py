# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "UCL Enterprise Architecture"
copyright = "2026, UCL"
author = "UCL"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinxcontrib.mermaid",
]

# MyST parser settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]

myst_heading_anchors = 3

# Source file suffixes
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_book_theme"
html_title = "UCL Enterprise Architecture"

html_theme_options = {
    "repository_url": "https://github.com/UCL/enterprise-architecture",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs",
    "show_toc_level": 2,
    "navigation_with_keys": True,
    "logo": {
        "image_light": "https://cdn.ucl.ac.uk/logos/ucl/ucl-logo--secondary.svg",
        "image_dark": "https://cdn.ucl.ac.uk/logos/ucl/ucl-logo--secondary-inverted.svg",
    },
}

# Custom CSS
html_css_files = [
    "ucl-overrides.css",
]

# Exclude patterns
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
