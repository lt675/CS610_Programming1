from main import *

class CounterQueue:
    def __init__(self):
        self.counters = {}
    
    def create_counter(self, counter_id):
        self.counters[counter_id] = Queue()
        print(f"Queue created for Counter ID {counter_id}")
    
    def enqueue(self, counter_id, customer_id):
        if counter_id in self.counters:
            try:
                self.counters[counter_id].put_nowait(customer_id)
            except Exception as e:
                print(f"Error adding customer: {e}")
    
    def dequeue(self, counter_id):
        if counter_id in self.counters:
            try:
                return self.counters[counter_id].get_nowait()
            except Empty:
                pass
        return None

if __name__ == "__main__":
    
    df_queue = df_init.copy()
    df_queue = df_queue.drop(df_queue.index[100:])
    df_queue['CounterID'] = df_queue.index % 5 + 1
    
    print(df_queue)
    """Use this for now. Write your own test code later"""
    
    # Assuming the CounterQueue class is defined above
    
    # Initialize the CounterQueue
    counter_queue = CounterQueue()
    
    # Create counters based on unique CounterID in df_queue
    unique_counter_ids = df_queue['CounterID'].unique()
    for counter_id in unique_counter_ids:
        counter_queue.create_counter(counter_id)
    
    # Enqueue customers from df_queue
    for index, row in df_queue.iterrows():
        customer_id = {
            'CustomerID': row['CustomerID'],
            'ArrivalTime': row['ArrivalTime'],
            'ServiceTime': row['ServiceTime'],
            'CountAssign': row['CounterID']
        }
        counter_queue.enqueue(row['CounterID'], customer_id)
    
    # Dequeue and print customers from each counter to verify
    for counter_id in unique_counter_ids:
        print(f"Dequeueing from Counter ID {counter_id}:")
        while True:
            customer_id = counter_queue.dequeue(counter_id)
            if customer_id is None:
                break  # Exit when the queue is empty
            print(customer_id)
