# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : server
@Time    : 2024-12-11 18:52:43
"""
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types

# 创建服务器实例
server = Server("example-server")


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    # 访问当前请求上下文
    context = server.request_context
    # 使用会话从客户端的LLM进行采样
    result = await context.session.create_message(
        messages=[
            types.SamplingMessage(
                role="user",
                content=types.TextContent(
                    type="text",
                    text="Analyze this data: " + json.dumps(arguments)
                )
            )
        ],
        max_tokens=100
    )
    return [types.TextContent(type="text", text=result.content.text)]


async def run():
    # 以STDIO方式运行服务器
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                )
            )
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
