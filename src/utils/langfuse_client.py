import os
from typing import Any


def run_config() -> dict[str, Any]:
    if not os.getenv("LANGFUSE_PUBLIC_KEY") or not os.getenv("LANGFUSE_SECRET_KEY"):
        return {}

    from langfuse.langchain import CallbackHandler

    return {"callbacks": [CallbackHandler()]}
