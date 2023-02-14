from __future__ import annotations

from typing import Any, Dict, List


class BaseResponse:
    def __init__(
        self,
        error: bool,
        data: List[Dict[str, Any]] | Dict[str, Any] | None = None,
        message: str | None = None
    ) -> None:
        self.error = error
        self.data = data
        self.message = message

    def json(self) -> Dict[str, Any]:
        return {
            "error": self.error,
            "data": self.data,
            "message": self.message
        }
