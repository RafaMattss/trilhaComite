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

## Introdução ao Apache Hive
O Apache Hive é um sistema de data warehousing e análise de dados construído em cima do Hadoop. Ele facilita a consulta e o gerenciamento de grandes conjuntos de dados armazenados no Hadoop Distributed File System (HDFS) usando uma linguagem semelhante ao SQL, conhecida como HiveQL (Hive Query Language). O Hive foi desenvolvido inicialmente pelo Facebook para lidar com a crescente quantidade de dados que precisavam ser analisados, e hoje é amplamente utilizado por muitas organizações para big data analytics.

## Hive vs. SQL
### Semelhanças
- **Linguagem**: HiveQL, a linguagem de consulta do Hive, é muito similar ao SQL, o que facilita a adoção por desenvolvedores familiarizados com bancos de dados relacionais.
- **Consultas**: Assim como no SQL, o HiveQL permite a execução de operações de consulta, agregação, filtragem e junção de dados.

### Diferenças
- **Execução**: As consultas HiveQL são convertidas em jobs MapReduce, Tez ou Spark, que são executados em um cluster Hadoop. Isso difere do SQL tradicional, onde as consultas são executadas em um servidor de banco de dados.
- **Desempenho**: Devido à natureza distribuída do Hadoop, o Hive é otimizado para leitura de grandes volumes de dados, mas pode ser mais lento para operações de escrita e atualização frequentes.
- **Esquema em Leitura**: O Hive utiliza um conceito de "schema on read", onde o esquema é aplicado aos dados apenas durante a leitura, ao contrário dos bancos de dados relacionais tradicionais que utilizam "schema on write".

## Por Que o Hive Surgiu
O Hive surgiu como uma solução para permitir que usuários familiarizados com SQL pudessem trabalhar com grandes conjuntos de dados armazenados no Hadoop sem precisar escrever código MapReduce. Sua criação foi motivada pela necessidade de:
- **Facilidade de Uso**: Prover uma interface SQL-like para Hadoop, facilitando a adoção e o uso por analistas de dados e engenheiros de dados.
- **Escalabilidade**: Habilitar a análise de grandes volumes de dados, aproveitando a escalabilidade e capacidade de processamento distribuído do Hadoop.
- **Integração**: Permitir a integração com outras ferramentas e frameworks do ecossistema Hadoop, como Pig, HBase e Spark.

## Função do Hive em um Ambiente de Big Data
O Apache Hive desempenha um papel crucial em ambientes de big data, proporcionando uma interface familiar para consulta e análise de dados armazenados no HDFS. Suas principais funções incluem:
- **Data Warehousing**: Hive é frequentemente usado como um data warehouse para armazenar e consultar grandes volumes de dados históricos.
- **ETL**: Hive é usado em processos de ETL (Extract, Transform, Load) para transformar e preparar dados para análise.
- **Análise Ad-hoc**: Permite aos usuários realizar consultas ad-hoc sobre grandes conjuntos de dados para extrair insights e gerar relatórios.
- **Integração com Ferramentas de BI**: Hive pode ser integrado com ferramentas de Business Intelligence (BI) para visualização e análise de dados.
  
## Partições no Hive
### O Que São Partições?
Partições no Hive são uma forma de dividir grandes conjuntos de dados em partes menores, baseadas no valor de uma ou mais colunas. Isso melhora significativamente o desempenho das consultas, pois permite que apenas as partições relevantes sejam lidas e processadas.

### Como Funciona?
Ao criar uma tabela particionada, o Hive armazena os dados em subdiretórios separados no HDFS, cada um correspondente a um valor específico da coluna de partição. Por exemplo, se uma tabela for particionada pela coluna `data`, os dados serão armazenados em subdiretórios como `data=2023-01-01/`, `data=2023-01-02/`, etc.

## Possibilidades e Benefícios ao Usar o Hive
- **Escalabilidade**: Capacidade de processar petabytes de dados distribuídos em um cluster Hadoop.
- **Custo-benefício**: Utiliza hardware comum, reduzindo custos em comparação com soluções de data warehousing tradicionais.
- **Flexibilidade**: Suporte a diversos formatos de dados (e.g., Parquet, ORC, JSON) e integração com outras ferramentas do ecossistema Hadoop.
- **Familiaridade**: A linguagem HiveQL é similar ao SQL, facilitando a curva de aprendizado para profissionais que já conhecem SQL.
- **Extensibilidade**: Hive permite a definição de funções de usuário (UDFs) para estender suas capacidades e personalizar operações de consulta.
- **Processamento em Lote**: Ideal para processamento de dados em lote, aproveitando o modelo de execução MapReduce.

------------------------------------------------------------------------------------------------------------------------------

# Guia para Apache Airflow

## Introdução ao Apache Airflow
O Apache Airflow é uma plataforma open-source para criação, agendamento e monitoramento de fluxos de trabalho programáveis. Desenvolvido originalmente pelo Airbnb, o Airflow permite que você defina seus workflows como código, utilizando o Python para criar pipelines de dados complexos de maneira eficiente e reutilizável. Ele é amplamente utilizado para automação de processos em data engineering e data science.

## Por Que Escolher o Apache Airflow
- **Flexibilidade**: Escreva seus workflows em Python, permitindo fácil integração com bibliotecas e ferramentas do ecossistema Python.
- **Escalabilidade**: Capacidade de escalar horizontalmente, distribuindo a carga de trabalho através de múltiplos nós de execução.
- **Extensibilidade**: Suporte a uma vasta gama de operadores, hooks e executors, além de permitir a criação de plugins personalizados.
- **Monitoramento e Logs**: Interface web intuitiva para monitoramento de tarefas, visualização de logs e gerenciamento de fluxos de trabalho.
- **Comunidade Ativa**: Grande comunidade open-source, garantindo melhorias contínuas, suporte e vasta documentação.

## Principais Conceitos do Apache Airflow

### DAG (Directed Acyclic Graph)
Uma DAG, ou Grafos Acíclicos Dirigidos, é uma coleção de todas as tarefas que você deseja executar, organizadas de uma maneira que reflete suas dependências. Em outras palavras, uma DAG é um grafo que direciona o fluxo de trabalho, onde cada nó representa uma tarefa e as arestas representam as dependências entre essas tarefas. 

### Tarefas (Tasks)
As tarefas são as unidades individuais de trabalho que compõem uma DAG. Elas são instâncias de operadores (Operators) que definem a ação que a tarefa irá executar, como transferência de dados, execução de scripts, ou chamada de APIs.

### Operadores (Operators)
Operadores são classes que encapsulam uma determinada tarefa. Existem diversos tipos de operadores, como `BashOperator` para executar comandos bash, `PythonOperator` para executar funções Python, e `Sensor` para verificar a disponibilidade de uma condição ou recurso.

### Scheduler
O Scheduler é o componente responsável por agendar e distribuir a execução das tarefas conforme definido nas DAGs. Ele monitora as DAGs e garante que as tarefas sejam executadas na ordem correta e no momento adequado.

### Executor
O Executor é a parte do Airflow que executa as tarefas. Existem vários tipos de executores, como o `SequentialExecutor`, `LocalExecutor`, `CeleryExecutor` e `KubernetesExecutor`, cada um oferecendo diferentes níveis de paralelismo e suporte a diferentes arquiteturas de cluster.

## Arquitetura do Apache Airflow
A arquitetura do Airflow consiste em vários componentes principais:
- **Web Server**: Interface gráfica para criação, monitoramento e gerenciamento de DAGs.
- **Scheduler**: Componente que verifica a execução das DAGs e distribui tarefas aos executores.
- **Executor**: Componente que executa as tarefas.
- **Workers**: Nós que realmente realizam o trabalho, executando as tarefas.
- **Metadata Database**: Banco de dados que armazena o estado das DAGs, tarefas e logs de execução.

## O Que é uma DAG e Como Usá-las
### Definição de uma DAG
Uma DAG é definida como um script Python que descreve o conjunto de tarefas e suas dependências. Aqui está um exemplo básico de uma DAG:

```python
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag,
)

t1 >> t2  # Define a dependência: t2 depende de t1
```
-------------------------------------------------------------------------------------------------
# Guia para Apache NiFi

## Introdução ao Apache NiFi
O Apache NiFi é uma plataforma de integração de dados que facilita a automação do fluxo de dados entre sistemas. Ele foi projetado para automação do movimento de dados entre diferentes fontes e destinos, com um foco especial em escalabilidade, segurança e gestão de dados em tempo real. Originalmente desenvolvido pela NSA (Agência de Segurança Nacional dos EUA) e depois doado à Apache Software Foundation, o NiFi é utilizado por empresas para construir pipelines de dados complexos que podem ser monitorados e ajustados em tempo real.

## Como Funciona o Apache NiFi
O NiFi permite a criação de fluxos de dados através de uma interface gráfica, onde os usuários podem arrastar e soltar componentes para definir a lógica de integração de dados. Cada fluxo de dados é composto por uma série de processadores que executam operações específicas nos dados, como leitura, transformação, roteamento e escrita em diferentes sistemas. A comunicação entre esses processadores é gerida por filas que garantem o controle e a manipulação eficiente dos dados.

## Para Que Serve o Apache NiFi
O Apache NiFi é usado para:
- **Ingestão de Dados**: Capturar dados de diversas fontes, incluindo bancos de dados, sistemas de arquivos, APIs, sensores IoT, etc.
- **Transformação de Dados**: Modificar e transformar dados enquanto eles passam pelo fluxo, incluindo limpeza, agregação e formatação.
- **Roteamento de Dados**: Enviar dados para diferentes destinos com base em regras definidas pelo usuário.
- **Monitoramento e Auditoria**: Fornecer visibilidade e rastreamento completo do fluxo de dados, permitindo auditoria e monitoramento em tempo real.
- **Integração de Sistemas**: Conectar diferentes sistemas, aplicações e serviços, permitindo a troca de dados de forma integrada.

## Principais Conceitos do Apache NiFi

### Fluxo de Dados (Data Flow)
Um fluxo de dados no NiFi é a representação gráfica da movimentação e transformação de dados entre fontes e destinos. Ele é composto por diversos componentes interconectados, cada um executando uma tarefa específica.

### Processadores (Processors)
Os processadores são os blocos de construção dos fluxos de dados no NiFi. Cada processador realiza uma função específica, como leitura de dados, transformação, roteamento ou escrita em um destino. Existem processadores pré-definidos para várias tarefas comuns, mas também é possível criar processadores personalizados.

### Conectores (Connections)
Os conectores são os links que conectam processadores, formando o caminho pelo qual os dados fluem. Eles servem como filas que armazenam os dados temporariamente enquanto são transferidos de um processador para outro, permitindo controle de fluxo e buffering.

### Controladores de Serviços (Controller Services)
Os controladores de serviços fornecem configurações compartilhadas que podem ser usadas por múltiplos processadores, como conexões de banco de dados, acesso a APIs externas, ou configurações de segurança.

### Propriedades de Processadores
Cada processador no NiFi possui um conjunto de propriedades configuráveis que definem seu comportamento. Isso inclui parâmetros como fontes de dados, destinos, métodos de transformação, e qualquer outro detalhe necessário para a operação específica do processador.

### Relacionamentos (Relationships)
Os relacionamentos são os caminhos possíveis que os dados podem seguir após serem processados por um processador. Por exemplo, um processador pode ter relacionamentos como "sucesso", "falha", ou "sem correspondência", permitindo o roteamento condicional dos dados.

### Grupos de Processos (Process Groups)
Grupos de processos permitem a organização e modularização dos fluxos de dados. Eles agrupam um conjunto de processadores e conectores em uma única unidade lógica, facilitando a gestão e reutilização de partes complexas do fluxo de dados.

### Templates
Templates são modelos reutilizáveis de fluxos de dados. Eles permitem exportar e importar configurações de fluxos, facilitando a replicação de configurações em diferentes ambientes ou projetos.

### Controle de Fluxo (Flow Control)
O NiFi oferece várias formas de controle de fluxo, incluindo a definição de limites de taxa, tamanho de lote, e priorização de filas, garantindo que o sistema possa lidar com picos de carga e manter a eficiência operacional.

## Exemplo de ingestão de Dados de um Banco de Dados
```markdown
1. **Processor**: `GenerateTableFetch` para ler dados de uma tabela de banco de dados.
2. **Processor**: `ExecuteSQL` para executar a consulta SQL.
3. **Processor**: `PutFile` para salvar os dados em um sistema de arquivos.

**Flow**: `GenerateTableFetch` -> `ExecuteSQL` -> `PutFile` ```


