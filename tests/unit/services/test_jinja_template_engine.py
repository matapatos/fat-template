"""Holds unit tests for Jinja template engine"""

# pylint: disable=protected-access

from pathlib import Path
from unittest.mock import MagicMock, call, mock_open, patch

import pytest
from fastapi import HTTPException
from services.template_engine.jinja import JinjaTemplateEngine


def test_bundle_urls_for_register():
    """Tests __init__ function"""
    template_engine = JinjaTemplateEngine(
        request=None,
        templates_dir=Path("/mock-dir"),
        bundle_entrypoints_filepath=Path("/filepath/entrypoints.json"),
    )
    bundle_urls_for = template_engine._templates.env.globals["bundle_urls_for"]
    # pylint: disable=comparison-with-callable
    assert bundle_urls_for == template_engine._bundle_urls_for


@pytest.mark.parametrize("bundle_name", ["invalid", "invalidcss", "invalidjs"])
def test_bundle_urls_for_invalid_name(bundle_name: str):
    """
    Tests bundle_urls_for function
    When an invalid bundle name is provided
    """
    template_engine = JinjaTemplateEngine(
        request=None,
        templates_dir=Path("/mock-dir"),
        bundle_entrypoints_filepath=Path("/filepath/entrypoints.json"),
    )
    with pytest.raises(
        HTTPException,
        match="Missing dot in bundle name. Expected something like "
        f"'{bundle_name}.js' or '{bundle_name}.css' but got '{bundle_name}'",
    ):
        template_engine._bundle_urls_for(bundle_name)


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='{"test":{"js":["test.js","test2.js"]}}',
)
def test_bundle_urls_for(mocked_open: MagicMock):
    """
    Tests bundle_urls_for function
    When no entrypoints has been loaded
    """
    mocked_request = MagicMock()
    del mocked_request.app.state.bundle_entrypoints
    template_engine = JinjaTemplateEngine(
        request=mocked_request,
        templates_dir=Path("/mock-dir"),
        bundle_entrypoints_filepath=Path("/filepath/entrypoints.json"),
    )
    assert template_engine._bundle_urls_for("test.js") == ["/test.js", "/test2.js"]
    assert mocked_open.called


def test_bundle_urls_for_doesnt_reload():
    """
    Tests bundle_urls_for function
    When a set of entrypoints has already been loaded
    """
    mocked_request = MagicMock()
    mocked_request.app.state.bundle_entrypoints = {
        "test": {"js": ["test.js", "test2.js"]}
    }
    template_engine = JinjaTemplateEngine(
        request=mocked_request,
        templates_dir=Path("/mock-dir"),
        bundle_entrypoints_filepath=Path("/filepath/entrypoints.json"),
    )
    assert template_engine._bundle_urls_for("test.js") == ["/test.js", "/test2.js"]


@pytest.mark.parametrize("bundle_name", ["unknown.js", "test.txt"])
def test_bundle_urls_for_unknown_bundle(bundle_name: str):
    """
    Tests bundle_urls_for function
    When a bundle name or type cannot be found
    """
    mocked_request = MagicMock()
    mocked_request.app.state.bundle_entrypoints = {
        "test": {"js": ["test.js", "test2.js"]}
    }
    template_engine = JinjaTemplateEngine(
        request=mocked_request,
        templates_dir=Path("/mock-dir"),
        bundle_entrypoints_filepath=Path("/filepath/entrypoints.json"),
    )
    assert template_engine._bundle_urls_for(bundle_name) == []


@patch(
    "services.template_engine.jinja.Jinja2Templates.TemplateResponse",
    return_value="<h1>My test</h1>",
)
def test_render(mocked_template_response: MagicMock):
    """Tests render function"""
    template_engine = JinjaTemplateEngine(
        request="my-request",
        templates_dir=Path("/mock-dir"),
        bundle_entrypoints_filepath=Path("/filepath/entrypoints.json"),
    )
    response = template_engine.render(name="test.html", title="Just a test", user_id=12)
    assert response == "<h1>My test</h1>"
    assert mocked_template_response.call_args == call(
        request="my-request",
        name="test.html",
        context={"title": "Just a test", "user_id": 12},
    )
