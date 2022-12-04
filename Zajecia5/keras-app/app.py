import flask
import tensorflow
import numpy as np

app = flask.Flask(__name__)
model = None

def load_model():
    global model 
    model = tensorflow.keras.models.load_model('FMNIST_Model.h5')

@app.route("/")
def hello():
    return "This is Fashion MNIST prediction app. Use <b>/predict</b> endpoint with POST request e.g. <br><br> curl -X POST -F image=@observation.csv 'http://localhost:5000/predict'"

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            image = np.genfromtxt(flask.request.files["image"], delimiter=',')/255
            image = image.reshape(1,28, 28, 1)
            preds = model.predict(image).tolist()[0]
            data["predictions"] = []
            for (label, prob) in enumerate(preds):
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)
            data["success"] = True

    return flask.jsonify(data)
if __name__ == "__main__":
    print("* Loading Keras model and Flask starting server...")
    load_model()
    app.run(host='0.0.0.0', threaded=False)