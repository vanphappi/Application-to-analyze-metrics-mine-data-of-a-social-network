    
import networkx as nx
import pandas as pd

data = pd.read_csv('facebook_combined2.csv',header=None)
data_friend = pd.DataFrame()
data_friend[['FromNodeID','ToNodeID']]=data.iloc[:,[0,1]]
G = nx.from_pandas_edgelist(data_friend, 'FromNodeID', 'ToNodeID')
non_edges=nx.non_edges(G)

def common_neighbors():
       
            list_common_neighbors=[(e[0],e[1],
                        len(list(nx.common_neighbors(G,e[0],e[1]))))
                        for e in non_edges]
            return list_common_neighbors#sorted(list_common_neighbors, key= lambda x: x[2] ,reverse=True)

def preferential_attachment():
      
            list_preferential_attachment=[(e[0],e[1],
                        list(nx.preferential_attachment(G,[(e[0],e[1])]))[0][2])
                        for e in non_edges]
            return list_preferential_attachment#sorted(list_preferential_attachment, key= lambda x: x[2] ,reverse=True)
    
def adamic_adar(self):
    
            list_adamic_adar=[(e[0],e[1],
                        list(nx.adamic_adar_index(G,[(e[0],e[1])]))[0][2])
                        for e in non_edges]
            return sorted(list_adamic_adar, key= lambda x: x[2] ,reverse=True)

def katz(self):
      
            phi = (1 + math.sqrt(n_nodes+1))
            centrality = nx.katz_centrality(G, 1 / phi - 0.01)
            list_katz=list(centrality.items())
            return sorted(list_katz, key= lambda x: x[1] ,reverse=True)

print(common_neighbors())
non_edges=nx.non_edges(G)

print(list(non_edges))