@echo off


:: 创建虚拟环境
python -m venv .venv

:: 激活虚拟环境
call .venv\Scripts\activate

:: 安装 requirements.txt 中的依赖
pip install -r requirements.txt

:: 输出确认消息
echo Virtual environment created and dependencies installed.

.venv\Scripts\python.exe setup.py

pause