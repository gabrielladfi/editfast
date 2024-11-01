from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes. Cambia "*" por la URL de tu frontend en producción.
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP.
    allow_headers=["*"],  # Permitir todos los headers.
)


API_URL = "http://161.35.113.72:3000/api/v1/prediction/940107e9-61e5-43dd-bf44-a3c9079cc943"
headers = {"Authorization": "Bearer OCtTClr7ajlz70NqRwoEWPXMljs7acxZKv54mpH-QAU"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# Definir el modelo de datos de entrada
class QuestionRequest(BaseModel):
    question: str

# Endpoint que acepta solicitudes POST
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    question = request.question
    print(question)
    try:
        response = query({
            "question": f"{question}",
        })
        final_response = response["response"]["text"]
        return {"response": final_response}
    except:
        return {"response": "No encuentro información al respecto"}

# Para correr el servidor, utiliza: uvicorn main:app --reload
