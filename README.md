# UCL Enterprise Architecture

Documentation site for UCL's enterprise architecture models, built with [MyST](https://myst-parser.readthedocs.io/) and [Sphinx](https://www.sphinx-doc.org/).

## Structure

```
docs/
├── index.md                          # Home page
├── conf.py                           # Sphinx configuration
├── models/
│   ├── business-capability.md        # Business capability model
│   ├── application-landscape.md      # Application portfolio
│   ├── data-architecture.md          # Data model and flows
│   └── technology-infrastructure.md  # Infrastructure layers
└── reference/
    ├── principles.md                 # Architecture principles
    ├── standards.md                  # Technical standards
    └── glossary.md                   # Terminology
```

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

The site deploys automatically to GitHub Pages on push to `main` via GitHub Actions.

To enable GitHub Pages:
1. Go to **Settings → Pages** in your GitHub repository
2. Set **Source** to **GitHub Actions**

## Contributing

Edit or add Markdown files under `docs/`. The site uses MyST-flavoured Markdown with support for:
- Mermaid diagrams (fenced with `` ```{mermaid} ``)
- Admonitions (`` :::{note} ``, `` :::{warning} ``, etc.)
- Definition lists, task lists, and cards via `sphinx-design`

Push to `main` to trigger a rebuild and deploy.
