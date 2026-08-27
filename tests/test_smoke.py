"""轻量冒烟测试（smoke test）。

背景：funmcp 仓库当前源码只有两个空的 __init__.py 文件
(src/funmcp/__init__.py、src/funmcp/mcp/__init__.py)，没有任何类/函数/
MCP server 实现，pyproject.toml 里 dependencies 也是空列表（未依赖官方
`mcp` PyPI 包）。README 只是关于 Model Context Protocol 的介绍性文档和
外部链接列表。

因此这里没有可供实例化/调用的公共类、函数或 MCP tool 定义，也没有
[project.scripts] CLI 入口。冒烟测试的范围收窄为：确认包能被正确安装、
顶层包及子包可以被导入，并显式记录“尚无实现”这一事实，避免后续误以为
已有可用功能。
"""

import importlib

import pytest


def test_import_top_level_package():
    """顶层包 funmcp 必须能被导入。"""
    module = importlib.import_module("funmcp")
    assert module is not None


def test_import_mcp_subpackage():
    """子包 funmcp.mcp 必须能被导入。"""
    module = importlib.import_module("funmcp.mcp")
    assert module is not None


def test_package_has_no_public_api_yet():
    """记录当前状态：包内没有任何公开的类/函数/常量。

    一旦仓库补上真正的 MCP server 实现，这个测试会失败，
    提醒需要同步替换/补充为针对真实实现的冒烟测试。
    """
    import funmcp
    import funmcp.mcp

    # "mcp" 本身是子包，导入后会挂在 funmcp 上，属预期内成员，需排除。
    public_top_level = [
        name for name in dir(funmcp) if not name.startswith("_") and name != "mcp"
    ]
    public_mcp = [name for name in dir(funmcp.mcp) if not name.startswith("_")]

    assert public_top_level == [], (
        f"funmcp 顶层包出现了新的公开成员 {public_top_level}，"
        "说明已有实现，请补充针对性的冒烟测试。"
    )
    assert public_mcp == [], (
        f"funmcp.mcp 子包出现了新的公开成员 {public_mcp}，"
        "说明已有实现，请补充针对性的冒烟测试。"
    )


def test_mcp_server_not_implemented_yet():
    """没有可实例化的 MCP server / tool 定义，无法做进一步冒烟测试。

    真实凭据/网络也无从谈起——因为连业务代码都还不存在。
    """
    pytest.skip("funmcp 当前仅有空的 __init__.py，尚无 MCP server 实现，跳过")
