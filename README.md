## 项目概述

该项目旨在通过自动化的方式利用MODTRAN模型计算特定条件下（如大气条件、地理位置等）的太阳辐射值。具体来说，用户需要准备一个包含必要参数的Excel表格，然后通过一系列脚本自动完成数据处理、模型调用以及结果输出。

### 使用指南

#### 准备输入数据
1. 使用提供的 `data.xlsx` 文件，按照给定的表头填写相应的参数。
   - 参数包括但不限于地理位置、日期、时间、大气条件等。

#### 调整配置
1. 打开 `setup.py` 文件，根据你的计算机配置调整 `run_num` 变量的值。
   - `run_num` 代表需要运行的案例数量，即最终将创建多少个文件夹。

#### 初始化项目
1. 运行 `setup.bat` 脚本。
   - 这一步会根据 `run_num` 的值创建相应数量的文件夹（例如 `1`, `2`, ...）。

#### 运行案例
1. 对于每一个创建的文件夹（如 `1/`, `2/`, ...），手动进入该文件夹并运行其中的 `RunRunRunRunRunRunRunRun.bat` 批处理文件。
   - 这个批处理文件会自动调用 MODTRAN 模型并计算指定案例的太阳辐射值。

#### 查看结果
  - 每个文件夹下将会生成一个 Excel 表格（如 `1_1.xlsx`, `2_2.xlsx`, ...），其中包含了对应案例的计算结果。

### 目录结构
```plaintext
project_directory/
│
├── data.xlsx
├── setup.py
├── setup.bat
├── 1/
│   └── RunRunRunRunRunRunRunRun.bat
│   └── 1_1.xlsx
├── 2/
│   └── RunRunRunRunRunRunRunRun.bat
│   └── 2_2.xlsx
│
└── ...
```

### 文件说明
- **data.xlsx**: 包含了用于计算太阳辐射值的所有必要参数的Excel表格。
- **setup.py**: 配置文件，用于设置运行参数，如`run_num`，即需要运行的案例数量。
- **setup.bat**: 执行脚本，用于初始化项目和创建必要的文件夹。
- **1/, 2/, ...**: 每个文件夹对应一个具体的案例，里面包含了用于调用MODTRAN模型的批处理文件以及最终的输出文件。
  - **RunRunRunRunRunRunRunRun.bat**: 批处理文件，用于运行MODTRAN模型。
  - **1_1.xlsx, 2_2.xlsx, ...**: Excel表格，存储了每个案例的计算结果。

### 注意事项
- **环境要求**: 该项目已经包含了所有必要的 Python 环境配置，因此不需要用户自行安装 Python 环境或依赖库。
- **IDE使用**: 不建议在 IDE（如 PyCharm）中直接运行该项目，因为它是基于批处理脚本设计的，更适合在命令行环境中运行。