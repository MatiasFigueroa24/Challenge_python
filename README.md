# Challenge_python
# Description
Utilizando la api de spotify crear un endpoint al que ingresando el nombre de la banda se obtenga un array de toda la discografía, cada disco debe tener este formato:
 
[{
    "name": "Album Name",
    "released": "10-10-2010",
     "tracks": 10,
     "cover": {
         "height": 640,
         "width": 640,
         "url": "https://i.scdn.co/image/6c951f3f334e05ffa"
     }
},
  ...
]
 
El endpoint de consulta debe ser el siguiente: http://localhost/api/v1/albums?q=<band-name>

Consideraciones adicionales:
• Podes usar un microframework (como FastAPI)
• Podes usar libs (como requests)
• No se puede usar ningún SDK de spotify

# Run proyect
uvicorn main:app --reload --host=127.0.0.1 --port=8000
