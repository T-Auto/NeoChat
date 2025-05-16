# NeoChat
对实现AI永久记忆的探索。

## 简介

A simple and pure AI conversation platform based on command-line format / 返璞归真的，基于命令行形式的AI对话平台

## 特性

- 使用RAG向量库记忆系统，拥有数万条上下文的记忆，且不会耗费太多Token。

## 用法

- 依照requirements创建.venv虚拟环境
- 打开.env.example，修改系统提示词和你的apikey，并重命名为.env
- 对话历史储存在Dialogue_history中。
- chroma_db_store是RAG生成的历史对话向量库，删除后可自动创建。
