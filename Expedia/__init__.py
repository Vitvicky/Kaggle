import pandas as pd
import os
import random
import operator


trainFilePath = "F:/UTD/Match/Kaggle/test.csv"
pwd = os.getcwd()
os.chdir(os.path.dirname(trainFilePath))
trainData = pd.read_csv(os.path.basename(trainFilePath))
#print trainData.head(5)

#correlation
#trainData.corr()["hotel_cluster"]

#extract train data's year,month
trainData["date_time"] = pd.to_datetime(trainData["date_time"])
trainData["year"] = trainData["date_time"].dt.year
trainData["month"] = trainData["date_time"].dt.month
#print trainData["month"]
unique_users = trainData.user_id.unique()
sel_user_ids = [unique_users[i] for i in sorted(random.sample(range(len(unique_users)), 50000)) ]
sel_train = trainData[trainData.user_id.isin(sel_user_ids)]
t1 = sel_train[( ((sel_train.year == 2014) & (sel_train.month < 9)))]
t2 = sel_train[((sel_train.year == 2014) & (sel_train.month >= 9))]

match_features = ['user_location_country', 'user_location_region', 'user_location_city', 'hotel_market', 'orig_destination_distance']
groups = t1.groupby(match_features)


def generate_matches(row, match_features):
    index = tuple([row[t] for t in match_features])
    try:
        group = groups.get_group(index)
    except Exception:
        return [];
    clus = list(set(group.hotel_cluster))
    return clus

def f5(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return resultdef make_key(items):
    return "_".join([str(i) for i in items])

#def predict(test,match_features):
#    predict_result = []
#    for index,row in test.iterrows():
#        key = make_key([row[m] for m in match_features])
#        if key in cluster_dict:
#            preds.append(cluster_dict[key])
#        else:
#            preds.append([])
            
            
            
exact_matches = []
for i in range(t2.shape[0]):
    exact_matches.append(generate_matches(t2.iloc[i],match_features))
