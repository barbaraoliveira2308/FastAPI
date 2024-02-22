'''from fastapi import FastAPI, Query, Depends, HTTPException, Header
from pydantic import BaseModel, ValidationError
from typing import List
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:3000"],  # Adicione o URL do seu frontend aqui
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SensorData(BaseModel):
    timestamp: str
    antenna: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    incline_angle: float


# Lista para armazenar dados simulados (você pode substituir por seus dados reais do sensor)
stored_sensor_data: List[SensorData] = []

# Configurando OAuth2 com tokenUrl e authorizationUrl
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl="OAuth2AuthorizationCodeBearer",  # Substitua com a URL onde você lida com a obtenção do token
    authorizationUrl="http://127.0.0.1:8000/sensor_data/",
      # Substitua com a URL onde você lida com a autorização
    # Substitua com a URL onde você lida com a autorização
)


class LoginPage(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    mensagem: str
  



@app.post("/login", response_model=dict)
async def login_page(username: str, password: str):
    if username == "usario" and password == "password":
    # Lógica de autenticação, se necessário, pode ser adicionada aqui
      return {"mensagem": "login bem sucedido"}

    else: 
        raise HTTPException(status_code=401, detail= "credenciais invalidas")



@app.get("/login/username/password", response_model=LoginResponse)
async def login_page(username: str, password: str):
    if username == "usuario" and password == "password":
        # Lógica de autenticação, se necessário, pode ser adicionada aqui
        return {"mensagem": "login bem sucedido"}
    else: 
        raise HTTPException(status_code=401, detail="credenciais invalidas")


    


@app.post("/webhook")
async def receive_sensor_data(sensor_data: SensorData):
   
    # Lógica para processar os dados recebidos, como salvar no banco de dados, etc.
    # Você pode acessar os dados através de sensor_data.timestamp, sensor_data.antenna, etc.
    stored_sensor_data.append(sensor_data)
    return {"status": "Data received successfully"}





# Rota protegida que usa o esquema OAuth2
@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    return {"token": token}




@app.get("/sensor_data", response_model=List[SensorData])
async def get_sensor_data():
    url = "http://127.0.0.1:8000/sensor_data"
    headers = {"tokenUrl": OAuth2AuthorizationCodeBearer}
    # Retorna os dados armazenados até agora
    return stored_sensor_data 



@app.get("/sensor_data/", response_model=List[SensorData])
async def get_sensor_data(
    antenna: str = Query(None, description="Filtrar por antena"),
    latitude: float = Query(None, description="Filtrar por latitude"),
    longitude: float = Query(None, description="Filtrar por longitude"),
    temperature_gt: float = Query(None, description="Filtrar por temperatura maior que"),
    temperature_lt: float = Query(None, description="Filtrar por temperatura menor que"),
):
    url = "http://127.0.0.1:8000/sensor_data/"
    headers = {"tokenUrl": OAuth2AuthorizationCodeBearer}
    filtered_data = []

    for data in stored_sensor_data:
        # Aplicar filtros
        if antenna and data.antenna != antenna:
            continue
        if latitude and data.latitude != latitude:
            continue
        if longitude and data.longitude != longitude:
            continue
        if temperature_gt and data.temperature <= temperature_gt:
            continue
        if temperature_lt and data.temperature >= temperature_lt:
            continue

        # Se todos os filtros passarem, adiciona aos dados filtrados
        filtered_data.append(data)

    # Retorna os dados após o loop
    return filtered_data
    print(filtered_data)


# Função de autenticação
async def authenticate_user(username: str, password: str):
    # Adicione a lógica de autenticação aqui
    # Retorne True se a autenticação for bem-sucedida, False caso contrário
    return username == "example" and password == "example_password"


'''








'''
url=os.getenv("INFLUXDB_HOST")
port=int(os.getenv("INFLUXDB_PORT", 8086))
username=os.getenv("INFLUXDB_USER")
password=os.getenv("INFLUXDB_PASSWORD")
influx_db=os.getenv('INFLUXDB_DB')
org=os.getenv('INFLUX_ORG')


client = InfluxDBClient(org='INFLUX_ORG',influx_db='INFLUXDB_DB',username='INFLUXDB_USER', password="INFLUXDB_PASSWORD", url='INFLUXDB_HOST' )

def write_sensor_data_to_influxdb(client, sensor_data):
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket="Bucket02", record=sensor_data)


'''
