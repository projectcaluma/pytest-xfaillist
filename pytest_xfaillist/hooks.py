from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _pytest.config import Config
    from _pytest.config.argparsing import Parser


def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        "--generate-xfaillist", action="store_true", help="Generate xfail.list"
    )


def pytest_configure(config: Config):
    if config.option.generate_xfaillist:
        config.pluginmanager.import_plugin("pytest_xfaillist.generate")
