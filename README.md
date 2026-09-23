# UCL Enterprise Architecture

Documentation site built with [MyST](https://myst-parser.readthedocs.io/) and [Sphinx](https://www.sphinx-doc.org/), published to GitHub Pages.

## Structure

```
docs/
├── index.md          # Home page
├── conf.py           # Sphinx configuration
└── _static/
    └── ucl-overrides.css
```

Add new pages as Markdown files under `docs/` and link them from the `toctree` in `index.md`.

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Build the site
sphinx-build -b html docs docs/_build/html

# Serve locally (optional)
python -m http.server -d docs/_build/html
```

## Deployment

The site deploys automatically to GitHub Pages on push to `main` via GitHub Actions (`.github/workflows/deploy.yml`).

To enable GitHub Pages:
1. Go to **Settings → Pages** in your GitHub repository
2. Set **Source** to **GitHub Actions**

## Authoring

The site uses MyST-flavoured Markdown with support for:
- Mermaid diagrams (fenced with `` ```{mermaid} ``)
- Admonitions (`` :::{note} ``, `` :::{warning} ``, etc.)
- Definition lists, task lists, and cards via `sphinx-design`
