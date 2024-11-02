import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from urllib.request import urlopen
import json

#direct flights
link = "https://data.transportation.gov/resource/4f3n-jbg2.json?year=2022"
file = urlopen(link)
list_of_flights = []
list_of_flights = json.load(file)
G = nx.DiGraph()
user_search_from = input("Enter a city (From): ")
user_search_to = input("Enter a city (To): ")
dict_of_connecting_flights = {}
for flight in list_of_flights:
  city1 = flight["city1"]
  city2 = flight["city2"]
  if user_search_from in str(city1):
    #direct flights
    #big o of n
    if user_search_from in str(city1) and user_search_to in str(city2):
      G.add_edge(city1, city2, weight=flight["fare"])
      print("There is at least one direct flight. Between " +
            user_search_from + " and " + user_search_to + " fare: " +
            flight["fare"])
if G.number_of_nodes() == 0:
  #Non-direct flights
  #big o of n^2, since to find non-direct flights I needed to use a nested for loop
  print("There is no direct flights. Between " + user_search_from + " and " +
        user_search_to)
  for flight in list_of_flights:
    city1 = flight["city1"]
    city2 = flight["city2"]
    if user_search_from in str(city1):
      for secound_flight in list_of_flights:
        secound_flight_city1 = secound_flight["city1"]
        secound_flight_city2 = secound_flight["city2"]
        if city2 in secound_flight_city1 and user_search_to in secound_flight_city2:
          G.add_edge(city1, city2, weight=flight["fare"])
          G.add_edge(city2,
                     secound_flight_city2,
                     weight=secound_flight["fare"])
          dict_of_connecting_flights[secound_flight_city1] = secound_flight[
              "fare"]
          print("The connecting city for " + user_search_from + " to " +
                user_search_to + " is " + flight["city2"] + " fare: " +
                (secound_flight["fare"]))
#Finding and showing the cheapest flight
cheapest_flight = ""
count = 0
for connected_flights in dict_of_connecting_flights:
  #big o of n, because we are going through the dictionary
  if count == 0:
    cheapest_flight = connected_flights
  if dict_of_connecting_flights[
      connected_flights] < dict_of_connecting_flights[cheapest_flight]:
    cheapest_flight = connected_flights
  count += 1
if G.number_of_nodes() == 0:
  print("There is no direct or non direct flights. Between " +
        user_search_from + " and " + user_search_to)
else:
  if len(dict_of_connecting_flights) != 0:
    print("The Cheapest connecting flight is: " + cheapest_flight + " fare: " +
          dict_of_connecting_flights[cheapest_flight])
  #Showing/printing the graph
  pos_spaced = nx.fruchterman_reingold_layout(G, k=0.5, iterations=100)
  plt.figure(figsize=(6, 10))  # 6x10 inches
  nx.draw(G, pos=pos_spaced, with_labels=True)
  nx.draw_networkx_edge_labels(G,
                               pos_spaced,
                               edge_labels=nx.get_edge_attributes(G, "weight"))
  #plt.show(block=False)
  plt.show()