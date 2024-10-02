from main import *
from dataframe import df_init
from queuelogic import CounterQueue


df_screwy = df_init.copy()


class Router:
    def __init__(self, data):
        self.tree = Tree()
        self.tree.create_node("Arrival", "arrival", data = df_screwy)
    
    def add_child(self, parent_id, child_data):
        self.create_node("Counter 1", "counter1", parent="arrival")
    
    def single_queue(self, record):
        counter1 = self.tree.children("arrival")[0]
        







routing = Tree()
routing.create_node("Arrival", "arrival", data = df_init)
routing.create_node("Counter 1", "counter1", parent="arrival")
routing.create_node("Counter 2", "counter2", parent="arrival")
routing.create_node("Counter 3", "counter3", parent="arrival")
routing.create_node("Counter 4", "counter4", parent="arrival")
routing.create_node("Counter 5", "counter5", parent="arrival")

print(routing)
print('arrival')

