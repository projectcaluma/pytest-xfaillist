from __future__ import annotations

from typing import TYPE_CHECKING

from . import item_to_test_id

if TYPE_CHECKING:
    from _pytest.config import Config
    from _pytest.python import Function
    from _pytest.runner import CallInfo

_faillist = []


def pytest_unconfigure(config: Config):
    __import__("pdb").set_trace()
    pass


def pytest_runtest_makereport(item: Function, call: CallInfo[None]):
    if call.when == "call" and call.excinfo:
        _faillist.append(item_to_test_id(item))
