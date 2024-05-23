# pip install pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Iniciar uma SparkSession
spark = SparkSession.builder \
    .appName("Exemplo Spark DataFrame para SQL") \
    .getOrCreate()

# Criar um DataFrame exemplo
data = [
    ("Alice", 34),
    ("Bob", 45),
    ("Catherine", 29),
    ("Daniel", 35),
    ("Evelyn", 25)
]

# Definir esquema das colunas
columns = ["Nome", "Idade"]

# Criar DataFrame
df = spark.createDataFrame(data, columns)

# Exibir o DataFrame
print("DataFrame original:")
df.show()

# Realizar uma transformação: filtrar pessoas com idade acima de 30
df_filtered = df.filter(col("Idade") > 30)

print("DataFrame após filtragem (Idade > 30):")
df_filtered.show()

# Registrar o DataFrame como uma tabela SQL temporária
df_filtered.createOrReplaceTempView("pessoas_maiores_30")

# Consultar a tabela SQL
print("Resultados da consulta SQL:")
result = spark.sql("SELECT Nome, Idade FROM pessoas_maiores_30")
result.show()

# Parar a SparkSession
spark.stop()
