#  加权无向网络零模型demo

原始网络数据文件：USAir97.txt，函数调用代码文件：NullModelCall.py,函数代码文件：WeightNetworkNullModels.py，详细理论说明：Algorithm_description.pdf

算法说明：每个零模型代码调用之后都可以生成一个对应的零模型数据文件，以csv的格式写在了当前路径下

##  一、基于随机断边重连的加权无向网络零模型

### 1.  0阶随机断边重连零模型

函数：

~~~python
def random_0k(G0,nspw=1,max_tries=100): #0阶随机断边重连零模型
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

调用：

~~~python
G0_0k = ws.random_0k(G0,nspw=2*edgesCount,max_tries=100*edgesCount) #零阶随机断边重连零模型
nx.write_edgelist(G0_0k,'WeightNetwork_0K.csv')
~~~



###  2.  1阶随机断边重连零模型

函数：

```python
def random_1k(G0,nswap=1,max_tries=100):    #1阶随机断边重连零模型
    if nswap >max_tries:
        raise nx.NetworkXError('"nswap > max_tries"')
    if len(G0)<4:
        raise nx.NetworkXError("Graph has less than three nodes")
    G = copy.deepcopy(G0)
    triesCount = 0
    brokenEdgesCount = 0
    edges = list(G.edges())
    nodes = G.nodes()
    while brokenEdgesCount < nswap:
        (u,v),(x,y) = random.sample(edges,2)
        if len(set([u,v,x,y])) < 4:
            continue
        if (u,y) not in edges and (y,u) not in edges and (x,v) not in edges and (v,x) not in edges:
            G.add_edges_from([(u,y),(x,v)]) #添加边
            G[u][y]['weight']=G[u][v]['weight']
            G[x][v]['weight']=G[x][y]['weight']
            G.remove_edges_from([(u,v),(x,y)])
            edges.extend([(u,y),(x,v)]) #边列表添加
            edges.remove((u,v)) #边列表移除
            edges.remove((x,y))
            brokenEdgesCount+=1
        if triesCount >= max_tries:
            e=('Maximum number of swap attempts (%s) exceeded '%triesCount +
            'before desired swaps achieved (%s).'%nswap)
            print (e)
            break
        triesCount +=1
    return G
```

调用：

```
G0_1k = ws.random_1k(G0,nswap=2*edgesCount,max_tries=100*edgesCount) #1阶随机断边重连零模型
nx.write_edgelist(G0_1k,'WeightNetwork_1K.csv')
```



###  3.  结构随机置乱零模型

函数：

```python
def structure_random(G0,delta=0,nswap=1,max_tries=100): #结构随机置乱零模型
    """"
    任取两个权重相同的连边，断边进行互连
    """
    if nswap >max_tries:
        raise nx.NetworkXError('"nswap > max_tries"')
    if len(G0)<4:
        raise nx.NetworkXError("Graph has less than three nodes")
    G = copy.deepcopy(G0)
    edges = list(G.edges())
    brokenCount = 0
    triesCount = 0
    while brokenCount < nswap:
        (u,v),(x,y) = random.sample(edges,2)
        if len(set([u,v,x,y])) < 4:
            continue
        if abs(float(G[u][v]['weight'])-float(G[x][y]['weight'])>delta):
            continue
        if (u,y) not in edges and (y,u) not in edges and (x,v) not in edges and (v,x) not in edges:
            G.add_edges_from([(u,y),(x,v)])
            G[u][y]['weight']=G[u][v]['weight']
            G[x][v]['weight']=G[x][y]['weight']
            G.remove_edges_from([(u,v),(x,y)])
            edges.extend([(u,y),(x,v)])
            edges.remove((u,v))
            edges.remove((x,y))
            brokenCount+=1
        if triesCount>max_tries:
            e=('Maximum number of swap attempts (%s) exceeded '%triesCount +
            'before desired swaps achieved (%s).'%nswap)
            print (e)
            break
        triesCount+=1
    return G
```

调用：

```python
G0_sr = ws.structure_random(G0,0,nswap=2*edgesCount,max_tries=100*edgesCount) #结构随机置乱零模型
nx.write_edgelist(G0_sr,'WeightNetwork_sr.csv')
```

###  4.  弱连边1阶零模型

函数：

```python
def weakEdge_1k(G0):#弱连边1阶零模型
    edges = list(G0.edges(data=True)) #一定要加上data=True，不然数据里面会没有权重
    weak_edges=[]
    weight = [] #用来放边权重
    for i in range(len(edges)):
        weight.append(edges[i][2]['weight'])
    weight.sort()   #权重数据五五分，前50%为弱连边，后50%为强连边,此次操作是为了找到处于中间权重值的数值，也就是门限值
    if len(weight) % 2 == 0:
        mid1 = int(len(weight)/2)
        mid2 = mid1 + 1
        if weight[mid1]==weight[mid2]:
            for i in edges: #小于门限值的，加入弱连边
                if i[2]['weight'] < weight[mid1]:
                    weak_edges.append(i)
        else:
            for i in edges:
                if i[2]['weight'] < weight[mid2]:
                    weak_edges.append(i)
    else:
        mid = math.floor(len(weight)/2)
        for i in edges:
            if i[2]['weight'] < weight[mid]:
                weak_edges.append(i)
    #----------------------改进部分------------------------
    G=copy.deepcopy(G0)
    for i in range(int(len(weak_edges))):
        weak_edges_random = random.sample(weak_edges,2)
        #选出两条边，其中节点u和v相连，x和y相连,现在进行断边重连
        u = weak_edges_random[0][0]
        v = weak_edges_random[0][1]
        x = weak_edges_random[1][0]
        y = weak_edges_random[1][1]
        G.add_edges_from([(u,y),(x,v)])
        G[u][y]['weight'] = weak_edges_random[0][2]['weight']
        G[x][v]['weight'] = weak_edges_random[1][2]['weight']
        G.remove_edges_from([(x,y),(u,v)])
    return G
```

调用：

```python
G0_weak = ws.weakEdge_1k(G0) #弱连边1阶零模型
nx.write_edgelist(G0_weak,'Weak_1k.csv')
```

###  5.  强连边1阶零模型

函数：

```python
def strong_1k(G0):  #强连边1阶零模型
    edges = list(G0.edges(data=True))
    weight = []
    strong_edge = []
    for i in range(len(edges)):
        weight.append(edges[i][2]['weight'])
    weight.sort(reverse=True)
    if len(weight)%2==0:
        mid1 = int(len(weight)/2)
        mid2 = mid1+1
        if weight[mid1]==weight[mid2]:
            for i in edges:
                if i[2]['weight'] > weight[mid1]:
                    strong_edge.append(i)
        else:
            for i in edges:
                if i[2]['weight'] < weight[mid2]:
                    strong_edge.append(i)
    else:
        mid = math.floor(len(weight)/2)
        for i in edges:
            if i[2]['weight'] > weight[mid]:
                strong_edge.append(i)
    #----------------------改进部分------------------------
    G=copy.deepcopy(G0)
    for i in range(int(len(strong_edge))):
        weak_edges_random = random.sample(strong_edge,2)
        #选出两条边，其中节点u和v相连，x和y相连,现在进行断边重连
        u = weak_edges_random[0][0]
        v = weak_edges_random[0][1]
        x = weak_edges_random[1][0]
        y = weak_edges_random[1][1]
        G.add_edges_from([(u,y),(x,v)])
        G[u][y]['weight'] = weak_edges_random[0][2]['weight']
        G[x][v]['weight'] = weak_edges_random[1][2]['weight']
        G.remove_edges_from([(x,y),(u,v)])
    return G
```

调用：

```python
G0_strong = ws.strong_1k(G0) #强连边1阶零模型
nx.write_edgelist(G0_strong,'Strong_1k.csv')
```

###  6.  权重随机置乱零模型

```python
def weight_random(G0,nswap=1,max_tries=100):   #权重随机置乱零模型
    G = copy.deepcopy(G0)
    if nswap > max_tries:
        raise nx.NetworkXError('nswap>max_tries')
    if len(G.edges)<4:
        raise nx.NetworkXError('Graph has less than four nodes')
    edges = list(G.edges())
    brokenCount = 0
    triesCount = 0
    while brokenCount < nswap:
        (u, v), (x, y) = random.sample(edges, 2)
        if len(set([x,y,u,v])) < 4:
            continue
        G[u][v]['weight'],G[x][y]['weight'] = G[x][y]['weight'],G[u][v]['weight']
        if triesCount >= max_tries:
            e=('Maximum number of swap attempts (%s) exceeded '%triesCount +
            'before desired swaps achieved (%s).'%nswap)
            print (e)
            break
        triesCount +=1
    return G
```

调用：

```python
G0_weightrandom = ws.weight_random(G0,nswap=2*edgesCount,max_tries=100*edgesCount) #权重随机置乱零模型
nx.write_edgelist(G0_weightrandom,'weight_equal.csv')
```

##  二、有倾向性断边重连的加权无向网络零模型

###  1.  面向富人俱乐部的零模型

​	函数：

```python
def rich_club_break(G0, k, max_tries=100):
    """
    富边：富节点和富节点的连边
    非富边：非富节点和非富节点的连边
    任选两条边(一条富边，一条非富边)，若富节点和非富节点间无连边，则断边重连
    达到最大尝试次数或无富边或无非富边，循环结束
    """
    if len(G0) < 4:
        raise nx.NetworkXError("Graph has less than four nodes.")
    G = copy.deepcopy(G0)
    edges = list(G.edges())
    nodes = G.nodes()
    rnodes = [e for e in nodes if G.degree(e,weight='weight')>=k]     #全部富节点
    redges = [e for e in edges if e[0] in rnodes and e[1] in rnodes] #网络中已有的富节点和富节点的连边
    pedges = [e for e in edges if e[0] not in rnodes and e[1] not in rnodes] #网络中已有的非富节点和非富节点的连边
#    len_redges = len(redges)
#    len_pedges = len(pedges)
    n = 0
    while redges and pedges:
        u,v = random.choice(redges)              #随机选一条富边
        x,y = random.choice(pedges)           #随机选一条非富边
        if (x,u) not in edges and (u,x) not in edges and (v,y) not in edges and (y,v) not in edges:
            G.add_edges_from([(u,x),(v,y)])
            G[u][x]['weight'] = G[u][v]['weight']
            G[v][y]['weight'] = G[x][y]['weight']
            G.remove_edges_from([(u,v),(x,y)])
            edges.extend([(u,x),(v,y)])
            edges.remove((u,v))
            edges.remove((x,y))
            redges.remove((u,v))
            pedges.remove((x,y))
        if n >= max_tries:
            print ('Maximum number of attempts (%s) exceeded '%n)
            break
        n += 1
    return G
```

调用：

```python
strengh = []
Gs=G0.degree(weight='weight')
for i in Gs: #将图中节点的强度排序，取第五十个作为阈值，大于阈值的强度的节点称为富节点
    strengh.append(i[1])
num=50
strengh.sort(reverse=True)
k=strengh[num]
G0_rich = ws.rich_club(G0,k,100*edgesCount) #面向富人俱乐部的零模型
nx.write_edgelist(G0_rich,'rich_club.csv')
G0_rich_break = ws.rich_club_break(G0,k,100*edgesCount)
nx.write_edgelist(G0_rich_break,'rich_club_break.csv')
```

###  2.  面向强度匹配特性的零模型

函数：

```python
def assort_mixing(G0, nswap=1, max_tries=100): #同配
    """
    强度大的边与强度大的边匹配
    """
    G = copy.deepcopy(G0)
    if len(G) < 4:
        raise nx.NetworkXError("Graph has less than four nodes.")
    if nswap > max_tries:
        raise nx.NetworkXError("nswap<max_tries.")
    breakCount = 0
    triesCount = 0
    edges = list(G.edges())
    while breakCount < max_tries:
        (u,v),(x,y) = random.sample(edges,2)
        if len(set([u,v,x,y])) < 4:
            continue
        points,weightSum = zip(*sorted(list(G.degree([u,v,x,y],weight='weight')),key=lambda d:d[1],reverse=True))
        points_list = list(points)
        a,b,c,d = points_list
        zip(*sorted(list(G.degree([u, v, x, y], weight='weight')), key=lambda d: d[1], reverse=True))
        if (a, b) not in edges and (b, a) not in edges and (c, d) not in edges and (d, c) not in edges:
            G.add_edges_from([(a, b), (c, d)])
            G[a][b]['weight'] = G[u][v]['weight']
            G[c][d]['weight'] = G[x][y]['weight']
            G.remove_edges_from([(u, v), (x, y)])
            edges.extend([(a, b), (c, d)])
            edges.remove((u, v))
            edges.remove((x, y))
            breakCount += 1
        if  triesCount>= max_tries:
            e = ('Maximum number of swap attempts (%s) exceeded ' % triesCount +
                 'before desired swaps achieved (%s).' % nswap)
            print(e)
            break
        triesCount += 1
    return G

def disassort_mixing(G0,nswap=1,max_tries=100): #异配
    """
    强度大的节点和强度小的节点相连
    :param G0:
    :param nswap:
    :param max_tries:
    :return:
    """
    if nswap>max_tries:
        raise nx.NetworkXError("Number of swaps > number of tries allowed.")
    if len(G0) < 4:
        raise nx.NetworkXError("Graph has less than four nodes.")
    G = copy.deepcopy(G0)
    triesCount = 0
    breakCount = 0
    edges = list(G.edges())
    while breakCount < nswap:
        (u,v),(x,y) = random.sample(edges,2) #任选两条边
        if len(set([u,v,x,y]))<4:
            continue
        points,weightSum = zip(*sorted(G.degree([u,v,x,y],weight='weight'),key=lambda d:d[1],reverse=True))
        points_list = list(points)
        a,b,c,d = points_list
        if (a,d) not in edges and (d,a) not in edges and (c,b) not in edges and (b,c)not in edges:
            G.add_edges_from([(a,d),(b,c)])
            G[a][d]['weight'] = G[u][v]['weight']
            G[b][c]['weight'] = G[x][y]['weight']
            G.remove_edges_from([(u,v),(x,y)])
            edges.extend([(a,d),(b,c)])
            edges.remove((u,v))
            edges.remove((x,y))
            breakCount += 1
        if triesCount >= max_tries:
            e=('Maximum number of swap attempts (%s) exceeded '%triesCount +
            'before desired swaps achieved (%s).'%nswap)
            print (e)
            break
        triesCount += 1
    return G
```

调用：

```python
#同配
G0_assort = ws.assort_mixing(G0,nswap=2*edgesCount,max_tries=100*edgesCount)
nx.write_edgelist(G0_assort,'G0_assort.csv')
#异配
G0_dissort = ws.disassort_mixing(G0,nswap=2*edgesCount,max_tries=100*edgesCount)
nx.write_edgelist(G0_dissort,'G0_dissort.csv')
```