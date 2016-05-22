import numpy as np # linear algebra
import pandas as pd
from __future__ import print_function

train = pd.read_csv('F:/UTD/Match/Kaggle/train.csv',
                    dtype={'srch_destination_id':np.int32,'is_booking':bool,'hotel_cluster':np.int32},
                    usecols=['srch_destination_id','is_booking','hotel_cluster'],
                    chunksize=50000)
aggregate = []
for chunk in train:
    agg = chunk.groupby(['srch_destination_id','hotel_cluster'])['is_booking'].agg(['sum','count'])
    agg.reset_index(inplace=True)
    aggregate.append(agg)
    print('.',end='')

print('')
aggregate = pd.concat(aggregate, axis=0)
aggregate.head()

#here merge every chunk together
click_weight = 0.1
agg1 = aggregate.groupby(['srch_destination_id','hotel_cluster']).sum().reset_index()
agg1['count'] -= agg1['sum']
agg1 = agg1.rename(columns={'sum':'bookings','count':'clicks'})
agg1['relevance'] = agg1['bookings'] + click_weight * agg1['clicks']
print(agg1.head())
    
#Find most popular hotel clusters by destination
def mostPopular(group, n_max=5):
    relevance = group['relevance'].values
    hotel_cluster = group['hotel_cluster'].values
    most_popular = hotel_cluster[np.argsort(relevance)[::-1]][:n_max]
    return np.array_str(most_popular)[1:-1] # remove square brackets

most_pop = agg1.groupby(['srch_destination_id',]).apply(mostPopular)
most_pop = pd.DataFrame(most_pop).rename(columns={0:'hotel_cluster'})
most_pop.head()


test = pd.read_csv('F:/UTD/Match/Kaggle/test.csv',
                    dtype={'srch_destination_id':np.int32},
                    usecols=['srch_destination_id'],)
test = test.merge(most_pop, how='left',left_on='srch_destination_id',right_index=True)
test.head()
test.hotel_cluster.isnull().sum()
most_pop_all = agg1.groupby('hotel_cluster')['relevance'].sum().nlargest(5).index
most_pop_all = np.array_str(most_pop_all)[1:-1]
#most_pop_all
test.hotel_cluster.fillna(most_pop_all,inplace=True)
test.hotel_cluster.to_csv('predicted_with_pandas.csv',header=True, index_label='id')