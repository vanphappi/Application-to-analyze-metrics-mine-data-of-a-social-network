from datetime import date
import math
import pandas as pd
from pandas.core.frame import DataFrame
import networkx as nx
import matplotlib.pyplot as plt
from pyvis import network as net
import plotly.graph_objects as go
from networkx.algorithms.community.centrality import girvan_newman
import numpy as np


class pre_data:
    data_friend = pd.DataFrame()
    G=None
    graph=None
    n_nodes=0
    n_edges=0
    stats=None
    pos=None
    non_edges=None

    loc_data=None

    def __init__(self,loc_data):
        self.loc_data=loc_data
        self.data_processing()

    def data_processing(self):
        data = pd.read_csv(self.loc_data,header=None)
        self.data_friend = pd.DataFrame()
        self.data_friend[['FromNodeID','ToNodeID']]=data.iloc[:,[0,1]]
        self.G = nx.from_pandas_edgelist(self.data_friend, 'FromNodeID', 'ToNodeID')
        self.non_edges=nx.non_edges(self.G)
        self.graph=nx.from_pandas_edgelist(self.data_friend,'FromNodeID','ToNodeID',create_using=nx.DiGraph())
        self.n_nodes=self.graph.number_of_nodes()
        self.n_edges=self.graph.number_of_edges()
        self.stats=pd.DataFrame(self.graph.nodes())
        self.stats.columns=['NODE']

    def r_pos(self):
        self.pos=nx.spring_layout(self.graph,k=0.15,iterations=20) 

class d_network(pre_data):

    def __init__(self,loc_data):
        super().__init__(loc_data)

    def d_allnetwork(self):
        if(self.pos==None):
            super().r_pos()
            plt.figure(figsize=(15, 15))
            nx.draw(self.graph, self.pos, node_size=80, node_color='black',alpha=0.7,edge_color='0.5',with_labels=False,width=True)
            plt.show()
        else:
            plt.figure(figsize=(15, 15))
            nx.draw(self.graph,self.pos, node_size=80, node_color='black',alpha=0.7,edge_color='0.5',with_labels=False,width=True)
            plt.show()

    def d_degree_centrally(self):
        if(self.pos==None):
            super().r_pos()
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                node_color=list(nx.degree_centrality(self.graph).values()),
                                nodelist=nx.degree_centrality(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('degree_centrality') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show()
        else:
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                node_color=list(nx.degree_centrality(self.graph).values()),
                                nodelist=nx.degree_centrality(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('degree_centrality') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show() 

    def d_in_degree_centrality(self):
        if(self.pos==None):
            super().r_pos()
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                               node_color=list(nx.in_degree_centrality(self.graph).values()),
                               nodelist=nx.in_degree_centrality(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('in_degree_centrality') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show() 
        else:
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                               node_color=list(nx.in_degree_centrality(self.graph).values()),
                               nodelist=nx.in_degree_centrality(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('in_degree_centrality') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show()

    def d_out_degree_centrality(self):
        if(self.pos==None):
            super().r_pos()
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                               node_color=list(nx.out_degree_centrality(self.graph).values()),
                               nodelist=nx.out_degree_centrality(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('out_degree_centrality') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show()
        else:
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                               node_color=list(nx.out_degree_centrality(self.graph).values()),
                               nodelist=nx.out_degree_centrality(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('out_degree_centrality') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show()
    
    def d_betweenness_centrality(self):
        if(self.pos==None):
            super().r_pos()
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                        node_color=list(nx.betweenness_centrality(self.graph).values()),
                                        nodelist=nx.betweenness_centrality(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('betweenness_centrality') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show()
        else:
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                        node_color=list(nx.betweenness_centrality(self.graph).values()),
                                        nodelist=nx.betweenness_centrality(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('betweenness_centrality') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show()

    def d_closeness_centrality(self):
        try:
            if(self.pos==None):
                super().r_pos()
                fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
                nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                            node_color=list(nx.closeness_centrality(self.graph.reverse(),wf_improved=False).values()),
                                            nodelist=nx.closeness_centrality(self.graph.reverse(),wf_improved=False).keys())
                edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
                plt.title('closeness_centrality') 
                plt.colorbar(nodes) 
                plt.axis('off') 
                plt.show()
            else:
                fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
                nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                            node_color=list(nx.closeness_centrality(self.graph.reverse(),wf_improved=False).values()),
                                            nodelist=nx.closeness_centrality(self.graph.reverse(),wf_improved=False).keys())
                edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
                plt.title('closeness_centrality') 
                plt.colorbar(nodes) 
                plt.axis('off') 
                plt.show()
        except:
            plt.close()
            if(self.pos==None):
                super().r_pos()
                fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
                nodes = nx.draw_networkx_nodes(self.G, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                            node_color=list(nx.closeness_centrality(self.G,wf_improved=False).values()),
                                            nodelist=nx.closeness_centrality(self.G,wf_improved=False).keys())
                edges = nx.draw_networkx_edges(self.G, self.pos,alpha=0.2,width=0.5)
                plt.title('closeness_centrality') 
                plt.colorbar(nodes) 
                plt.axis('off') 
                plt.show()
            else:
                fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
                nodes = nx.draw_networkx_nodes(self.G, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                            node_color=list(nx.closeness_centrality(self.G,wf_improved=False).values()),
                                            nodelist=nx.closeness_centrality(self.G,wf_improved=False).keys())
                edges = nx.draw_networkx_edges(self.G, self.pos,alpha=0.2,width=0.5)
                plt.title('closeness_centrality') 
                plt.colorbar(nodes) 
                plt.axis('off') 
                plt.show()            

    def d_clustering_coefficient(self):
        if(self.pos==None):
            super().r_pos()
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                        node_color=list(nx.clustering(self.graph).values()),
                                        nodelist=nx.clustering(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('clustering_coefficient') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show()
        else:
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                        node_color=list(nx.clustering(self.graph).values()),
                                        nodelist=nx.clustering(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('clustering_coefficient') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show()

    def d_grivan_newman(self):
        if(self.pos==None):
            super().r_pos()
            cluster=girvan_newman(self.graph)
            node_groups = next(cluster)
            n = len(node_groups)
            color = list(np.random.choice(range(256), size=n+1))
            color_node = []
            dict ={}
            for node in self.graph: 
                for i in range (n):
                    if node in node_groups[i]:
                        color_node.append(color[ i])
                        dict.update({node: color[i]})
                        break
            color_edge =[]
            for edge in self.graph.edges:
                i = dict.get(edge[0])
                j = dict.get(edge[1])
                if (i==j): 
                    color_edge.append(i)
                else:
                    color_edge.append(color[n])
            plt.figure(figsize=(25, 25))
            nx.draw(self.graph, self.pos, node_size=80,
                    node_color=color_node,alpha=0.7,edge_color=color_edge,with_labels=False,width=0.6)
            plt.title('Community detection for graph subcriber') 
            plt.show()
        else:
            cluster=girvan_newman(self.graph)
            node_groups = next(cluster)
            n = len(node_groups)
            color = list(np.random.choice(range(256), size=n+1))
            color_node = []
            dict ={}
            for node in self.graph: 
                for i in range (n):
                    if node in node_groups[i]:
                        color_node.append(color[ i])
                        dict.update({node: color[i]})
                        break
            color_edge =[]
            for edge in self.graph.edges:
                i = dict.get(edge[0])
                j = dict.get(edge[1])
                if (i==j): 
                    color_edge.append(i)
                else:
                    color_edge.append(color[n])
            plt.figure(figsize=(25, 25))
            nx.draw(self.graph, self.pos, node_size=80,
                    node_color=color_node,alpha=0.7,edge_color=color_edge,with_labels=False,width=0.6)
            plt.title('Community detection for graph subcriber') 
            plt.show()

    def d_page_rank(self):
        if(self.pos==None):
            super().r_pos()
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                        node_color=list(nx.pagerank(self.graph).values()),
                                        nodelist=nx.pagerank(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('page_rank') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show()
        else:
            fig, ax = plt.subplots(1,1, figsize=(25,25), dpi=50)
            nodes = nx.draw_networkx_nodes(self.graph, self.pos, node_size=80, cmap=plt.cm.plasma, 
                                        node_color=list(nx.pagerank(self.graph).values()),
                                        nodelist=nx.pagerank(self.graph).keys())
            edges = nx.draw_networkx_edges(self.graph, self.pos,alpha=0.2,width=0.5)
            plt.title('page_rank') 
            plt.colorbar(nodes) 
            plt.axis('off') 
            plt.show() 

class output_data(pre_data):

    stats_Degree=None
    stats_InDegree=None
    stats_OutDegree=None
    stats_betweenness_centrality=None
    stats_closeness_centrality=None
    stats_clustering_coeficient=None
    stats_pagerank=None

    list_common_neighbors=None
    list_preferential_attachment=None
    list_adamic_adar=None
    list_katz=None

    def __init__(self,loc_data):
        super().__init__(loc_data)

    def degree_centrality_value(self):
        degree_list = [v for k, v in nx.degree_centrality(self.graph).items()]
        self.stats['DEGREE CENTRALITY']=degree_list
        self.stats['DEGREE CENTRALITY'] = round(self.stats['DEGREE CENTRALITY'] * (self.n_nodes-1))
        self.stats_Degree=self.stats[['NODE','DEGREE CENTRALITY']]
    
    def in_degree_centrality_value(self):
        in_degree_list = [v for k, v in nx.in_degree_centrality(self.graph).items()]
        self.stats['IN-DEGREE CENTRALITY']=in_degree_list
        self.stats['IN-DEGREE CENTRALITY'] = round(self.stats['IN-DEGREE CENTRALITY'] * (self.n_nodes-1))
        self.stats_InDegree=self.stats[['NODE','IN-DEGREE CENTRALITY']]

    def out_degree_centrality_value(self):
        out_degree_list = [v for k, v in nx.out_degree_centrality(self.graph).items()]
        self.stats['OUT-DEGREE CENTRALITY']=out_degree_list
        self.stats['OUT-DEGREE CENTRALITY'] = round(self.stats['OUT-DEGREE CENTRALITY'] * (self.n_nodes-1))
        self.stats_OutDegree=self.stats[['NODE','OUT-DEGREE CENTRALITY']]
    
    def betweenness_centrality_value(self):
        betweenness_centrality = [v for k, v in nx.betweenness_centrality_subset(self.graph,self.graph.nodes,self.graph.nodes).items()]
        self.stats['BETWEENNESS CENTRALITY']=betweenness_centrality
        self.stats_betweenness_centrality=self.stats[['NODE','BETWEENNESS CENTRALITY']]

    def closeness_centrality_value(self):
        try:
            closeness_centrality_list = [v for k, v in nx.closeness_centrality(self.graph.reverse(),wf_improved=False).items()]
            self.stats['CLOSENESS CENTRALITY']=closeness_centrality_list
            self.stats_closeness_centrality=self.stats[['NODE','CLOSENESS CENTRALITY']]
        except:
            closeness_centrality_list = [v for k, v in nx.closeness_centrality(self.G,wf_improved=False).items()]
            self.stats['CLOSENESS CENTRALITY']=closeness_centrality_list
            self.stats_closeness_centrality=self.stats[['NODE','CLOSENESS CENTRALITY']]

    def clustering_coeficient_value(self):
        clustering_coeficient_list = [v for k, v in nx.clustering(self.graph).items()]
        self.stats['CLUSTERING COEFFICIENT']=clustering_coeficient_list
        self.stats_clustering_coeficient=self.stats[['NODE','CLUSTERING COEFFICIENT']]
    
    def centrality_fre(self,type):
        counts=self.stats.groupby([type]).size().reset_index(name='FREQUENCY')
        counts['PROBABILITY']=counts['FREQUENCY']/counts['FREQUENCY'].sum()
        return counts

    def girvan_newman_anal(self):
        list_data=[]
        cluster=girvan_newman(self.graph)
        node_groups = next(cluster)
        n = len(node_groups)
        list_data.append('Số cộng đồng: '+str(n))
        for i in range (n):
            list_data.append('Cộng đồng '+str(i)+':'+str(node_groups[i]))
        return list_data
    
    def page_rank_anl(self,num=1):
        try:
            return self.stats_pagerank.sort_values(by='PAGE RANK', ascending=False).head(num)
        except:
            pagerank_list = [v for k, v in nx.pagerank(self.graph).items()]
            self.stats['PAGE RANK']=pagerank_list
            self.stats_pagerank=self.stats[['NODE','PAGE RANK']]
            return self.stats_pagerank.sort_values(by='PAGE RANK', ascending=False).head(num)
    
    def page_rank_fre(self):
        try:
            counts=self.stats.groupby(['PAGE RANK']).size().reset_index(name='FREQUENCY')
            counts['PROBABILITY']=counts['FREQUENCY']/counts['FREQUENCY'].sum()
            return counts
        except:
            self.page_rank_anl()
            counts=self.stats.groupby(['PAGE RANK']).size().reset_index(name='FREQUENCY')
            counts['PROBABILITY']=counts['FREQUENCY']/counts['FREQUENCY'].sum()
            return counts

    def common_neighbors(self):
        try:
            return sorted(self.list_common_neighbors, key= lambda x: x[2] ,reverse=True)
        except:
            self.list_common_neighbors=[(e[0],e[1],
                        len(list(nx.common_neighbors(self.G,e[0],e[1]))))
                        for e in self.non_edges]
            return sorted(self.list_common_neighbors, key= lambda x: x[2] ,reverse=True)

    def preferential_attachment(self):
        try:
            return sorted(self.list_preferential_attachment, key= lambda x: x[2] ,reverse=True)
        except:
            self.list_preferential_attachment=[(e[0],e[1],
                        list(nx.preferential_attachment(self.G,[(e[0],e[1])]))[0][2])
                        for e in self.non_edges]
            return sorted(self.list_preferential_attachment, key= lambda x: x[2] ,reverse=True)
    
    def adamic_adar(self):
        
        try:
            return sorted(self.list_adamic_adar, key= lambda x: x[2] ,reverse=True)
        except:
            self.list_adamic_adar=[(e[0],e[1],
                        list(nx.adamic_adar_index(self.G,[(e[0],e[1])]))[0][2])
                        for e in self.non_edges]
            return sorted(self.list_adamic_adar, key= lambda x: x[2] ,reverse=True)

    def katz(self):
        try:
            return sorted(self.list_katz, key= lambda x: x[1] ,reverse=True)
        except:
            phi = (1 + math.sqrt(self.n_nodes+1))
            centrality = nx.katz_centrality(self.G, 1 / phi - 0.01)
            self.list_katz=list(centrality.items())
            return sorted(self.list_katz, key= lambda x: x[1] ,reverse=True)

class backend(d_network,output_data):

    def __init__(self,loc_data):
        d_network.__init__(self,loc_data)
        output_data.__init__(self,loc_data)
        self.type_di=self.graph
        self.type_non_di=self.G

    def set_type_graph(self,num):
        if(num==0):
            self.graph=self.type_non_di
        else:
            self.graph=self.type_di
            

    def d_type(self,type):
        if(type=='DEGREE CENTRALITY'):
            self.d_degree_centrally()
        elif (type=='IN-DEGREE CENTRALITY'):
            self.d_in_degree_centrality()
        elif (type=='OUT-DEGREE CENTRALITY'):
            self.d_out_degree_centrality()
        elif (type=='BETWEENNESS CENTRALITY'):
            self.d_betweenness_centrality()
        elif (type=='CLOSENESS CENTRALITY'):
            self.d_closeness_centrality()
        elif (type=='CLUSTERING COEFFICIENT'):
            self.d_clustering_coefficient()
    
    def op_data_value(self,type,num):
        if(type=='DEGREE CENTRALITY'):
            try:
                return self.stats_Degree.sort_values(by='DEGREE CENTRALITY', ascending=False).head(num)
            except:
                self.degree_centrality_value()
                return self.stats_Degree.sort_values(by='DEGREE CENTRALITY', ascending=False).head(num)
        elif(type=='IN-DEGREE CENTRALITY'):
            try:
                return self.stats_InDegree.sort_values(by='IN-DEGREE CENTRALITY', ascending=False).head(num)
            except:
                self.in_degree_centrality_value()
                return self.stats_InDegree.sort_values(by='IN-DEGREE CENTRALITY', ascending=False).head(num)
        elif(type=='OUT-DEGREE CENTRALITY'):
            try:
                return self.stats_OutDegree.sort_values(by='OUT-DEGREE CENTRALITY', ascending=False).head(num)
            except:
                self.out_degree_centrality_value()
                return self.stats_OutDegree.sort_values(by='OUT-DEGREE CENTRALITY', ascending=False).head(num)
        elif(type=='BETWEENNESS CENTRALITY'):
            try:
                return self.stats_betweenness_centrality.sort_values(by='BETWEENNESS CENTRALITY', ascending=False).head(num)
            except:
                self.betweenness_centrality_value()
                return self.stats_betweenness_centrality.sort_values(by='BETWEENNESS CENTRALITY', ascending=False).head(num)
        elif(type=='CLOSENESS CENTRALITY'):
            try:
                return self.stats_closeness_centrality.sort_values(by='CLOSENESS CENTRALITY', ascending=False).head(num)
            except:
                self.closeness_centrality_value()
                return self.stats_closeness_centrality.sort_values(by='CLOSENESS CENTRALITY', ascending=False).head(num)
        elif(type=='CLUSTERING COEFFICIENT'):
            try:
                return self.stats_clustering_coeficient.sort_values(by='CLUSTERING COEFFICIENT', ascending=False).head(num)
            except:
                self.clustering_coeficient_value()
                return self.stats_clustering_coeficient.sort_values(by='CLUSTERING COEFFICIENT', ascending=False).head(num)

    def op_data_fre(self,type):
        try:
            return self.centrality_fre(type)
        except:
            if(type=='DEGREE CENTRALITY'):
                self.degree_centrality_value()
            elif (type=='IN-DEGREE CENTRALITY'):
                self.in_degree_centrality_value()
            elif (type=='OUT-DEGREE CENTRALITY'):
                self.out_degree_centrality_value()
            elif (type=='BETWEENNESS CENTRALITY'):
                self.betweenness_centrality_value()
            elif (type=='CLOSENESS CENTRALITY'):
                self.closeness_centrality_value()
            elif (type=='CLUSTERING COEFFICIENT'):
                self.clustering_coeficient_value()
            return self.centrality_fre(type)
    
    def link_prediction(self,type):
        if(type =='COMMON NEIGHBORS'):
            self.non_edges=nx.non_edges(self.G)
            return self.common_neighbors()
        elif(type =='PREFERENTIAL ATTACHMENT'):
            self.non_edges=nx.non_edges(self.G)
            return self.preferential_attachment()
        elif(type =='ADAMIC/ADAR'):
            self.non_edges=nx.non_edges(self.G)
            return self.adamic_adar()
        else:
            self.non_edges=nx.non_edges(self.G)
            return self.katz()

    def get_n_nodes(self):
        return int(self.n_nodes)
