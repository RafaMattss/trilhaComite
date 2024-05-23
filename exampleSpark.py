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

# CRUD Operations
# CREATE - Adicionar novas entradas à tabela
new_data = [("Frank", 36), ("Grace", 32)]
df_new = spark.createDataFrame(new_data, columns)
df_combined = df_filtered.union(df_new)
df_combined.createOrReplaceTempView("pessoas_maiores_30")

# READ - Consultar a tabela SQL
print("Resultados da consulta SQL após CREATE:")
result = spark.sql("SELECT Nome, Idade FROM pessoas_maiores_30")
result.show()

# UPDATE - Atualizar dados na tabela
spark.sql("UPDATE pessoas_maiores_30 SET Idade = 40 WHERE Nome = 'Alice'")
print("Resultados da consulta SQL após UPDATE:")
result = spark.sql("SELECT Nome, Idade FROM pessoas_maiores_30")
result.show()

# DELETE - Excluir dados da tabela
spark.sql("DELETE FROM pessoas_maiores_30 WHERE Nome = 'Daniel'")
print("Resultados da consulta SQL após DELETE:")
result = spark.sql("SELECT Nome, Idade FROM pessoas_maiores_30")
result.show()

# ETL Process
# Extract - Extrair dados do DataFrame original
df_extracted = df

# Transform - Transformar os dados (por exemplo, adicionar 5 anos à idade)
df_transformed = df_extracted.withColumn("Idade", col("Idade") + 5)

# Load - Carregar os dados transformados em uma nova tabela SQL
df_transformed.createOrReplaceTempView("pessoas_transformadas")
print("DataFrame transformado após ETL:")
spark.sql("SELECT * FROM pessoas_transformadas").show()

# Parar a SparkSession
spark.stop()
