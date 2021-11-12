import functools
import requests
import http
import sys

from typing import IO


def example_function(
    response: requests.Response,
    status: http.HTTPStatus,
    stream: IO[str] = sys.stdout,
) -> requests.Request:
    """
    Example function using :mod:`requests`.

    It looks like :doc:`autodoc <usage/extensions/autodoc>` is resolving type hints like
    ``requests.Response`` to their internal definition, e.g.
    ``requests.models.Response``. This `caused an issue
    <https://github.com/psf/requests/issues/5954>`_ (now fixed) with :doc:`intersphinx
    <usage/extensions/intersphinx>` references.

    For comparison, this function includes type hints for the Python standard library
    and explicit references to the public APIs via `interphinx-untangled
    <https://webknjaz.github.io/intersphinx-untangled/>`_.

    :param response: A :class:`requests.Response` instance.
    :param status: An :class:`http.HTTPStatus` instance.
    :param stream: A :class:`typing.IO` instance.

    :return: A :class:`requests.Request` instance.

    :raises requests.HTTPError: A :class:`requests.HTTPError` instance.
    """
    response.raise_for_status()
    return response.request


#: Example partial with default value for ``status``.
example_partial = functools.partial(example_function, status=http.HTTPStatus.ACCEPTED)
