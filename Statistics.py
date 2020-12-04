'''
topic:统计量的计算
author:zwise
'''
import networkx as nx
import WeightNetworkNullModels as ws
import matplotlib.pyplot as plt
import copy
from networkx.algorithms import cluster as cls


# 节点单位权重的计算
def avg_weight(G,i):
    si = G.degree(i,weight='weight')
    ki = G.degree(i)
    return si/ki

#权重分布的差异性yi
def difference_weight(G,i):
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

# 最短路径长度
def shortest(G):
    pass



# 1.5聚类系数
def clustering_coefficient(G):
    td_iter = cls._directed_weighted_triangles_and_degree_iter(G, nodes=None, weight=None)
    for v, dt, db, t in td_iter:
        print(v,dt,db,t)



fp = open('USAir97.txt','rb')
G = nx.read_weighted_edgelist(fp)   #原始网络数据读取
fp.close()
G0 = G.to_undirected() #原始网络无向化
edgesCount = len(G0.edges())

clustering_coefficient(G0)

# yi = difference_weight(G0,'3') #权重分布的差异性yi
# r = matching_coefficient_r(G0) #无权网络匹配系数r
# print(r)
# rw1 = matching_coefficient_rw1(G0) #加权网络匹配系数rw1
# print(rw1)
# rw2 = matching_coefficient_rw2(G0) #加权网络匹配系数rw2
# print(rw2)
# knni = avg_neigh_ki(G0,'1') #邻居节点的平均度knni
# print(knni)
# kwnni = avg_neigh_kwi(G0,'1') # 最近邻节点权重的平均
# print(kwnni)



# G0_0k = ws.random_0k(G0,nspw=2*edgesCount,max_tries=100*edgesCount) #零阶随机断边重连零模型
# ki = G0.degree('1')#度
# ki = G0.degree('1')
# ki_0k = G0_0k.degree('1')
# si = G0.degree('1',weight='weight')#强度
# si_0k = G0_0k.degree('1',weight='weight')
# ui = si/ki#单位权重
# ui_0k = si_0k/ki_0k
# print('原始网络节点1的度：',G0.degree('1'))
# print('0阶随机断边重连零模型之后节点1的度：',G0_0k.degree('1'))
# print('原始网络节点1的强度：',G0.degree('1',weight='weight'))
# print('0阶随机断边重连零模型之后节点1的强度',G0_0k.degree('1',weight='weight'))
# print('原网络单位权重',avg_weight(G0,'1'))
# print('0阶随机断边重连零模型单位权重',ui_0k)
# print('1和2节点之间的权重',G0[1][2]['weight'])


