import networkx as nx
import matplotlib.pyplot as plt
import numpy
import csv

class TubeMap:
    def __init__(self,file_name):
        self.map = nx.Graph()
        self.file_name = file_name

    def get_stations(self):
        with open(self.file_name,mode = "r",encoding = "utf-8") as tube_stations:
            reader = csv.reader(tube_stations)
            for line in reader:
                self.map.add_path(line[2:], data = {'line':line[0],'edge_colour':line[1]})
##      print(self.map.edges())
                
    def generate_edge_colours(self,current_map):
        return edge_colours

    def create_graph_plot(self,current_map):
        pass

    def display_full_map(self):
        pass

    def display_travel_map(self,start,end):
        pass

    def get_directions(self,start,end):
        return directions

if __name__ == "__main__":
    TubeMap = TubeMap("tube.csv")
    TubeMap.get_stations()
