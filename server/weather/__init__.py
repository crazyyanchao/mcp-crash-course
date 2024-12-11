# -*- coding: utf-8 -*-
"""
@Author  : Yc-Ma
@Desc    : INIT
@Time    : 2024-12-11 17:21:13
"""
from . import server
import asyncio


def main():
    """Main entry point for the package."""
    asyncio.run(server.main())


# Optionally expose other important items at package level
__all__ = ['main', 'server']
