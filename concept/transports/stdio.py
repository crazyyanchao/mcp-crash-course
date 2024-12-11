# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : stdio
@Time    : 2024-12-11 18:52:54
"""
# 导入MCP库
import mcp.server.stdio

# 创建MCP服务器实例
from mcp.server import Server

server = Server("example-server")


# 定义资源、工具或提示的处理函数
# 例如，定义一个简单的工具
@server.tool()
def add(a: int, b: int) -> int:
    return a + b


# 使用stdio传输运行服务器
if __name__ == "__main__":
    mcp.server.stdio.run(server)