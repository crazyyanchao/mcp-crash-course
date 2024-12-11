# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : server
@Time    : 2024-12-11 18:52:43
"""
from mcp.server import Server
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types

# 创建服务器实例
server = Server("example-server")


# 列出可用资源
@server.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    return [
        types.Resource(
            uri="file:///logs/app.log",
            name="Application Logs",
            mimeType="text/plain"
        )
    ]


# 读取资源内容
@server.read_resource()
async def handle_read_resource(uri: str) -> types.ReadResourceResult:
    if uri == "file:///logs/app.log":
        with open("/path/to/your/logs/app.log", "r") as file:
            log_contents = file.read()
        return types.ReadResourceResult(
            contents=[
                types.ResourceContent(
                    uri=uri,
                    mimeType="text/plain",
                    text=log_contents
                )
            ]
        )
    raise ValueError("Resource not found")


async def run():
    # 以STDIO方式运行服务器
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example",
                server_version="0.1.0",
                capabilities=server.get_capabilities()
            )
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
