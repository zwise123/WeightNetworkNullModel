# WeightNetworkNullModel（加权网络零模型）
此项目研究的是复杂网络中的加权网络零模型，算法思想基于许小可老师的《网络零模型构造及应用》，基于刘波师兄给的代码，在师兄的代码上进行改进重构
其中NullModelCall.py是函数调用代码，WeightNetworkNullModels.py包含加权网络零模型功能
## 基于随机断边重连的加权无向网络零模型
### 0阶随机断边重连零模型
改变了原始网络的度分布和权重分布，WeightNetWorkNullModels.py中random_0k就为0阶随机断边重连零模型的代码函数。
### 1阶随机断边重连零模型
改变了原始网络的权重分布，WeightNetWorkNullModels.py中random_1k为1阶随机断边重连零模型的代码函数。
### 结构随机置乱零模型
仅仅改变了原始网络的拓扑结构，WeightNetWorkNullModels.py中structure_random为结构随机置乱零模型代码函数。
### 弱连边1阶零模型
WeightNetWorkNullModels.py中weakEdge_1k为弱连边1阶零模型代码函数。
### 强连边1阶零模型
WeightNetWorkNullModels.py中strong_1k为强连边1阶零模型代码函数。
### 权重随机置乱零模型
WeightNetWorkNullModels.py中weight_random为权重随机置乱零模型代码函数。
## 有倾向性断边重连的加权无向网络零模型
### 面向富人俱乐部的零模型
WeightNetWorkNullModels.py中，rich_club，rich_club_break为面向富人俱乐部的零模型代码函数
### 面向强度匹配特性的零模型
WeightNetWorkNullModels.py中，assort_mixing（强度大的节点和强度大的节点相连），dissort_mixing（强度大的节点和强度小的节点相连）为面向强度匹配特性的零模型。
### 面向全局最优的零模型
