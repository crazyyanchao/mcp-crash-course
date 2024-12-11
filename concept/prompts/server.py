# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : server
@Time    : 2024-12-11 18:52:43
"""
from fastmcp import FastMCP

# 创建MCP服务器实例
mcp = FastMCP("Demo")


# 定义一个prompt
@mcp.prompt()
def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"


# 运行服务器
if __name__ == "__main__":
    mcp.run()
