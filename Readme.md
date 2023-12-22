# Install Python Virtual Env
Switch your working directory to this repository, and run:
```bash
python3 -m venv .venv
source ./.venv/bin/activate
```

# Install Dependencies
```bash
pip3 install -r requirements.txt
```

# Train Model
Run the following command to train model:
```bash
python3 train.py
```
This script will retrieve data set from Azure object storage. Connection string of the storage account is now hard coded in the script for testing purpose. Execution of this file will take a while and then you'll see output below:
```
store_type
S1    88752
S4    45924
S2    28896
S3    24768
Name: count, dtype: int64
******************************
location_type
L1    85140
L2    48504
L3    29928
L5    13932
L4    10836
Name: count, dtype: int64
******************************
region_code
R1    63984
R2    54180
R3    44376
R4    25800
Name: count, dtype: int64
******************************
holiday
0    163520
1     24820
Name: count, dtype: int64
******************************
discount
No     104051
Yes     84289
Name: count, dtype: int64
******************************
Train Accuracy:  0.7336097453795882
```
The model will be dumpped to a file: `model.pkl`.

# Run Flask 
```bash
flask run
```

# Test
Open your browser and type in `127.0.0.1:5000`, you'll be able to input the features and start predict the order number of a specific store by id.