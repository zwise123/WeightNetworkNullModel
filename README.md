# 加权无向网络零模型
![](https://img.shields.io/badge/python-3.8-blue) ![](https://img.shields.io/badge/version-1.0-orange) ![](https://img.shields.io/badge/networkx-2.5-yellow) ![](https://img.shields.io/badge/numpy-1.19.1-%234169E1)  
本项目主要介绍加权无向网络零模型，主要有基于随机断边重连的加权无向网络零模型、有倾向性断边重连的加权无向网络零模型；其中基于随机断边重连的加权无向网络零模型包含0阶随机断边重连零模型、1阶随机断边重连零模型、结构随机置乱零模型、弱连边1阶零模型、强连边1阶零模型、权重随机置乱零模型，有倾向性断边重连的加权无向网络零模型包含面向富人俱乐部的零模型、面向强度匹配特性的零模型、面向全局最优的零模型。
## 理论介绍
具体理论介绍详情查看Algorithm_description.pdf文件。
## 代码使用
* 环境搭建  
   *  networkx库
   *  numpy库
   *  random库
   *  copy库
   *  math库
   
* 零模型函数（WeightNetworkNullModels.py文件）
   *  random_0k-0阶随机断边重连零模型
   *  random_1k-1阶随机断边重连零模型
   *  structure_random-结构随机置乱零模型
   *  weakEdge_1k-弱连边1阶零模型
   *  strong_1k-强连边1阶零模型
   *  weight_random-权重随机置乱零模型
   *  rich_club_break-面向富人俱乐部的零模型
   *  assort_mixing、disassort_mixing-面向强度匹配特性的零模型   


在NullModel_demo.ipynb文件中有整个程序的运行演示以及说明。

## 加权统计量
  加权统计量计算在Statistics.py文件中
