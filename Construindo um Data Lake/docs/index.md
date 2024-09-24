# Construindo um Data Lake

Este projeto tem como objetivo construir um Data Lake escalável e eficiente usando serviços da AWS, para armazenar, processar e analisar grandes volumes de dados estruturados e não estruturados. O Data Lake foi projetado para suportar diferentes fontes de dados e servir como base para análises avançadas e machine learning.

### Objetivos:

* Criar um repositório centralizado de dados, integrando fontes de dados variadas.
* Implementar um fluxo automatizado de ingestão e processamento de dados.
* Facilitar o acesso a dados limpos e estruturados para análises em tempo real e relatórios.
* Garantir segurança e controle de acesso a dados sensíveis.

### Tecnologias Utilizadas:

* AWS S3: Para armazenamento escalável de dados.
* AWS IAM: Para controle de acesso e segurança.
* Python: Para scripts de integração e automação de tarefas.

### Etapas do Projeto:

1- Criação do bucket no S3: Definir a estrutura de armazenamento e camadas (raw, curated, trusted) para dados brutos, transformados e prontos para uso.
2 - Ingestão de dados: Automatizar a coleta de dados de múltiplas fontes (bancos de dados, APIs e arquivos).
3 - Transformação de dados: Usar o AWS Glue para limpar, transformar e catalogar os dados.
4 - Consulta e análise: Utilizar o AWS Athena para executar consultas SQL diretamente nos dados armazenados no S3.
5 - Segurança e Governança: Configurar permissões de acesso usando IAM, criptografia de dados e monitoramento com AWS CloudWatch.

### Resultados:

*Data Lake funcional capaz de ingerir e processar dados de forma automatizada.
*Redução do tempo de acesso a dados de múltiplas fontes.
*Plataforma escalável para futuras implementações de pipelines de machine learning e análise avançada.