
import joblib
from preprocess import text_prepare

# load saved models
vec = joblib.load("./saved_models/raw_cv_vectorizer.pkl")
model = joblib.load("./saved_models/logreg.pkl")

index_to_label = {1: 'Stress', 0: 'Not Stressed'}


def ml_predict(text):
    dredd = text_prepare(text)
    vec_transformed = vec.transform([dredd])
    return index_to_label[model.predict(vec_transformed).item()]
