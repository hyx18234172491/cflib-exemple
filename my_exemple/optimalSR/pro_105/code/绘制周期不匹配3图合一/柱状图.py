import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from my_exemple.optimalSR.pro_105.code.a_50ms_70ms.distribution_up import getPlotData as Data_50ms_70ms_up
from my_exemple.optimalSR.pro_105.code.a_50ms_70ms.distribution_down import getPlotData as Data_50ms_70ms_down

from my_exemple.optimalSR.pro_105.code.a_40ms_70ms.distribution_up import getPlotData as Data_40ms_70ms_up
from my_exemple.optimalSR.pro_105.code.a_40ms_70ms.distribution_down import getPlotData as Data_40ms_70ms_down

from my_exemple.optimalSR.pro_105.code.a_30ms_70ms.distribution_up import getPlotData as Data_30ms_70ms_up
from my_exemple.optimalSR.pro_105.code.a_30ms_70ms.distribution_down import getPlotData as Data_30ms_70ms_down

# 创建三个不同的错误数据集
error_data_50_70_up = Data_50ms_70ms_up()
error_data_50_70_down = Data_50ms_70ms_down()

error_data_40_70_up = Data_40ms_70ms_up()
error_data_40_70_down = Data_40ms_70ms_down()

error_data_30_70_up = Data_30ms_70ms_up()
error_data_30_70_down = Data_30ms_70ms_down()

error_datasets = [
    Data_50ms_70ms_up(),

    Data_40ms_70ms_up(),
    Data_30ms_70ms_up(),
    Data_50ms_70ms_down(),
    Data_40ms_70ms_down(),

    Data_30ms_70ms_down()
]

# 创建子图
fig, axes = plt.subplots(2, 3, figsize=(10, 6))
# 绘制每个子图
for i, ax in enumerate(axes.flat):
    if i < len(error_datasets):
        sns.histplot(error_datasets[i]['error'], kde=True, binwidth=1, ax=ax)
        mean = error_datasets[i]['error'].mean()
        std = error_datasets[i]['error'].std()

        ax.text(0.5, 0.95, f'$\mu={mean:.2f}$\n$\sigma={std:.2f}$',
                verticalalignment='top', horizontalalignment='center',
                transform=ax.transAxes, fontsize=20, bbox=dict(facecolor='white', alpha=0.8))
        # # 获取当前的x轴范围
        # xlim = ax.get_xlim()
        # # 生成四个均匀分布的刻度位置
        # x_ticks = np.linspace(xlim[0], xlim[1], 4)
        # ax.set_xticks(x_ticks)
        ax.set_xlabel('')  # 移除横坐标标签
        ax.set_ylabel('')  # 移除纵坐标标签
    else:
        ax.axis('off')  # 如果没有更多的数据集，隐藏多余的子图

# 在每列的最上方添加标注
fig.text(0.23, 0.94, '50ms-70ms', ha='center', fontsize=20)
fig.text(0.54, 0.94, '40ms-70ms', ha='center', fontsize=20)
fig.text(0.86, 0.94, '30ms-70ms', ha='center', fontsize=20)

fig.text(0.025, 0.70, 'Moving away', va='center', rotation='vertical', fontsize=20)
fig.text(0.025, 0.26, 'Moving towards', va='center', rotation='vertical', fontsize=20)
plt.tight_layout(rect=[0.05, 0, 1, 0.95])
plt.show()
