@echo off

python -m venv .venv

call .venv\Scripts\activate

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

echo Virtual environment created and dependencies installed.

.venv\Scripts\python.exe setup.py

pause