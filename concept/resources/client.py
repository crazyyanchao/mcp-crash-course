# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : client
@Time    : 2024-12-11 18:52:54
"""
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 创建服务器参数以连接到STDIO
server_params = StdioServerParameters(
    command="uv",
    args=["run", "server.py"],  # 可选的命令行参数
    env=None  # 可选的环境变量
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化连接
            await session.initialize()
            # 列出可用资源
            resources = await session.list_resources()
            print("Available resources:", resources)

            # 读取特定资源
            resource_content = await session.read_resource("file:///logs/app.log")
            print("Resource content:", resource_content)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
