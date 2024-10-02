from main import *




class Router:
    def __init__(self):
        self.data = None
        self.tree = Tree()
        self.tree.create_node("Arrival", "arrival") #No initial data
        self.counter_queue = CounterQueue()
    
    def set_data(self, data):
        self.data = data
        self.tree.get_node("arrival").data = self.data #Update root with new data
    
    def add_child(self, parent_id, counter_id):
        self.tree.create_node(counter_id, counter_id, parent=parent_id)
    
    def single_queue(self, customer_id):
        single_counter = self.tree.children("arrival")[0] #find 1st counter
        counter_id = single_counter.identifier #which r u?
        self.counter_queue.enqueue(counter_id, customer_id) #yeet customer
    
    def round_robin(self, customer_id):
        data = self.set_data.
        
        df_queue['CounterID'] = df_queue.index % 5 + 1
        counter_id = self.tree.children("arrival")[0] #find 1st counter
        



if __name__ == "__main__":
    # Initialize DataFrame for testing
    df_tree = df_init.copy()  # Assuming df_init is already defined in your code
    df_tree = df_tree.drop(df_tree.index[100:])  # Trimming the DataFrame for testing
    print(df_tree)

    def test_single_queue_with_dataframe(df_tree):
        # Step 1: Initialize Router with sample data
        router = Router()
        router.set_data(df_tree)  # Set the data for the router (if necessary)
    
        # Step 2: Create counters based on unique CounterIDs from df_tree
        unique_counter_ids = df_tree['CounterID'].unique()
        for counter_id in unique_counter_ids:
            router.add_child("arrival", f"Counter {counter_id}")  # Add child nodes for each counter
    
        # Step 3: Test single_queue method with each customer in df_tree
        for index, row in df_tree.iterrows():
            customer_id = {
                'CustomerID': row['CustomerID'],
                'ArrivalTime': row['ArrivalTime'],
                'ServiceTime': row['ServiceTime'],
                'CountAssign': row['CounterID']
            }
            
            # Call single_queue to enqueue the customer
            router.single_queue(customer_id)
    
        # Step 4: Verify the state of the first counter's queue
        first_counter_id = router.tree.children("arrival")[0].identifier  # Get the first counter ID
        queued_customer = router.counter_queue.dequeue(first_counter_id)  # Dequeue a customer from the first counter
    
        # Print the result to check if the customer was enqueued correctly
        print(f"Dequeued customer from Counter {first_counter_id}: {queued_customer}")

    # Run the test using df_tree
    test_single_queue_with_dataframe(df_tree)



