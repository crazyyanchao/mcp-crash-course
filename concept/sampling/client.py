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
    command="python",  # 可执行文件
    args=["example_server.py"],  # 可选的命令行参数
    env=None  # 可选的环境变量
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化连接
            await session.initialize()
            # 这里可以添加代码来处理服务器的Sampling请求


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())