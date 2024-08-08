# Copyright (c) 2024 by 董晨泉.
# All rights reserved.
#
# Licensed under the MIT License.
# See LICENSE file for more details.

import numpy as np
from scipy.interpolate import UnivariateSpline

def extract_columns(file_path, start_line=922):
    second_column_data = []
    third_last_column_data = []

    with open(file_path, 'r') as file:
        for _ in range(start_line):
            next(file)

        for line in file:
            values = line.strip().split()

            if len(values) >= 15:
                try:
                    second_column = float(values[1])
                    third_last_column = float(values[-3])

                    second_column_data.append(second_column)
                    third_last_column_data.append(third_last_column)

                except ValueError:
                    continue

    return np.array(second_column_data), np.array(third_last_column_data)

def calculate_area(x, y):
    # 对 x 进行排序并获取排序索引
    sorted_indices_x = np.argsort(x)
    sorted_x = x[sorted_indices_x]
    sorted_y = y[sorted_indices_x]

    # 找到 x 严格递增的索引
    increasing_indices_x = np.where(np.diff(sorted_x) > 0)[0]

    # 根据递增的 x 索引筛选 y
    increasing_y = sorted_y[increasing_indices_x]

    # 找到筛选后的 y 严格递增的索引
    increasing_indices_y = np.where(np.diff(increasing_y) > 0)[0]

    # 最终的严格递增的 x 和 y
    final_x = sorted_x[increasing_indices_x][increasing_indices_y]
    final_y = increasing_y[increasing_indices_y]

    # 创建样条插值函数
    spline = UnivariateSpline(final_x, final_y, s=0)

    # 计算积分区间
    x_min = np.min(final_x)
    x_max = np.max(final_x)

    # 计算曲线与 x 轴围成的面积
    area = spline.integral(x_min, x_max)

    return area
def save_data(path):
    x2= np.array(range(6, 20))
    y2= []

    for i in range(6, 20):
        second_column, third_last_column = extract_columns(fr'{path}_{i}.tp6', start_line=669)
        area = calculate_area(second_column, third_last_column)
        area_chuli = area * 3.1415926 * 2 * 10000
        y2.append(area_chuli)

    return x2,y2
def calculate_area_with_new_data(x1, y1):
    # 确保 x1 是数值型一维数组
    x1 = np.array(x1, dtype=float)
    y1 = np.array(y1, dtype=float)  # 确保 y1 也是数值型数组

    # 对 x1 进行排序并获取排序索引
    sorted_indices_x1 = np.argsort(x1)
    sorted_x1 = x1[sorted_indices_x1]
    sorted_y1 = y1[sorted_indices_x1]

    # 找到 x1 严格递增的索引
    increasing_indices_x1 = np.where(np.diff(sorted_x1) > 0)[0]

    # 根据递增的 x1 索引筛选 y1
    final_y1 = sorted_y1[increasing_indices_x1]

    # 创建样条插值函数
    spline = UnivariateSpline(sorted_x1[increasing_indices_x1], final_y1, s=0)

    # 计算积分区间
    x1_min = np.min(sorted_x1[increasing_indices_x1])
    x1_max = np.max(sorted_x1[increasing_indices_x1])

    # 计算曲线与 x 轴围成的面积
    area = spline.integral(x1_min, x1_max)

    return area

def getArea(path):
    x1, y1 = save_data(path)
    area_new = calculate_area_with_new_data(x1, y1)
    return area_new

if __name__ == '__main__':

    for i in range(6,20):
        second_column, third_last_column = extract_columns(fr'D:\Study\20240807_14\110.995305_35.406978_2020_07_01_{i}.txt',start_line=669)
        area = calculate_area(second_column, third_last_column)
        area_chuli=area*3.1415926*2*10000
        print('7 月 1 日第{}时'.format(i))
        print('x',second_column)
        print('y',third_last_column)
        print("积分结果：", area)
        print("积分处理结果：", area_chuli)
        print('============='*10)
        print('\n')
    x1,y1=save_data()
    print(x1)
    print(y1)
    area_new = calculate_area_with_new_data(x1, y1)
    print("曲线与 x 轴围成的面积:", area_new)





