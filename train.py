# %%
### import libraries
import numpy as np 
import os
from azure.storage.blob import BlobServiceClient
from io import StringIO
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle


# %% [markdown]
# # Data Loading

# %%
# show the dataset structure
connection_string = "BlobEndpoint=https://mldatasettmp.blob.core.windows.net/;QueueEndpoint=https://mldatasettmp.queue.core.windows.net/;FileEndpoint=https://mldatasettmp.file.core.windows.net/;TableEndpoint=https://mldatasettmp.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2024-12-22T22:45:53Z&st=2023-12-22T14:45:53Z&spr=https&sig=tSqSY9VryzqE%2F%2B%2FoPos%2BpuuvoYvKUpl9Wl%2FQJ7UFbz4%3D"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

blob_name = "TRAIN.csv"
container_name = "datasets"

blob_client = blob_service_client.get_blob_client(container_name, blob_name)

blob_data = blob_client.download_blob().readall()
df = pd.read_csv(StringIO(blob_data.decode('utf-8')))
df.head()

# %%
df.tail()

# %%
# show the dataset columns
df.columns

# %%
# reformat the column names
df.columns=df.columns.str.lstrip("#").str.lower()
df.head(2)

# %%
# remove the id column
df.drop("id",axis=1,inplace=True)
df.head(2)

# %%
col=["store_type","location_type","region_code","holiday","discount"]

for i in col:
    print(df[i].value_counts())
    print("*"*30)

# %% [markdown]
# # Data Preprocessing

# %%
df.isna().sum()

# %% [markdown]
# # Encoding

# %%
# transfer non numeric columns to numeric columns
dms=pd.get_dummies(df[["discount","region_code","location_type","store_type"]])
dms

# %%
df.drop(["discount","region_code","location_type","store_type"],
        axis=1,inplace=True)
df.head()

# %%
df=pd.concat([df,dms],axis=1)
df.head()

# %%
df.drop("discount_Yes",axis=1,inplace=True)
df.drop("date",axis=1,inplace=True)
df.drop("sales",axis=1,inplace=True)
df.head()

# %% [markdown]
# # Modelling

# %%
X=df.drop("order",axis=1)
y=df["order"]

# %%
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

# %%
### Random Forest Regressor Fit
rf=RandomForestRegressor().fit(X_train,y_train)

# %%
accuary=rf.score(X_train,y_train)
print("Train Accuracy: ",accuary)

# %% [markdown]
# # Conclusion
# We can see the Accuracy is over 70%. Let dump the model to use it later.

# %%
pickle.dump(rf,open('model.pkl','wb'))


