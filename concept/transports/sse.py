# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : sse
@Time    : 2024-12-11 18:52:43
"""
# 导入MCP库
from mcp.server import Server
from mcp.server.sse import SSEServerTransport

# 创建MCP服务器实例
server = Server("example-server")


# 定义资源、工具或提示的处理函数
# 例如，定义一个简单的资源
@server.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"


# 使用SSE传输运行服务器
if __name__ == "__main__":
    # 假设你有一个Flask应用，可以这样集成SSE传输
    from flask import Flask, request, Response

    app = Flask(__name__)


    @app.route('/mcp', methods=['POST'])
    def mcp_endpoint():
        transport = SSEServerTransport(request, None)
        return Response(transport.handle(), content_type='text/event-stream')


    # 运行Flask应用
    app.run(debug=True)
