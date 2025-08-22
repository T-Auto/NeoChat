# 环境变量示例（请手动创建 .env 并根据需要填写）

请在项目根目录创建 `.env` 文件，内容参考如下：

```
# DeepSeek API Key
API_KEY=sk-xxxx

# 可选：在日志或界面中展示的AI名称
AI_NAME=Neo

# 可选：全局系统提示词
SYSTEM_PROMPT=你是一个优秀的AI DM。
```

注意：此文件仅示例，不会被程序自动读取为配置。程序通过 `python-dotenv` 自动加载根目录 `.env`。

