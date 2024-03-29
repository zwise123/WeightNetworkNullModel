## 加权无向网络零模型

加权无向网络零模型算法说明

## 基于随机断边重连的加权无向网络零模型
### 0阶随机断边重连零模型
由于加权网络中的连边带有权重，因此断边重连过程中要保证删除的连边和新增的连边权重一致。每次断边重连的具体过程如图所示：先随机从原始网络中删除一条带有权重的连边，如图(a)所示中的AC边，再随机从网络中选择两个不相连的节点，如A、D节点，在A与D之间添加一条连边，新添加的连边权重要与原始网络AC边的权重相同，重连后的结果如图(b)所示。为了使网络充分随机化，一般应根据网络的规模将上述断边重连过程重复多次，直到原始网络足够随机化后才认为生成了对应的零模型。  
<img src="https://github.com/zwise123/WeightNetworkNullModel/blob/master/githubPic/0%E9%98%B6%E9%9B%B6%E6%A8%A1%E5%9E%8B%E7%BD%91%E7%BB%9C.jpg"  alt="0阶随机断边重连零模型"  width="600" height="200"/>

### 1阶随机断边重连零模型
加权网络中0阶零模型改变了原始网络的度分布和权重分布，是随机性最强的一种零模型。为了降低零模型的随机性，本节中介绍随机化程度低一些的1阶零模型， 它保持原始网络的度序列(度分布)不变。加权网络1阶零模型也可以使用随机断边重连的方式产生，具体构造过程如图所示：先随机选择四个不同节点，如图(a)中 的A、B、C和D四个节点，保证这四个节点之间至少存在两条连边如AC和BD，然后将 这两条连边断徭后在AD和BC之间生成新的连边，新添加的连边AD(BC)的权重分别与 原始网络AC(BD)边的权重相同，重连后的结果如图(b)所示。为了使网络充分随机 化，丌般应根据网络的规模将上述断边重连过程重复多次，直到原始网络足够随机化 后才认为生成了对应的零模型。  
<img src="https://github.com/zwise123/WeightNetworkNullModel/blob/master/githubPic/1%E9%98%B6%E9%9B%B6%E6%A8%A1%E5%9E%8B.png"  alt="1阶随机断边重连零模型"  width="600" height="200"/>
### 结构随机置乱零模型
上述加权网络的零阶模型与1阶模型同时置乱了网络的拓扑和权重，无法分辨出原始网络中权重相关性还是拓扑结构是该网络非平凡特性的内在因素。本小节中介绍的结构置乱算法保证了连边权重没有发生改变，改变的仅仅是网络的拓扑结构，因此可 以用该零模型来衡量原始网络中拓扑结构对于网络非平凡特性的影响。
结构置乱算法的具体产生过程如图所示。首先随机选取他对权重相等的连边，如图(a)中的边AC和BD，如果此时节点A与D不相连，B与C不相连，那么可 将连边AC和BD切断，再使节点A与D相连，B与C相连，连边上的权重均和以前的连 边AC(BD)权重相同。等权重置乱算法破坏了网络的拓扑结构，但每个节点的强度并没 有发生变化，每个节点连边之间的权重相关性也没有发生变化，因此可以用来研究拓 扑结构对网络性质的影响。在有些网络中，寻找权重相同的连边比较困难，此时为了保证尽可能交换比较多的连边，可以在要求不严格的情况下，将权重近似的边进行交换构造零模型。  
<img src="https://github.com/zwise123/WeightNetworkNullModel/blob/master/githubPic/%E7%BB%93%E6%9E%84%E7%BD%AE%E4%B9%B1%E9%9B%B6%E6%A8%A1%E5%9E%8B.png"  alt="1阶随机断边重连零模型"  width="600" height="200"/>
### 弱连边1阶零模型
为了衡量弱连边在网络中的作用，可以通过断边重连的方式生成弱连边1阶置乱零模型。如图(a)所示，一个简单的加权网络，按照上面介绍的强弱连接划分方法 可以将此网络中的连边划分为强连边AB和CD，弱连边AC和BD。首先在网络中的弱连边中随机选择两条连边AC和BD；如果此时节点A与D不相连，B与C不相连，那么可将连边AC和BD切断，再使节点A与D相连，B与C相连，连边上的权重均和以前的连 边AC(BD)权重相同。根据网络的规模重复上述两个步骤足够多次，就可以构造出弱连 边1阶置乱零模型。弱连边1阶置乱零模型在保持了网络的度分布不变的同时，也保证了强连边之间的拓扑结构和权重相关性不变，只改变了弱连边的结构和权重分布。因此，该零模型可以用来衡量原始网络中弱连边对网络非平凡特性的影响。  
<img src="https://github.com/zwise123/WeightNetworkNullModel/blob/master/githubPic/%E5%BC%B1%E8%BF%9E%E8%BE%B91%E9%98%B6%E9%9B%B6%E6%A8%A1%E5%9E%8B.png"  alt="1阶随机断边重连零模型"   width="600" height="200"/>
### 强连边1阶零模型
根据构造弱连边1阶置乱零模型的构造方法，同样可以构造出强连边1阶置乱零 模型，构造过程如图所示。首先，在原始网络中随机选择两条强连边，如图(a)中的AC和BD，如果此时节点A与D不相连，B与C不相连，那么可将连边AC和BD切 断，再使节点A与D相连，B与C相连，连边上的权重均和以前的连边AC(BD)权重相 同。根据网络的规模重复上述两个步骤足够多次，就可以构造出强连边1阶置乱零模 型。强连边1阶置乱零模型在保持原始网络的平均度和度分布不变的同时，也可以保持 原始网络中弱连边的拓扑结构和权重分布不变，只置乱强连边的拓扑结构和权重，该 零模型可以用来衡量原始网络中强连边对于网络非平凡特性的影响。  
<img src="https://github.com/zwise123/WeightNetworkNullModel/blob/master/githubPic/%E5%BC%BA%E8%BF%9E%E8%BE%B91%E9%98%B6%E9%9B%B6%E6%A8%A1%E5%9E%8B.png"  alt="1阶随机断边重连零模型"  width="600" height="200"/>
### 权重随机置乱零模型
除了原始网络的拓扑结构，节点之间的权重相关性是影响网络非平凡特性的另仦 个重要因素。为了单独研究权重的影响，北师大狄增如研究小组在对经济物理学家交 流网络的研究中提出了权重置乱算法。典型权重置乱算法的具体过程如图所示，首先在网络中随机选取两个权重不相等的连边，如连边AB的权重为3，CD的权重为2； 然后将两个连边权重置乱(交换)，置乱后连边AB的权重为2，CD的权重为3。根据网络 的规模重复上述两个步骤足够多次，就可以达到置乱连边权重的目的。  
<img src="https://github.com/zwise123/WeightNetworkNullModel/blob/master/githubPic/%E6%9D%83%E9%87%8D%E7%BD%AE%E4%B9%B1%E9%9B%B6%E6%A8%A1%E5%9E%8B.png"  alt="1阶随机断边重连零模型"  width="600" height="200"/>
## 有倾向性断边重连的加权无向网络零模型
### 面向富人俱乐部的零模型
在无权网络中大多数网络都存在的富人俱乐部现象，比如在Internet网络中，度大 节点（富节点）之间连接往往比较多，形成的网络子图密度也比较大[59]。在加权网络中，我们将强度大的节点定义为富节点，称强度大的节点(富节点)之间相互连接的现象 为富人俱乐部现象。在图(a)所示的网络中，可以看到节点的尺寸有大有小，节点 之间的连边有粗有细。这里节点的尺寸大小表示该节点的强度，节点越大表示它们的 强度也就越大。而连边的宽度表示的是连边权重的大小，边越宽，表示权重越大。在 ˆ重要的五个节点（红色标记）之间的六条连接的权重之和为14；在图(b)中，朌 强的六条连接为黑色，他们的权重总和为21。因此得到两者的比值为14/21 = 2/3。 通过上面的一个简单的边权重数值分析，可以看出在加权网络中的富人俱乐部现象， 不但要考虑节点的度，也要考虑边的权重。  
### 面向强度匹配特性的零模型
在加权网络中，如果强度大的节点倾向于和强度大的节点相连，强度小的节点倾 向于和强度小的节点相连，那么网络中存在节点强度的正匹配特性。相反，如果强度 小的节点倾向于和强度大的节点相连，那么网络中存在节点强度的负匹配特性。加权 随机置乱算法不仅破坏了网络拓扑，也扰乱了网络本身的强度相关性，使连边不再具
有强度同配或异配特性。  
### 面向全局最优的零模型
复杂网络通常根据全局效率原则来优化其组织形式，其中心思想就是通过优化连 边权重达到将整体流量柏大化的目的[55,56]。根据全局效率原则，连边的权重应该与其介数中心性相关，每条连边的介数中心性与所有通过它的节点对之间的构短路径数量 成正比[55,57,58]，也就是说，连边的介数中心性越大，越多的节点对之间的构短路径经 过它，这样的连边起到的是“桥梁”作用。因此，通过给高介数中心性的连边赋予大的 权重值，可以提高网络中的全局效率。根据这仙思想，可以构造出一个使网络整体流 量达到朰大化的全局杀优零模型，如图所示。首先，计算图(a)中原始网络的 所有连边的介数中心性；然后，根据连边介数中心性的大小把网络的原始权重进行重 新分配，介数中心性大的连边，分配到的权重就越大；将原始网络中所有连边按照原则分配就构造出原始网络的全局杀优零模型，如图(b)所示。通过这样有倾向性的置乱原始网络的权重，可以在保持原始网络拓扑结构的基础上将网络连边的权重和通 过它的构短路径的节点对的数量调节为正比关系，达到全局杀优的效果，此零模型可 以用来衡量原始网络的全局效率对于非平凡特性的影响。  
<img src="https://github.com/zwise123/WeightNetworkNullModel/blob/master/githubPic/%E9%9D%A2%E5%90%91%E5%85%A8%E5%B1%80%E6%9C%80%E4%BC%98%E7%9A%84%E9%9B%B6%E6%A8%A1%E5%9E%8B.png"  alt="1阶随机断边重连零模型"   width="600" height="200"/>







