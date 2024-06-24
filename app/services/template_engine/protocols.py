"""Holds protocols for the template engine"""

from typing import Protocol


# pylint: disable=too-few-public-methods
class Renderable(Protocol):
    """Used to render HTML pages"""

    def render(self, name: str, **kwargs):
        """
        Renders a HTML template

        :param str name: Template name
        :param **kwargs: Additional context properties
        """
