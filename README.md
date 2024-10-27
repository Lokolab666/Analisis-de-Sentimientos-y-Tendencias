# API de predicción de Sentimientos y de Tendencias

Este proyecto es un servicio web basado en FastAPI que proporciona dos funcionalidades principales:

1. **Predicción de Sentimientos**: Predice si un texto dado es negativo, neutral o positivo.
2. **Predicción de Tendencias**: Identifica tendencias a partir de un texto dado basándose en aspectos predefinidos relacionados con la atención médica.

## Project Structure

```
.
├── Despliegue
│   ├── main.py
│   ├── modelos
│   │   ├── FastText-Model-For-ABSA.bin
│   │   └── nlp_pqrs_original.h5
│   │   └── nlp_sintetica.h5
│   │   └── tokenizer.pkl
├── Dockerfile
├── requirements.txt
└── README.md
```

## Endpoints

### `/sentimientos_datos_original` (POST)
- **Description**: Predice el sentimiento del texto dado a partir de los datos originales.
- **Request Body**: `{ "text": "stexto para analizar" }`
- **Response**: 
  ```json
  {
    "texto": "texto para analizar",
    "predicciones": {
      "Negativo": 85.5,
      "Neutral": 3.7,
      "Positivo": 10.8
    }
  }
  ```
### `/sentimientos__datos_mezclados` (POST)
- **Description**: Predice el sentimiento del texto dado a partir de los datos genéricos.
- **Request Body**: `{ "text": "stexto para analizar" }`
- **Response**: 
  ```json
  {
    "texto": "texto para analizar",
    "predicciones": {
      "Negativo": 10.5,
      "Neutral": 45.7,
      "Positivo": 43.8
    }
  }
  ```


### `/tendencias_lda` (POST)
- **Description**: Predice las 3 principales tendencias/aspectos relacionados con el texto dado.
- **Request Body**: `{ "text": "otro texto para analizar" }`
- **Response**:
  ```json
  {
    "texto": "otro texto para analizar",
    "top_tendencias": [
      { "aspecto": "citas medicas", "similitud": 75.0 },
      { "aspecto": "enfermeria", "similitud": 60.5 },
      { "aspecto": "urgencias", "similitud": 50.2 }
    ]
  }
  ```

## Funcionalidades de Inicio

### Prerequisitos
- Docker

### Instalación
1. Clonar el repositorio:
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```
2. Construir el contenedor Docker:
   ```sh
   docker build -t sentiment-trend-api .
   ```
3. Ejecutar el contenedor:
   ```sh
   docker run -p 8000:8000 sentiment-trend-api
   ```
4. La API estará disponible en `http://localhost:8000`.

## Uso
- Puede probar los endpoints utilizando herramientas como Postman o cURL- La API esta deplegada en el [enlace](https://sentiment-trend-api-643026306142.us-central1.run.app) para su consumo externo con sus correspondientes endpoints.
- La API esta deplegada en el [enlace](https://sentiment-trend-api-643026306142.us-central1.run.app) para su consumo externo con sus correspondientes endpoints.

## Requisitos
Todas las dependencias están listadas en `requirements.txt`:
- fastapi==0.95.2
- tensorflow==2.12.0
- transformers==4.28.1
- gensim==4.3.1
- numpy==1.24.2
- uvicorn==0.22.0

## Licencia
Este proyecto está licenciado bajo la licencia MIT.

## Contacto
Cristian Fandiño - [cristian9918@hotmail.com](mailto:cristian9918@hotmail.com)

No dudes en abrir un PR si tienes alguna pregunta o sugerencia.