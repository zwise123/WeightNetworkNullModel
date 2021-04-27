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
import itertools
import numpy as np
import math


# 1节点单位权重的计算
def avg_weight(G,i,weight = 'weight'):
    si = G.degree(i,weight = weight)
    ki = G.degree(i)
    return si/ki

#2权重分布的差异性yi
def difference_weight(G,i):
    si = G.degree(i,weight='weight')
    yi = 0.0
    for node in G[i]:
        wij = G[i][node]['weight']
        yi += (wij/si)**2
    return yi

# 3无权网络匹配系数r
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

# 4加权匹配系数rw1
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

# 5加权匹配系数rw2(基于节点强度匹配特征)
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

# 6邻居节点的平均度(衡量匹配特性)
def avg_neigh_ki(G,i):
    ki = G.degree(i)
    kj_sum = 0.0
    for j in G[i]:
        kj_sum += G.degree(j)
    knni = kj_sum/ki
    return knni

# 7最近邻节点权重的平均
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
    
# 8富人俱乐部系数 networkx有自带的求富人俱乐部系数的函数，它返回的是k取所有可能值的情况
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
    return (2*Ek)/(Nk*(Nk-1))


###xxx
#9加权网络富人俱乐部系数
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
    importa''nce_nodes = [i for i in nodes if G.degree(i,weight = 'weight') >= r]
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

#----------------------------------聚类系数-------------------------------------
#10计算关联三点组数量
def associate_three_group(G):
    nodes = list(G.nodes())
    guanlian = 0
    for u,v in itertools.combinations(nodes, 2):
        u_friends = list(G.neighbors(u))
        v_friends = list(G.neighbors(v))
        if (u_friends == []) or (v_friends == []):
            guanlian += 0
        else:
            guanlian += len(set(u_friends) & set(v_friends))
    return guanlian

#11无权重网络全局聚类系数
def global_clustering_unweight(G):
    atg = associate_three_group(G) #计算关联三点组数量作为分母
    triangle = 0
    #计算三角形数量
    for i in nx.triangles(G).values():
        triangle += i
    return triangle/atg



#12加权网络全局聚类系数
def global_clustering_weight(G):
    nodes = list(G.nodes())
    edges = list(G.edges())
    #计算构成三角形的总权重
    weight_triangle = 0
    weight_triangle_n = 0
    weight_three = 0
    weight_three_n = 0
    three_point = set() #存放计算过的三角形
    for u,v in itertools.combinations(nodes,2):
        #计算闭合三角形的总权重
        if (u,v) in edges:
            u_friends = list(G.neighbors(u))
            v_friends = list(G.neighbors(v))
            cn = list(set(u_friends) & set(v_friends)) #共同邻居节点
            for i in cn:
                if (u,v,i) in three_point or (u,i,v) in three_point or (i,v,u) in three_point or (v,u,i) in three_point or (i,u,v) in three_point or (v,i,u) in three_point:
                    continue
                else:
                    weight_triangle_n = G[u][v]['weight'] + G[u][i]['weight'] + G[v][i]['weight']
                    three_point.add((u,v,i))
            weight_triangle += weight_triangle_n 
            weight_triangle_n = 0 #加完之后置为0
        #计算除开三角形的三点组总权重
        else:
            u_friends = list(G.neighbors(u))
            v_friends = list(G.neighbors(v))
            cn = list(set(u_friends) & set(v_friends))
            for i in cn:
                weight_three_n = G[u][i]['weight'] + G[v][i]['weight']
            weight_three += weight_three_n
    #因为上面计算的是除开三角形的三点组总权重，所以最后三点组的总权重应该还要加上三角形的总权重
    weight_three += weight_triangle
    return weight_triangle/weight_three

#13无权网络局域聚类系数        
def Local_clustering_coefficient_unweight(G,i):
    ti = nx.triangles(G,i)#节点i所包含的三角形数量
    ki = G.degree(i)
    if ki*(ki-1) == 0:
        return 0.0
    return (2*ti)/(ki*(ki-1))

#14加权网络局域聚类系数
def Local_clustering_coefficient_weight_one(G,i,weight='weight'):
    edges = list(G.edges())
    si = G.degree(i,weight = weight)
    ki = G.degree(i)
    i_friends = nx.neighbors(G,i)
    weight_t = 0\
    #排除分母为零的情况
    if (ki-1) == 0:
        return 0
    for j,k in itertools.combinations(i_friends,2):
        if (j,k) in edges:
            weight_t += (G[i][j][weight] +G[j][k][weight])/2
    return weight_t/(si*(ki-1))

#Onnela等将莫提分析推广到加权网络研究的局域加权聚类系数
def Local_clustering_coefficient_weight_two(G,i,weight='weight'):
    edges_weight = list(G.edges(data = True))
    edges = list(G.edges())
    ki = G.degree(i)
    i_friends = nx.neighbors(G,i)
    weight_t = 0
    wmax = 0
    #排除分母为零的情况
    if (ki-1) == 0:
        return 0
    #获取连边权重最大的值wmax
    for u in edges_weight:
        if u[2][weight] > wmax:
            wmax = u[2][weight]
    for j,k in itertools.combinations(i_friends, 2):        
        if (j,k) in edges:
            wij = G[i][j][weight]/wmax
            wjk = G[j][k][weight]/wmax
            wik = G[i][k][weight]/wmax
            weight_t += pow(wij+wjk+wik,1/3)
    return 2/(ki*(ki-1)*weight_t)    
            
    
