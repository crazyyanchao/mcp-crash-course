# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : client
@Time    : 2024-12-11 18:52:54
"""
from prompt_engine.code_engine import CodeEngine, PythonCodeEngineConfig

# 定义prompt的描述
description = "Natural Language Commands to Python Code. The code should print the result of the command."

# 定义NL->Code交互的例子
examples = [
    {"input": "what's 10 plus 18", "output": "print(10 + 18)"},
    {"input": "what's 10 times 18", "output": "print(10 * 18)"}
]

# 创建CodeEngine实例
code_engine = CodeEngine(description=description, examples=examples)

# 构建prompt
query = "What's 1018 times the ninth power of four?"
prompt = code_engine.build_prompt(query)
print(prompt)