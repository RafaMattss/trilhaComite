# Trilha de Aprendizagem
Trilha de conhecimento a ser apresentada no comitê do dia 27/05

# Guia para Google Cloud Platform (GCP)

## Introdução ao Google Cloud Platform (GCP)
O Google Cloud Platform (GCP) é um conjunto de serviços de computação em nuvem oferecido pelo Google. Ele proporciona uma infraestrutura robusta e flexível para desenvolvimento, implantação e gestão de aplicações e serviços na nuvem. Com uma vasta gama de serviços, o GCP é ideal para empresas de todos os tamanhos, proporcionando escalabilidade, segurança e inovação contínua.

## Conceitos Básicos do GCP

### Zonas e Regiões
- **Regiões**: Uma região é uma localização geográfica específica onde você pode hospedar seus recursos. Cada região é composta por várias zonas.
- **Zonas**: Uma zona é um local de implantação isolado dentro de uma região. A configuração multi-zonal oferece alta disponibilidade e redundância.

### Compute Engine
O **Compute Engine** é o serviço de infraestrutura como serviço (IaaS) do GCP. Ele permite a criação de máquinas virtuais (VMs) altamente personalizáveis e escaláveis. As principais características incluem:
- **Vários tipos de máquinas**: Otimizadas para computação, memória ou armazenamento.
- **Instâncias preemptivas**: Instâncias de curto prazo a preços mais baixos.
- **Grupos de instâncias gerenciadas**: Facilita a escalabilidade automática e a manutenção de suas VMs.

### Kubernetes Engine (GKE)
O **Google Kubernetes Engine (GKE)** é um serviço gerenciado para a implantação, gestão e escalabilidade de aplicações em contêineres usando Kubernetes. Benefícios do GKE incluem:
- **Gerenciamento automatizado**: Atualizações e manutenção de clusters.
- **Escalabilidade**: Ajuste automático da capacidade com base na demanda.
- **Segurança**: Integração com serviços de segurança do Google, como IAM e VPC.

### Serviços de Banco de Dados

#### Cloud SQL
O **Cloud SQL** é um serviço gerenciado para bancos de dados relacionais, compatível com MySQL, PostgreSQL e SQL Server. Ele oferece:
- **Backup e recuperação automáticos**: Proteção contra perda de dados.
- **Alta disponibilidade**: Replicação multi-zonal para failover automático.
- **Escalabilidade**: Ajuste de recursos conforme necessário.

#### Firestore e Bigtable
- **Firestore**: Um banco de dados NoSQL de documentos, escalável e de alta performance, ideal para aplicações móveis e web.
- **Bigtable**: Um banco de dados NoSQL escalável para grandes volumes de dados analíticos e operacionais.

## Outros Serviços e Conceitos Importantes

### Cloud Storage
O **Cloud Storage** é um serviço de armazenamento de objetos unificado, ideal para armazenar e acessar dados não estruturados. Ele oferece:
- **Classes de armazenamento**: Otimização de custo com diferentes classes de armazenamento (Standard, Nearline, Coldline, Archive).
- **Segurança**: Criptografia automática e gerenciamento de chaves.

### BigQuery
O **BigQuery** é um serviço de análise de dados totalmente gerenciado e sem servidor. Ele permite consultas SQL em grandes conjuntos de dados, proporcionando:
- **Alta performance**: Consultas rápidas e escaláveis.
- **Facilidade de uso**: Integração com ferramentas de BI e suporte a SQL padrão.

### Operações no GCP

#### Monitoramento e Logging
- **Stackdriver**: Uma suíte de ferramentas para monitoramento, logging e diagnóstico de suas aplicações e infraestrutura. Inclui:
  - **Logging**: Coleta e armazenamento de logs.
  - **Monitoring**: Monitoramento de métricas e alertas.
  - **Trace**: Rastreamento de solicitações para identificar gargalos.

#### IAM (Identity and Access Management)
O **IAM** permite gerenciar acesso a recursos do GCP de forma granular. Ele oferece:
- **Papéis e permissões**: Controle detalhado sobre quem pode fazer o quê.
- **Autenticação e autorização**: Integração com sistemas de identidade para autenticação segura.

-----------------------------------------------------------------------------------------------------------

# Guia para Apache Spark

## Introdução ao Apache Spark
O Apache Spark é uma poderosa ferramenta de processamento de dados em larga escala, projetada para análise de dados rápida e eficiente. Ele oferece suporte para tarefas de processamento de dados em tempo real e em lote, sendo uma escolha popular para empresas que precisam lidar com grandes volumes de dados de forma rápida e eficiente.

## Hadoop e Apache Spark
### O que é Hadoop?
O Hadoop é um framework de código aberto que permite o processamento distribuído de grandes conjuntos de dados através de clusters de computadores. Ele é composto por dois componentes principais:
- **HDFS (Hadoop Distributed File System)**: Um sistema de arquivos distribuído que armazena dados em clusters.
- **MapReduce**: Um modelo de programação para processamento de dados em paralelo.

### Interação entre Hadoop e Spark
Embora o Hadoop tenha sido uma solução dominante para big data, o Apache Spark tem ganhado popularidade devido à sua capacidade de processar dados mais rapidamente. O Spark pode ser executado no Hadoop YARN, usando HDFS para armazenamento de dados. Isso permite que o Spark utilize a infraestrutura de Hadoop existente, oferecendo um processamento mais rápido e flexível.

## Conceitos de Análise de Dados com Apache Spark

### RDD (Resilient Distributed Dataset)
O **RDD** é a principal abstração do Spark. Ele representa uma coleção de objetos distribuídos, imutáveis e tolerantes a falhas, que podem ser processados em paralelo. RDDs suportam duas operações principais:
- **Transformações**: Operações que produzem um novo RDD, como `map` e `filter`.
- **Ações**: Operações que retornam um valor ao driver, como `count` e `collect`.

### DataFrames e Datasets
- **DataFrames**: Uma coleção distribuída de dados organizados em colunas, similar a uma tabela em um banco de dados relacional. Eles oferecem otimizações de desempenho através do Catalyst optimizer.
- **Datasets**: Uma versão tipada dos DataFrames que fornece a segurança de tipos no tempo de compilação, combinando as vantagens do RDD com a otimização do Catalyst.

### Spark SQL
O **Spark SQL** permite consultas SQL sobre dados estruturados e semiestruturados. Ele pode ser usado com DataFrames e oferece suporte a várias fontes de dados, incluindo:
- **Hive**: Integração com o metastore do Hive para consulta e gerenciamento de dados.
- **Parquet e ORC**: Formatos de armazenamento colunares otimizados para análise de dados.

### Análise de Dados em Tempo Real com Spark Streaming
O **Spark Streaming** permite o processamento de fluxos de dados em tempo real. Ele divide os fluxos contínuos de dados em pequenos lotes e os processa em intervalos de tempo. Com Spark Streaming, você pode realizar tarefas como:
- **Processamento de logs em tempo real**.
- **Detecção de fraudes**.
- **Monitoramento de sistemas em tempo real**.

## Bancos de Dados para Spark SQL

### Hive
O **Hive** é uma infraestrutura de data warehousing construída sobre o Hadoop, que facilita a consulta e o gerenciamento de grandes conjuntos de dados armazenados no HDFS. Com a integração do Spark SQL, as consultas Hive podem ser aceleradas pelo Spark.

### HBase
O **HBase** é um banco de dados NoSQL que funciona em cima do HDFS, oferecendo leitura e escrita rápida de dados grandes. Ele pode ser usado junto com o Spark para análises em tempo real e processamento de dados de alta velocidade.

### Cassandra
O **Cassandra** é um banco de dados NoSQL distribuído e altamente escalável, adequado para lidar com grandes volumes de dados. O Spark pode se conectar ao Cassandra para realizar consultas rápidas e processamento de dados distribuídos.

-------------------------------------------------------------------------------------------------------------------------


# Hive
Análise de banco de dados

# Air Flow
Rotina de dev fodasse

# Nefe
Interface gráfica de análise

## Alguma pergunta????
## Obrigado
