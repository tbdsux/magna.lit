from __future__ import annotations

from typing import Any, Dict, Generic, TypeVar

T = TypeVar("T")


class BaseResponse(Generic[T]):
    def __init__(
        self, error: bool, data: T | None = None, message: str | None = None
    ) -> None:
        self.error = error
        self.data = data
        self.message = message

    def json(self) -> Dict[str, Any]:
        return {"error": self.error, "data": self.data, "message": self.message}
