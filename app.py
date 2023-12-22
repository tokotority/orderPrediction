from flask import Flask, render_template, request
import pickle
import numpy
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
holiday_map	= {
    'Yes' : 1,
    'No' : 0
}
discount_No_map = {
    'Yes' : 0,
    'No' : 1
}

region_code_map = {
    'R1' : [1,0,0,0],
    'R2' : [0,1,0,0],
    'R3' : [0,0,1,0],
    'R4' : [0,0,0,1]
}
location_type_map = {
    'L1' : [1,0,0,0,0],
    'L2' : [0,1,0,0,0],
    'L3' : [0,0,1,0,0],
    'L4' : [0,0,0,1,0],
    'L5' : [0,0,0,0,1]
}
store_type_map = {
    'S1' : [1,0,0,0],
    'S2' : [0,1,0,0],
    'S3' : [0,0,1,0],
    'S4' : [0,0,0,1]
}

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    store_id = [int(request.form['store_id'])]
    holiday = [int(holiday_map[request.form['holiday']])]
    discount = [int(discount_No_map[request.form['discount']])]
    region_code = region_code_map[request.form['region_code']]
    location_type = location_type_map[request.form['location_type']]
    store_type = store_type_map[request.form['store_type']]
    features = store_id + holiday + discount + region_code + location_type + store_type

    valarr = [numpy.array(features)]
    prediction = model.predict(valarr)
    return render_template('index.html', 
                           prediction=round(prediction[0]),
                           storeID=store_id[0],)

if __name__ == '__main__':
    app.run(debug=True)
