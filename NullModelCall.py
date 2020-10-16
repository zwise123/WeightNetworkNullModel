import networkx as nx
import WeightNetworkNullModels as ws
import matplotlib.pyplot as plt

fp = open('USAir97.txt','rb')
G = nx.read_weighted_edgelist(fp)   #实证网络数据读取
fp.close()
# nx.draw(G)
# plt.show()


G0 = G.to_undirected() #原始网络无向化
edgesCount = len(G0.edges())
nx.draw(G0)
plt.show()

# G0_0k = ws.random_0k(G0,nspw=2*edgesCount,max_tries=100*edgesCount) #零阶随机断边重连零模型
# nx.write_edgelist(G0_0k,'WeightNetwork_0K.csv')
# nx.draw(G0_0k)
# plt.show()
#
# G0_1k = ws.random_1k(G0,nswap=2*edgesCount,max_tries=100*edgesCount) #1阶随机断边重连零模型
# nx.write_edgelist(G0_1k,'WeightNetwork_1K.csv')
#
# G0_sr = ws.structure_random(G0,0,nswap=2*edgesCount,max_tries=100*edgesCount) #结构随机置乱零模型
# nx.write_edgelist(G0_sr,'WeightNetwork_sr.csv')
#
# G0_weak = ws.weakEdge_1k(G0) #弱连边1阶零模型
# nx.write_edgelist(G0_weak,'Weak_1k')

# G0_strong = ws.strong_1k(G0) #强连边1阶零模型
# nx.write_edgelist(G0_strong,'Strong_1k')

# G0_weightrandom = ws.weight_random(G0,nswap=2*edgesCount,max_tries=100*edgesCount) #权重随机置乱零模型
# nx.write_edgelist(G0_weightrandom,'weight_equal.csv')

# ------------------------有倾向性断边重连的加权无向网络零模型----------------------------------
# strengh = []
# Gs=G0.degree(weight='weight')
# for i in Gs:
#     strengh.append(i[1])
# num=50
# strengh.sort(reverse=True)
# k=strengh[num]
# G0_rich = ws.rich_club(G0,k,100*edgesCount) #面向富人俱乐部的零模型
# nx.write_edgelist(G0_rich,'rich_club.csv')
# G0_rich_break = ws.rich_club_break(G0,k,100*edgesCount)
# nx.write_edgelist(G0_rich_break,'rich_club_break.csv')

#面对强度匹配特性的零模型
G0_assort = ws.assort_mixing(G0,nswap=2*edgesCount,max_tries=100*edgesCount)
nx.write_edgelist(G0_assort,'G0_assort.csv')

G0_dissort = ws.disassort_mixing(G0,nswap=2*edgesCount,max_tries=100*edgesCount)
nx.write_edgelist(G0_dissort,'G0_dissort.csv')