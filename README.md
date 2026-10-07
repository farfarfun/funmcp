# funmcp

MCP（Model Context Protocol）资料收集仓库：汇总 mcphub、smithery、mcp.so 等 MCP 服务器注册站点与中文文档链接。

## 安装

```bash
uv add funmcp
```

## 当前状态

本仓库当前仅是一个已发布到 PyPI 的空骨架包（`src/funmcp/`、`src/funmcp/mcp/` 均只有空的 `__init__.py`），尚无可调用的公开 API 或 MCP server 实现，暂无可运行示例。导入方式：

```python
import funmcp
```

## 开发与发布

```bash
uv sync --group dev
uv run ruff check --fix . && uv run ruff format .
uv run pytest
```

发布由维护者使用 `uv run funbuild build --version <版本号> "<提交信息>"` 完成；该流程负责版本递增、构建、安装校验、发布与打 tag。

下方内容为 MCP 协议本身的背景资料与相关站点链接，供了解 MCP 生态使用。

# MCP简介

[MCP](https://mcp-docs.cn/introduction)(Model Context Protocol)是一个[开放协议](https://modelcontextprotocol.io/introduction)，它为应用程序向 LLM 提供上下文的方式进行了标准化。你可以将 MCP 想象成 AI 应用程序的 USB-C 接口。就像 USB-C 为设备连接各种外设和配件提供了标准化的方式一样，MCP 为 AI 模型连接各种数据源和工具提供了标准化的接口。



# MCP SERVER

|序号|链接|说明|  
|:-:|:-:|:-:|
|1|[mcphub](https://mcphub.io/registry)||
|2|[opentools](https://opentools.com/registry)||
|3|[mcphunt](https://mcphunt.com/zh)||
|4|[cursor directory](https://cursor.directory/mcp)||
|5|[pulsemcp](https://www.pulsemcp.com/servers)||
|6|[smithery](https://smithery.ai/)||
|7|[claude](https://modelcontextprotocol.io/examples)||
|8|[mcp.so](https://mcp.so/servers)||


# 相关链接
* [mcp-docs](https://mcp-docs.cn/introduction)
* [Mcp 相关的热门 GitHub AI项目仓库](https://www.aibase.com/zh/repos/topic/mcp)

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
