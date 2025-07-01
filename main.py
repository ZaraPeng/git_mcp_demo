# main.py
from mcp.server.fastmcp import FastMCP

# 创建MCP服务器
mcp = FastMCP("Git MCP Demo")


# 添加一个简单的工具
@mcp.tool()
def hello_git(name: str) -> str:
    """返回一个Git相关的问候"""
    return f"Hello {name}, welcome to Git MCP integration!"


# 添加一个资源
@mcp.resource("git_info/{repo_name}")
def get_git_info(repo_name: str) -> dict:
    """获取Git仓库信息"""
    return {
        "repo_name": repo_name,
        "status": "initialized",
        "description": "A demo repository for Git MCP integration"
    }


if __name__ == "__main__":
    mcp.settings.host = "0.0.0.0"
    mcp.run(transport='sse')