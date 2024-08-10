# Copyright (c) 2024 by 董晨泉.
# All rights reserved.
#
# Licensed under the MIT License.
# See LICENSE file for more details.

import numpy as np
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d
from scipy.integrate import quad

def extract_columns(file_path, start_line=922):
    second_column_data = []
    third_last_column_data = []

    with open(file_path, 'r') as file:
        for _ in range(start_line):
            next(file)

        for line in file:
            values = line.strip().split()

            if len(values) >= 9:
                try:
                    second_column = float(values[1])
                    third_last_column = float(values[3])

                    second_column_data.append(second_column)
                    third_last_column_data.append(third_last_column)

                except ValueError:
                    continue

    return np.array(second_column_data), np.array(third_last_column_data)

def calculate_area(x, y):
    """
    计算给定浮点数 x 和 y 数据拟合曲线与 x 轴围成的面积，并可视化曲线

    参数:
    x (list 或 numpy.ndarray): x 轴数据（浮点数）
    y (list 或 numpy.ndarray): y 轴数据（浮点数）

    返回:
    float: 曲线与 x 轴围成的面积
    """
    x = np.array(x)
    y = np.array(y)

    # 对数据进行插值拟合
    f = interp1d(x, y, kind='linear')  # 这里选择线性插值，您可以根据需要选择其他插值方法

    # 定义积分函数
    def integrand(x):
        return f(x)

    # 计算积分，增加细分次数限制
    result, error = quad(integrand, np.min(x), np.max(x), limit=25000)

    return result

def save_data(path):
    x2= np.array(range(6, 20))
    y2= []

    for i in range(6, 20):
        second_column, third_last_column = extract_columns(fr'{path}_{i}.tp6', start_line=669)
        area = calculate_area(second_column, third_last_column)
        area_chuli = area * 10000
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
        second_column, third_last_column = extract_columns(fr'C:\Users\35525\Desktop\20240810\20240810\110.995305_35.406978_2020_07_01_{i}.tp6',start_line=447)
        area = calculate_area(second_column, third_last_column)
        area_chuli=area*10000
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





