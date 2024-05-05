from dotenv import load_dotenv
from influxdb_client import InfluxDBClient


# Variáveis de ambiente
load_dotenv(dotenv_path="Backend\\Generator\\Influx_variaveis.env")

 #Configuração do cliente InfluxDB



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


