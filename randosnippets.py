# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:56:08 2024

@author: litem
"""

# Generate linked list class
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def append(self, node):
        if not self.head:
            self.head = node  # If the list is empty, set the head to the new node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = node  # Add the new node at the end

    # def display(self):
    #     current = self.head
    #     while current:
    #         print(f"CustomerID: {current.customer_id}, "
    #               f"ArrivalTime: {current.arrival_time}, "
    #               f"ServiceTime: {current.service_time}, "
    #               f"Countassign: {current.count_assign}, "
    #               f"ArrTimestp: {current.arr_timestp}, "
    #               f"ServStrTimestp: {current.serv_str_timestp}, "
    #               f"ServFinTimestp: {current.serv_fin_timestp}, "
    #               f"TotQueueTime: {current.tot_queue_time}")
    #         current = current.next

# # Display the linked list
# linked_list.display()





# # Generate node class to store row information from dataframe
# class Node:
#     def __init__(self, customer_id, arrival_time, service_time, count_assign=None,
#                   arr_timestp=None, serv_str_timestp=None, serv_fin_timestp=None,
#                   tot_queue_time=None):
#         self.customer_id = customer_id
#         self.arrival_time = arrival_time
#         self.service_time = service_time
#         self.count_assign = count_assign
#         self.arr_timestp = arr_timestp
#         self.serv_str_timestp = serv_str_timestp
#         self.serv_fin_timestp = serv_fin_timestp
#         self.tot_queue_time = tot_queue_time
#         self.next = None  # Pointer to the next node

# # Generate linked list class
# class LinkedList:
#     def __init__(self):
#         self.head = None  # Start with an empty list

#     def append(self, node):
#         if not self.head:
#             self.head = node  # If the list is empty, set the head to the new node
#         else:
#             current = self.head
#             while current.next:  # Traverse to the end of the list
#                 current = current.next
#             current.next = node  # Add the new node at the end

#     def display(self):
#         current = self.head
#         while current:
#             print(f"CustomerID: {current.customer_id}, "
#                   f"ArrivalTime: {current.arrival_time}, "
#                   f"ServiceTime: {current.service_time}, "
#                   f"Countassign: {current.count_assign}, "
#                   f"ArrTimestp: {current.arr_timestp}, "
#                   f"ServStrTimestp: {current.serv_str_timestp}, "
#                   f"ServFinTimestp: {current.serv_fin_timestp}, "
#                   f"TotQueueTime: {current.tot_queue_time}")
#             current = current.next

# # Generate linked list for customers
# linked_list = LinkedList()

# # Iterate over DataFrame rows and create nodes
# for _, row in df_init.iterrows():
#     new_node = Node(
#         customer_id=row['CustomerID'],
#         arrival_time=row['ArrivalTime'],
#         service_time=row['ServiceTime'],
#         count_assign=row['CountAssign'],
#         arr_timestp=row['ArrTimestp'],
#         serv_str_timestp=row['ServStrTimestp'],
#         serv_fin_timestp=row['ServFinTimestp'],
#         tot_queue_time=row['TotQueueTime']
#     )
#     linked_list.append(new_node)
