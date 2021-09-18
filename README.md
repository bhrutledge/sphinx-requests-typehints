# sphinx-requests-typehints

Example project showing how Sphinx's [`autdoc`](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) and [`intersphinx`](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html) extensions handle type hints from [`requests`](https://docs.python-requests.org/en/master/).

See the rendered API documentation at <https://sphinx-requests-typehints.readthedocs.io/>.

## Getting started

In an active virtual environment:

```sh
pip install -r requirements.txt

make -c docs html

open docs/_build/html/example_package.html
```
