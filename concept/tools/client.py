# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : client
@Time    : 2024-12-11 18:52:54
"""
# example_client.py
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 创建服务器参数以连接到STDIO
server_params = StdioServerParameters(
    command="python",  # 可执行文件
    args=["example_server.py"],  # 可选的命令行参数
    env=None  # 可选的环境变量
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化连接
            await session.initialize()
            # 列出可用工具
            tools = await session.list_tools()
            print("Available tools:", tools)
            # 调用一个工具
            result = await session.call_tool("add", arguments={"a": 5, "b": 3})
            print("Result of add tool:", result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())