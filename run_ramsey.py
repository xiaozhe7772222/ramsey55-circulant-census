#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R(5,5) 计算工具箱入口。用法: python run_ramsey.py <command> ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ramsey.cli import main
main()

