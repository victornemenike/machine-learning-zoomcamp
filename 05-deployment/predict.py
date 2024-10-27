import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

customer = {"job": "management", "duration": 400, "poutcome": "success"}
#def predict(customer):
X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print('input', customer)
print('churn probability', y_pred)