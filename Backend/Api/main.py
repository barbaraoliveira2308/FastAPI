from fastapi import FastAPI, HTTPException, Depends, Query, status
from typing import List
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from pydantic import BaseModel
from fastapi.security import OAuth2AuthorizationCodeBearer
from typing import List
from dotenv import load_dotenv
import os
import sys
sys.path.append(r'C:\Users\barbara.oliveira\OneDrive - Evoleo Technologies, Lda\Desktop\Projeto API\Backend')




app = FastAPI()


load_dotenv(dotenv_path= 'Variaveis.env')


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl=
    authorizationUrl=,
)

#variaveis auth

auth0_domain = os.getenv("AUTH0_DOMAIN")
auth0_client_id = os.getenv("AUTH0_CLIENT_ID")
auth0_client_secret_key = os.getenv("AUTH0_CLIENT_SECRET")
auth0_app_secret_key = os.getenv("APP_SECRET_KEY")





class SensorData(BaseModel):
    timestamp: str
    antenna: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    incline_angle: float

# Inicialize o cliente InfluxDB
token = ""
org = ""
bucket = ""











stored_sensor_data: List[SensorData] = []


def fetch_data_from_db(client, query, org):
    try:
        tables = client.query_api().query(query, org=org)
        result = []
        for table in tables:
            for record in table.records:
            
                result.append(record.values) 
                
        return result
       
    except Exception as e:
        print(f"Falha na execução da consulta InfluxDB. Erro: {e}")
        # Remova a linha abaixo se não quiser imprimir a variável tables no caso de erro

        raise e

# Exemplo de uso:
def main():
    # Substitua a consulta abaixo pela consulta específica que você deseja realizar
    db_query = 'from(bucket:"Bucket02") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "sensor_data")'

    # Substitua os valores de 'influx_db' e 'org' pelos valores corretos
    data_from_db = fetch_data_from_db(client, db_query, org)

    # Exiba ou manipule os dados conforme necessário
    print("Dados obtidos do banco de dados:")
    print(data_from_db)

# Chama a função principal
if __name__ == "__main__":
    main()








@app.post("/webhook")
async def receive_sensor_data(sensor_data: SensorData):
    # Lógica para processar os dados recebidos, como salvar no banco de dados, etc.
    # Você pode acessar os dados através de sensor_data.timestamp, sensor_data.antenna, etc.
    stored_sensor_data.append(sensor_data)
    return {"status": "Data received successfully"}

'''
@app.get("/influx_data",  response_model=List[SensorData],dependencies=[Depends(oauth2_scheme)]) 
async def fetch_data_from_db(client, query, org):
    try:
        tables = client.query_api().query(query, org=org)
        result = []
        for table in tables:
            for record in table.records:
            
                result.append(record.values) 
                
        return result
       
    except Exception as e:
        print(f"Falha na execução da consulta InfluxDB. Erro: {e}")
        # Remova a linha abaixo se não quiser imprimir a variável tables no caso de erro

        raise e

# Exemplo de uso:
def main():
    # Substitua a consulta abaixo pela consulta específica que você deseja realizar
    db_query = 'from(bucket:"Bucket02") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "sensor_data")'

    # Substitua os valores de 'influx_db' e 'org' pelos valores corretos
    data_from_db = fetch_data_from_db(client, db_query, org)

    # Exiba ou manipule os dados conforme necessário
    print("Dados obtidos do banco de dados:")
    print(data_from_db)

# Chama a função principal
if __name__ == "__main__":
    main()


'''





@app.get("/sensor_data/", response_model=List[SensorData],dependencies=[Depends(oauth2_scheme)])
async def get_sensor_data(
    antenna: str = Query(None, description="Filtrar por antena"),
    latitude: float = Query(None, description="Filtrar por latitude"),
    longitude: float = Query(None, description="Filtrar por longitude"),
    temperature_gt: float = Query(None, description="Filtrar por temperatura maior que"),
    temperature_lt: float = Query(None, description="Filtrar por temperatura menor que"),
    incline_angle: float = Query(None, description="Filtrar por temperatura menor que"),
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
        if incline_angle and data.incline_angle != incline_angle:
            continue
  


        # Se todos os filtros passarem, adiciona aos dados filtrados
        filtered_data.append(data)

    # Retorna os dados após o loop
    return filtered_data
    print(filtered_data)
