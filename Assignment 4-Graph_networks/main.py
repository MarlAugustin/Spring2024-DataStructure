import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from urllib.request import urlopen
import json

# plt.show()
link = "https://data.transportation.gov/resource/4f3n-jbg2.json?year=2022"
file = urlopen(link)
list_of_flights = []
list_of_flights = json.load(file)
nx_graphs = nx.DiGraph()
user_search = input("Enter a city: ")
for flight in list_of_flights:
  city1 = flight["city1"]
  city2 = flight["city2"]
  if user_search in str(city1) :
    nx_graphs.add_edge(city1, city2, weight=flight["nsmiles"])
if nx_graphs.number_of_nodes() == 0:
  print("Flight not found")
else:
  nx.draw(nx_graphs, with_labels=True, font_weight='bold')
  nx.draw_networkx_edge_labels(nx_graphs,  nx.spring_layout(nx_graphs), edge_labels = nx.get_edge_attributes(nx_graphs, "weight"))
  plt.show()
  