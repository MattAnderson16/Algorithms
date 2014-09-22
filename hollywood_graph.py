import networkx as nx

hollywood_graph = nx.Graph()
hollywood_graph.add_edge("Vicent Cassel","Scott Cann",data = {"film":"Ocean's Thirteen"}) # creates edge and vertices, can only create two at a time.
hollywood_graph.add_edge("Vicent Cassel","James McAvoy",data = {"film":"Trance"}) # can add a third parameter for labels e.g. label = {"film":"x-men"}
hollywood_graph.add_edge("James McAvoy","Kevin Bacon",data = {"film":"X-Men"})
hollywood_graph.add_edge("James McAvoy","Rasario Dawson",data = {"film":"Trance"})
hollywood_graph.add_edge("Rasario Dawson","Richard Frice",data = {"film":"Unstoppable"})
hollywood_graph.add_edge("Richard Frice","Kevin Bacon",data = {"film":"Planes, Trains and Automobiles"})
hollywood_graph.add_edge("Kevin Bacon","David Crow",data = {"film":"X-Men"})
hollywood_graph.add_edge("Kevin Bacon","Lasco Atkins",data = {"film":"X-Men"})
hollywood_graph.add_edge("Kevin Bacon","Michael Fassbender",data = {"film":"X-Men"})
hollywood_graph.add_edge("David Crow","Idris Elba",data = {"film":"Buffalo Soldiers"})
hollywood_graph.add_edge("Idris Elba","Michael Fassbender",data = {"film":"Prometheus"})
hollywood_graph.add_edge("Michael Fassbender","Noomi Rapace",data = {"film":"Prometheus"})
hollywood_graph.add_edge("Noomi Rapace","Lasco Atkins",data = {"film":"Sherlock Holmes"})
