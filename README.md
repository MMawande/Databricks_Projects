[Azure+Databricks+Course+Slide+Deck+V4 (1).pdf](https://github.com/MMawande/Databricks_Projects/files/12051868/Azure%2BDatabricks%2BCourse%2BSlide%2BDeck%2BV4.1.pdf)
# Databricks_Projects
Azure Databricks For Data Engineers (Project on Formula 1 Racing![image](https://github.com/MMawande/Databricks_Projects/assets/39480947/55228673-ad2f-4196-82fd-7b9e50c88792)
 About this course
- The primary focus of this course is Azure databricks which is a widely adapted spark based unified data analytics platform optimized for Microsoft cloud.

- Will learn Spark using Spark SQL (PySpark + SparkSQL)

- Learn delta lake , and how we can use delta lake to implement the emerging lakehouse architecture

- Azure Data Lake Storage Gen2 as a storage solution (section)

- Creation of a Data Lake Service for reading & writing data into the Data Lake 

- Azure Data Factory to create schedules and monitor Data Pipelines, creating Pipelines for databricks notebooks, scheduling & monitoring those pipelines (section)
- The course focuses on building production quality data engineering solution so secrets are managed by the Azure Key Vault
- How we can connect to the data in databricks from Power BI to create BI reports


Will be doing a project on building a cloud data platform for reporting and doing analysis of the data from Formula1 Cloud Data Platform



- In this project, will build a Data Lake from Azure, by Ingesting Formula1 race data from an external API.

- We will then Transform this data as required for reporting & analysis purposes and make them available in our Presentation Layer
- We will then Analyse the data for trans using the using Databricks and create the necessary dashboards.

- We will also make the data available for BI reporting & how to access this data from Power BI

- All of this process will be scheduled and triggered by the Azure Data Factory (ADF) Pipelines

- We will then go through the new and emerging Data Lakehouse Architecture & convert our solution to create   a Data Lakehouse using Delta Lake

- Along the way we will do some interesting analysis on the data to identify the most dominant drivers and the teams in the history of formula1.



	1. Azure Portal ->The overview of the Azure Portal
	
	2. Azure Databricks -> Azure Databricks Architecture and the user interface
	
	3. Project Overview ->Includes the overview of the Formula1 Season, the Data, the API & the project 
	Requirements
	
	4. Spark Overview -> Overview of the Spark Architecture as well the Data Frame & the Data Sources API
	
	a. Databricks -> As part of Databricks we have separate sections for -  a) Clusters, b) Notebooks, c) Data Lake Access, d) Security Access to Data Lake, e) Databricks Mounts & f) Databricks Jobs

	b. Spark (Python) -> We use PySpark to Ingest the source data into our Data Lake, during Ingestion we will deal with few types & complexities of data, we have separate sections for those a) - Data Ingestion 1, b) Data Ingestion 2, c) Data Ingestion 3, d) Transformation + filters + seggregations, e) Aggregations, & f) Incremental Load
	
	c. Spark(SQL) -> We have sections on - a) Temp Views and how to access them from PySpark, b) DDL ( creating databases, tables & views), c) DML (inserting data into tables, filters, joins & aggregations), d) Analysis sing Spark SQL, e) Incremental Load - Advanced topic on implementing different design patterns for  data loading in which we will implement  an incremental load pattern (this will be done both using PySpark & SparkSQL)

![image](https://github.com/MMawande/Databricks_Projects/assets/39480947/736ef461-7d92-40be-b7e1-25b5d33e80fc)
