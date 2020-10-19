# WeightedNetworkNullModel（加权网络零模型）
![](https://img.shields.io/badge/python-3.8-blue) ![](https://img.shields.io/badge/version-1.0-orange)  
在加权网络中，除了结构和权重这些重要特征以外，研究者们经常利用统计量来刻画网络的非平凡特性。但是，复杂网络中计算的统计量往往只是一个绝对的数值，都是无量纲的，这对于刻画网络性质来说是不利的，因为不同规模的网络就无法直接比较性质上的差别。为了解决这一问题，我们利用构造零模型的方式来构造与原始网络具有某些相同特性的随机化副本来量化分析统计量的相对数值。

* 基于随机断边重连的加权无向网络零模型 
   * 0阶随机断边重连零模型
   * 1阶随机断边重连零模型
   * 结构随机置乱零模型
   * 弱连边1阶零模型
   * 强连边1阶零模型
   * 权重随机置乱零模型
   
* 有倾向性断边重连的加权无向网络零模型
   * 面向富人俱乐部的零模型
   * 面向强度匹配特性的零模型
   * 面向全局最优的零模型

## 样例
WeightNetworkNullModels.py中0阶随机断边重连零模型主函数
~~~python
import networkx as nx
import random
import copy
import math

#0阶随机断边重连零模型
def random_0k(G0,nspw=1,max_tries=100): 
    if nspw > max_tries:
        raise nx.NetworkXError("nspw > max_tries")
    if len(G0) < 3:
        raise nx.NetworkXError("Graph has less than three nodes")
    G = copy.deepcopy(G0)
    triesCount = 0  #总尝试次数
    brokenEdgesCount = 0 #断边次数
    edges = list(G.edges()) #获取图的所有边
    nodes = G.nodes()   #获取图的所有节点
    while brokenEdgesCount < nspw:
        b,e = random.choice(edges) #随机选择一条即将断开的边
        x,y = random.sample(nodes,2) #随机找两个节点，然后判断是否存在边
        if x not in G[y] and y not in G[x]:
            G.add_edge(x,y,weight = G[b][e]['weight'])
            G.remove_edge(b,e)
            edges.append((x,y))
            edges.remove((b,e))
            brokenEdgesCount+=1
        if triesCount >= max_tries:
            e=('Maximum number of swap attempts (%s) exceeded '%n +
            'before desired swaps achieved (%s).'%nspw)
            print (e)
            break
        triesCount +=1
    return G
~~~
NullModelCall.py中函数调用
~~~python
import networkx as nx
import WeightNetworkNullModels as ws

G0_0k = ws.random_0k(G0,nspw=2*edgesCount,max_tries=100*edgesCount) #零阶随机断边重连零模型
nx.write_edgelist(G0_0k,'WeightNetwork_0K.csv')
~~~
