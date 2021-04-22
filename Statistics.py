'''
topic:统计量的计算
des:对应《加权网络的常用统计量》论文所编写的代码
author:zwise
'''
import networkx as nx
import WeightNetworkNullModels as ws
import matplotlib.pyplot as plt
import copy
from networkx.algorithms import cluster as cls
import time


# 节点单位权重的计算
def avg_weight(G,node):
    si = G.degree(i,weight='weight')
    ki = G.degree(i)
    return si/ki

#权重分布的差异性yi
def difference_weight(G,node):
    si = G.degree(i,weight='weight')
    yi = 0.0
    for node in G[i]:
        wij = G[i][node]['weight']
        yi += (wij/si)**2
    return yi

# 无权网络匹配系数r
def matching_coefficient_r(G):
    M = len(G.edges) #M为网络中连边的总条数
    # print(G.edges)
    edges = G.edges
    kikj_sum = 0.0  #kikj相乘的和
    ki_sum_kj = 0.0 #kikj相加的和
    ki_2_kj_2_sum = 0.0 #kikj的平方和的和
    for edge in edges:
        ki = G.degree(edge[0])
        kj = G.degree(edge[1])
        kikj_sum += ki*kj
        ki_sum_kj += ki+kj
        ki_2_kj_2_sum += ki**2 + kj**2        
    M_rl = 1/M #M(图总边数)的倒数
    r = (M_rl*kikj_sum-(M_rl*0.5*ki_sum_kj)**2)/(M_rl*0.5*ki_2_kj_2_sum-(M_rl*0.5*ki_sum_kj)**2) #计算公式
    return r

# 加权匹配系数rw1
def matching_coefficient_rw1(G):
    edges = G.edges
    H = 0.0  # H为网络中所有连边的总权重
    kikjwij_sum = 0.0
    ki_sum_kj_wij = 0.0
    ki_2_kj_2_wij_sum = 0.0
    for edge in edges: #计算H
        wij = G[edge[0]][edge[1]]['weight']
        H += wij
        ki = G.degree(edge[0])
        kj = G.degree(edge[1])
        kikjwij_sum += ki*kj*wij
        ki_sum_kj_wij += wij*(ki+kj)
        ki_2_kj_2_wij_sum += (ki**2+kj**2)*wij
    print(kikjwij_sum,ki_sum_kj_wij,ki_2_kj_2_wij_sum)
    H_rl = 1/H  # H(总权重)的倒数
    rw1 = (H_rl*kikjwij_sum-(H_rl*0.5*ki_sum_kj_wij)**2)/(H_rl*0.5*ki_2_kj_2_wij_sum-(H_rl*0.5*ki_sum_kj_wij)**2)
    return rw1

# 加权匹配系数rw2(基于节点强度匹配特征)
def matching_coefficient_rw2(G):
    edges = G.edges
    M = len(G.edges)
    H = 0.0  # H为网络中所有连边的总权重
    sisj_sum = 0.0
    si_sum_sj = 0.0
    si_2_sj_2_sum = 0.0
    for edge in edges: #计算H
        si = G.degree(edge[0],weight='weight')
        sj = G.degree(edge[1],weight='weight')
        sisj_sum += si*sj
        si_sum_sj += (si+sj)
        si_2_sj_2_sum += (si**2+sj**2)

    M_rl = 1/M  # H(总权重)的倒数
    rw2 = (M_rl*sisj_sum-(M_rl*0.5*si_sum_sj)**2)/(M_rl*0.5*si_2_sj_2_sum-(M_rl*0.5*si_sum_sj)**2)
    return rw2

# 邻居节点的平均度(衡量匹配特性)
def avg_neigh_ki(G,i):
    ki = G.degree(i)
    kj_sum = 0.0
    for j in G[i]:
        kj_sum += G.degree(j)
    knni = kj_sum/ki
    return knni

# 最近邻节点权重的平均
def avg_neigh_kwi(G,i):
    si = G.degree(i,weight='weight')
    wijkj_sum = 0.0
    for j in G[i]:
        wij = G[i][j]['weight']
        kj = G.degree(j)
        wijkj_sum += wij*kj
    kwnni = wijkj_sum/si
    return kwnni

# 最短路径长度network有具体的方法https://www.osgeo.cn/networkx/reference/algorithms/shortest_paths.html
    
# 富人俱乐部系数 networkx有自带的求富人俱乐部系数的函数，它返回的是k取所有可能值的情况
def rich_club_coefficient(G,k):
    """
    Parameters
    ----------
    G : 网络图
    k : 度。节点度大于等于k的称为富节点，否则为非富节点
    """
    edges = list(G.edges())
    nodes = list(G.nodes())
    nodesk = [i for i in nodes if G.degree(i) >= k]
    Ek = len([e for e in edges if e[0] in nodesk and e[1] in nodesk])
    Nk = len(nodesk)
    if (Nk*(Nk-1)) == 0:
        raise nx.NetworkXError("分母为零")
    print(Ek)
    print(Nk)
    return (2*Ek)/(Nk*(Nk-1))


###xxx
#加权网络富人俱乐部系数
def rich_club_coefficient_weight(G,r):
    """
    用于加权网络判断图是否有富人俱乐部效应
    Parameters
    ----------
    G:网络图
    r:强度值。节点强度大于等于r的称为富节点，否则为非富节点
    Returns float
    -------
    None.
    """
    Wr = 0
    Wl_rank = 0
    nodes = list(G.nodes())
    edges = list(G.edges(data=True))
    importance_nodes = [i for i in nodes if G.degree(i,weight = 'weight') >= r]
    importance_edges = [e for e in edges if e[0] in importance_nodes and e[1] in importance_nodes]
    for e in importance_edges:
        Wr += G[e[0]][e[1]]['weight']
    # for i in edges:
        # print(i[2]['weight'])
    weight = []
    for i in edges:
        weight.append(i[2]['weight'])
    weight.sort(reverse=True)
    for i in range(len(importance_edges)):
        Wl_rank += weight[i]
    return Wr/Wl_rank
    
    