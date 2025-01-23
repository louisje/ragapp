from pydantic import BaseModel

from .duckduckgo import DuckDuckGoTool
from .image_generator import ImageGeneratorTool
from .interpreter import E2BInterpreterTool
from .openapi import OpenAPITool
from .query_engine import QueryEngineTool
from .wikipedia import WikipediaTool

__all__ = [
    "DuckDuckGoTool",
    "ImageGeneratorTool",
    "E2BInterpreterTool",
    "OpenAPITool",
    "QueryEngineTool",
    "WikipediaTool",
]


TOOL_MAP = {
    "DuckDuckGo": DuckDuckGoTool,
    "ImageGenerator": ImageGeneratorTool,
    "Interpreter": E2BInterpreterTool,
    "OpenAPI": OpenAPITool,
    "QueryEngine": QueryEngineTool,
    "Wikipedia": WikipediaTool,
}


def get_tool_by_id(tool_id: str) -> BaseModel:
    if tool_id not in TOOL_MAP:
        raise ValueError(f"Tool {tool_id} not found")
    return TOOL_MAP[tool_id]
