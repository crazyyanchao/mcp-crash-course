# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : server
@Time    : 2024-12-11 18:52:43
"""
# demo.py
from fastmcp import FastMCP

# 创建一个MCP服务器
mcp = FastMCP("Demo 🚀")


# 定义一个工具（tool）
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 定义一个动态资源
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# 运行服务器
if __name__ == "__main__":
    mcp.run()
