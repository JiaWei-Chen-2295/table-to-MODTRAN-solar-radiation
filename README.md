## 项目概述

该项目旨在通过自动化的方式利用 MODTRAN 模型计算特定条件下（如大气条件、地理位置等）的太阳辐射值。具体来说，用户需要准备一个包含必要参数的Excel表格，然后通过一系列脚本自动完成数据处理、模型调用以及结果输出。

## 项目环境准备

1. 运行前务必确认你的 Python 版本是 **3.12.XX** 及以上

2. 将你的命令行使用 `cd` 命令定位到 `Mod5.2.1.0.exe` 同级目录下。

   ```bash
   cd path/to/Modtran5    
   ```

2. 使用如下命令拉取项目到本地。
   
   ```bash
   git clone https://github.com/JiaWei-Chen-2295/table-to-MODTRAN-solar-radiation.git
   ```
   
3. 将拉取下来的文件夹 `table-to-MODTRAN-solar-radiation-master` 中的文件移动到与 `Mod5.2.1.0.exe` 同级目录下。

4. 将数据按照 `数据.xlsx` 的表格标题写好参数，务必将名字修改为 `数据.xlsx` 。

5. 运行 `setup.bat` 脚本。 这个脚本将帮助你安装运行环境和计算结果。

6. 当 `setup.bat` 脚本提示 `把所有数字文件夹下的bat脚本启动吧` 时，就会创建好文件夹（如 `1/`, `2/`, ...）。

7. 手动进入这些文件夹并运行其中的 `RunRunRunRunRunRunRunRun.bat` 批处理文件。

### 查看结果
  - 每个文件夹下将会生成一个 Excel 表格（如 `1_1.xlsx`, `2_2.xlsx`, ...），其中包含了对应案例的计算结果。

### 目录结构
```plaintext
project_directory/
│
├── 数据.xlsx
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
- **数据.xlsx**: 包含了用于计算太阳辐射值的所有必要参数的Excel表格。
- **setup.py**: 配置文件，用于设置运行参数，如`run_num`，即需要运行的案例数量。
- **setup.bat**: 执行脚本，用于初始化项目和创建必要的文件夹。
- **1/, 2/, ...**: 每个文件夹对应一个具体的案例，里面包含了用于调用MODTRAN模型的批处理文件以及最终的输出文件。
  - **RunRunRunRunRunRunRunRun.bat**: 批处理文件，用于运行MODTRAN模型。
  - **1_1.xlsx, 2_2.xlsx, ...**: Excel表格，存储了每个案例的计算结果。

### 注意事项
- **环境要求**: 该项目已经包含了所有必要的 Python 环境配置的脚本，因此不需要用户自行安装 Python 环境或依赖库。按照要求运行脚本即可。
- **IDE使用**: 不建议在 IDE（如 PyCharm）中直接运行该项目，因为它是基于批处理脚本设计的，更适合在命令行环境中运行。

## 贡献者
- **指导者**:
  - 张宪哲老师 
  - 张波学长
- **主要开发者**:
  - 陈佳玮 ([JavierChen](https://github.com/JiaWei-Chen-2295))
  - 董晨泉 ([ChenQuanDong](https://github.com/DCQ200849))

- **贡献者**:
- **感谢**:
