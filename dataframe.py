"""MORE DOCUMENTATION NEEDED!!!!!!!!!!!!!!!!!!!!!!"""

"""Create simulation for different types of queues
"""

from main import *

# Arrival time will be 0.1-1 mimute with an average of 0.2 minutes
A_lower, A_upper, A_avg = 0.1, 1, 0.2

# Service time will be 0.5-5 minutes with an average of 2.75 minutes
S_lower, S_upper, S_avg = 0.5, 5, 2.75

# Simulation will allow new arrivals for 8 hours (480 minutes)
# Determine max rows by taking duration and diving by worst case
# scenario of arrival times (every 0.05 minutes)
dur = 480
n_max = int(dur/0.05)

# Generate arrival times based on truncated exponential distribution
Arange_param = (A_upper - A_lower)/A_avg
arrival_trunc = truncexpon(b=Arange_param, loc = A_lower, scale = A_avg).rvs(size = n_max)
arrival_sum = np.cumsum(arrival_trunc)
arrival_times = arrival_sum[arrival_sum <= dur]

# Generate service times based on truncated normal distribution
S_std = (S_upper - S_lower)/4 # General estimation for std of norm dist
S_a = (S_lower - S_avg) / S_std
S_b = (S_upper - S_avg) / S_std

service_times = truncnorm(a=S_a, b=S_b, loc=S_avg, scale=S_std).rvs(size=len(arrival_times))

# Create dataframe
column_names = ['CustomerID', 'ArrivalTime', 'ServiceTime', 'CounterID',
                'ArrivalStamp', 'ServiceStamp', 'FinishStamp', 'TotalQTime']
pd.set_option('display.max_columns', None)
df_init = pd.DataFrame(columns=column_names)
df_init['CustomerID'] = range(1, len(arrival_times) +1)
df_init['ArrivalTime'] = arrival_times
df_init['ServiceTime'] = service_times
df_init[['CounterID','ArrivalStamp', 'ServiceStamp', 'FinishStamp',
        'TotalQTime']]= 0

if __name__ == "__main__":
    print(df_init)
