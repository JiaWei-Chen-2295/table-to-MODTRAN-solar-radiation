# Copyright (c) 2024 by JavierChen.
# All rights reserved.
#
# Licensed under the MIT License.
# See LICENSE file for more details.
import os
import time

import pandas as pd
import shutil
from glob import glob
import threading
import subprocess
import concurrent.futures

def split_excel(input_path, num, output_prefix=''):
    """
    这段代码会将一个 Excel 文件按照指定的 num_parts 分割成多个 Excel 文件，
    每个文件都保留了原始文件的第一行作为表头，并且文件名为
    output_part_1.xlsx, output_part_2.xlsx, 等等。
    """
    # 读取 Excel 文件
    df = pd.read_excel(input_path)

    # 获取原始的列名（表头）
    header = df.columns.tolist()

    # 计算每部分应该有多少行
    chunk_size = len(df) // num
    if chunk_size == 0:
        raise ValueError("The number of parts is too large for the data size.")

    # 创建每部分的数据框，并保存为新的 Excel 文件
    for i in range(num):
        start_row = i * chunk_size
        end_row = (i + 1) * chunk_size if i < num - 1 else None

        # 选择相应的行
        part_df = df.iloc[start_row:end_row]

        # 如果这是第一个部分，则直接保存
        if i == 0:
            part_df.to_excel(f'{output_prefix}{i + 1}.xlsx', index=False)
        else:
            # 使用 pandas 的 `to_excel` 函数直接插入表头
            with pd.ExcelWriter(f'{output_prefix}{i + 1}.xlsx', engine='openpyxl') as writer:
                part_df.to_excel(writer, startrow=0, header=True, index=False)


def copy_non_excel_files_and_dirs_to_new_folders(num):
    # 当前目录
    current_dir = os.getcwd()

    # 获取当前目录下的所有文件和文件夹
    all_files_and_dirs = glob(os.path.join(current_dir, '*'))

    # 筛选出非 Excel 文件和文件夹
    non_excel_files_and_dirs = [item for item in all_files_and_dirs if not item.endswith(('.xlsx', '.xls'))]

    # 根据 num 创建相应数量的新文件夹，并复制文件和文件夹
    for folder_num in range(1, num + 1):
        new_folder_name = str(folder_num)
        new_folder_path = os.path.join(current_dir, new_folder_name)

        # 创建新文件夹
        os.makedirs(new_folder_path, exist_ok=True)

        # 复制非 Excel 文件到新文件夹
        for item in non_excel_files_and_dirs:
            if os.path.isfile(item):
                shutil.copy(item, new_folder_path)
            elif os.path.isdir(item):
                # 复制文件夹及其内容到新文件夹
                dest_dir = os.path.join(new_folder_path, os.path.basename(item))
                shutil.copytree(item, dest_dir)



def move_excel_files_to_matching_folders():
    # 当前目录
    current_dir = os.getcwd()

    # 获取当前目录下的所有 Excel 文件
    excel_files = glob(os.path.join(current_dir, '*.xlsx')) + glob(os.path.join(current_dir, '*.xls'))

    # 移动 Excel 文件到相应的文件夹
    for excel_file in excel_files:
        # 获取文件名（不包括扩展名）
        filename = os.path.splitext(os.path.basename(excel_file))[0]

        # 构建目标文件夹路径
        target_folder = os.path.join(current_dir, filename)

        # 检查文件夹是否存在
        if os.path.exists(target_folder) and os.path.isdir(target_folder):
            # 构建目标文件路径
            target_file = os.path.join(target_folder, os.path.basename(excel_file))

            # 移动文件
            shutil.move(excel_file, target_file)
            print(f"Moved {excel_file} to {target_folder}")

def copy_folder_contents(source_folder, target_folder):
    """复制源文件夹的内容到目标文件夹"""
    # 使用 copytree 函数复制整个文件夹内容
    shutil.copytree(source_folder, target_folder)

if __name__ == '__main__':
    start_time = time.time()

    run_num = 4
    path = "数据.xlsx"
    split_excel(path, run_num)
    copy_non_excel_files_and_dirs_to_new_folders(run_num)
    for _ in range(1, run_num + 1):
        target_folder = os.path.join(os.getcwd(), str(_))  # 构造目标文件夹的完整路径
    
        # 如果目标文件夹不存在，则创建它
        if not os.path.exists(target_folder):
            exit(404)
    
        # 复制文件夹内容
        copy_folder_contents(".venv", target_folder + "\.venv")
    move_excel_files_to_matching_folders()
    print("现在，该你动了")
    print("把所有数字文件夹下的bat脚本启动吧")
    print("双击他们的RunRunRun..bat")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(print(f"代码执行耗时: {elapsed_time:.6f} 秒"))


