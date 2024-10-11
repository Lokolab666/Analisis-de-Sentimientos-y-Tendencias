from fastapi import FastAPI
from tensorflow.keras.models import load_model
from transformers import BertTokenizer
from gensim.models import FastText
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np


app = FastAPI()

# Load models
model_sentiments_data_original = load_model("Despliegue/modelos/nlp_pqrs_original.h5")
model_sentiments_data_mezclada = load_model("Despliegue/modelos/nlp_sintetica.h5")

with open("Despliegue/modelos/tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)

fasttext_model_lda = FastText.load("app/models/FastText-Model-For-ABSA.bin")

# Define aspects for similarity
aspects = [
    "citas medicas", "enfermeria", "urgencias", "gestion documental", 
    "procedimientos de salud", "aseo y limpieza", "facturacion"
]


@app.post("/sentimientos_datos_original")
def predict_sentimiento(text: str):
    tokens = tokenizer.texts_to_sequences([text])
    x_new = pad_sequences(tokens, maxlen=50)
    predictions = model_sentiments_data_original.predict([x_new, x_new])
    emotions = {0: 'Negativo', 1: 'Neutral', 2: 'Positivo'}
    response = {emotions[i]: round(float(pred) * 100, 2) for i, pred in enumerate(predictions[0])}
    return {"texto": text, "predicciones": response}


@app.post("/sentimientos__datos_mezclados")
def predict_sentimiento(text: str):
    tokens = tokenizer.texts_to_sequences([text])
    x_new = pad_sequences(tokens, maxlen=50)
    predictions = model_sentiments_data_mezclada.predict([x_new, x_new])
    emotions = {0: 'Negativo', 1: 'Neutral', 2: 'Positivo'}
    response = {emotions[i]: round(float(pred) * 100, 2) for i, pred in enumerate(predictions[0])}
    return {"texto": text, "predicciones": response}


@app.post("/tendencias_lda")
def predict_tendencias(text: str):
    def get_similarity(text, aspect):
        try:
            text = " ".join(text)  # Simple tokenization
            return fasttext_model.wv.n_similarity(text, aspect)
        except Exception:
            return 0

    similarities = {aspect: get_similarity(text, aspect) for aspect in aspects}
    top_aspects = sorted(similarities.items(), key=lambda item: item[1], reverse=True)[:3]
    response = [{"aspecto": aspect, "similitud": round(similarity * 100, 2)} for aspect, similarity in top_aspects]
    return {"texto": text, "top_tendencias": response}

