import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


seer_df = pd.read_csv('drugs.csv',index_col=0)

sites_list = [site for site in seer_df['Primary Site'] if not pd.isnull(site)]
sites_set = set()

for site_list in sites_list:
    sites = site_list.split(';')

    for site in sites:
        sites_set.add(site.upper())

drugs_list = seer_df.index.tolist()
drugs_set = set()

for drug in drugs_list:
    if not pd.isnull(seer_df.loc[drug]['Primary Site']):
        drugs_set.add(drug)

edges = []

for index, sites in seer_df[['Primary Site']].iterrows():
    if not pd.isnull(sites['Primary Site']):
        sites_list = sites['Primary Site']
        for site in sites_list.split(';'):
            edges.append((index,site))


C = nx.Graph()
C.add_nodes_from(drugs_set, bipartite=0)
C.add_nodes_from(sites_set, bipartite=1)
C.add_edges_from(edges)

nx.draw(C, with_labels = True)  
plt.show()