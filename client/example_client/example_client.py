# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : example-client
@Time    : 2024-12-11 18:26:57
"""
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",  # Executable
    args=[
        "--directory",
        r"D:\workspace\mcp\mcp-crash-course\server\example_server",
        "run",
        "sse.py"
    ],  # Optional command line arguments
    env=None  # Optional environment variables
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # The example server only supports prompt primitives:

            # List available prompts
            prompts = await session.list_prompts()

            # Get a prompt
            prompt = await session.get_prompt("example-prompt", arguments={"arg1": "value"})

            # Other example calls include:

            # List available resources
            # resources = await session.list_resources()

            # List available tools
            # tools = await session.list_tools()

            # Read a resource
            # resource = await session.read_resource("file://some/path")

            # Call a tool
            # result = await session.call_tool("tool-name", arguments={"arg1": "value"})


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())