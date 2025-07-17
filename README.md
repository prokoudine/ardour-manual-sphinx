# Ardour user manual

This is a preliminary port of the [Ardour manual](https://manual.ardour.org) to Sphinx.

## Prerequisites

`$ pip install sphinx sphinx-book-theme sphinxcontrib-video sphinx-multiversion`

## Building HTML

The following command builds an HTML version of the user manual:

`$ make html`

## TODO

- [X] Pick an initial theme
- [ ] Do the the port (pandoc to convert + images)
- [ ] Restructure the guide (parts of the Interface chapter belong to Editing and Mixing)
- [ ] Fix all the broken references (clean rebuild shows them all)
- [ ] Clean up formatting (replace `:menuselection:` and `:guilabel:` with bold text)
- [ ] Set up CI (deployment, linting)
- [ ] Take care of redirects where possible
