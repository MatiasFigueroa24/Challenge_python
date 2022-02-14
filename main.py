from fastapi import FastAPI
import requests
import base64
from secrets import *

app = FastAPI()

Access_token = 'BQBl-i5HHjX8rV-NCKbQExW64JObkRErYGR9PpYWKbvujIkrCHE4QOzdPloEquTP_qom87AQlmBmxMGIGd22TDDwblhVjO-9c2gcMoNCLbGEBGb2qxdTWl2yUdfnagD_nJbARXY29mGboQXHlnvP4ZBmhpsGW8bkEhfGYjG1IANXkXhZ'

authURL='https://accounts.spotify.com/api/token'
authHeader = {}
authData= {}

def getAccessToken(clientID, clientSecret):
    message = f"{clientID}:{clientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    authHeader['Authorization'] = "Basic "+ base64_message
    authData['grant_type'] = "client_credentials"
    res = requests.post(authURL,headers=authHeader,data=authData)

    responseObject = res.json()
    accessToken = responseObject['access_token']

    return accessToken

@app.get('/api/v1/albums')
def albums(q: str | None = None):
    #obtenemos el token para realizar la peticion
    get_token = getAccessToken(clientID, clientSecret)

    #buscamos la banda
    url_search_band = 'https://api.spotify.com/v1/search?q='+ q +'&type=artist&limit=1'
    get_Header = {
            'Authorization': 'Bearer ' + get_token
    }
    response_band = requests.get(url_search_band, headers=get_Header)
    json_band = response_band.json()

    #obtenemos el id de la banda
    id_band = ''.join([i['id'] for i in json_band['artists']['items']])

    #Con el ID de la banda obtenemos los albums
    get_date_albums = 'https://api.spotify.com/v1/artists/'+ id_band +'/albums'
    response_date_albums = requests.get(get_date_albums,headers=get_Header)
    json_albums = response_date_albums.json()

    date_albums_json = []
    for list in json_albums['items']:
        #obtenemos los datos de cada albums
        date_albums_json.append({
            "name": list['name'],
            "released": list['release_date'],
            "tracks": list['total_tracks'],
            "cover": {
                "height": list['images'][0]['height'],
                "width": list['images'][2]['width'],
                "url": list['images'][1]['url']
            }
        })

    return date_albums_json
