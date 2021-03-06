from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _pytest.python import Function


def item_to_test_id(item: Function) -> str:
    function = item.function
    return f"{function.__module__}.{function.__name__}"
