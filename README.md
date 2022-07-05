# Challenge Data Engineer

**Description:**

The project consists to design the database based on the files attached, ingest the files attached into the postgres database and build a REST API to get the records from the database. At the end of this page, you will find docker-compose templates to get you started immediately with postgres and a centos instance where you can load the files. You can choose the programming language to develop the code.

**The core functionality for this challenge is:**

1. Design the E-R from the database and create the structure based on the files attached. 
2. Ingest the data from the centos server to the postgres database. 
3. At least the 'read' request must be supported for the API 
4. The server where the API is going to be deployed must have access only to the postgres database. And the centos server must have access only to the postgres database as well.

**Some optional functionalities you can implement:**

1. Validate the column state has a length of 2 and only contains letters. 
2. Your code could run on Docker as well. 
3. Support more request than just 'read', like 'create' or 'update'. 
4. Unit test and coverage of your code 
5. Implement CI/CD 
6. Implement a mechanism to create or update the schema

## E-R from the database

![image](https://user-images.githubusercontent.com/61101012/177243890-fd014caa-fd9a-4a5a-bb27-cac7708b154e.png)

## DDL

```SQL
CREATE TABLE public.samples (
  first_name varchar(50) NOT NULL,
  last_name varchar(50) NOT NULL,
  company_name varchar(50) NULL,
  address varchar(50) NULL,
  city varchar(50) NULL,
  state varchar(2) NULL,
  zip varchar(50) NULL,
  phone1 varchar(50) NULL,
  phone2 varchar(50) NULL,
  email varchar(50) NULL,
  department varchar(50) NOT NULL,
  CONSTRAINT samples_pkey PRIMARY KEY (first_name, last_name, department),
  CONSTRAINT samples_state_check CHECK (((char_length((state)::text) > 0) AND (char_length((state)::text) < 3) AND ((state)::text ~ '[A-Za-z]{2}'::text)))
);
```

## Ingest the data from the centos server to the postgres database

![image](https://user-images.githubusercontent.com/61101012/177244595-f8d4c125-aa91-405f-9a65-6f5bcd50071b.png)

## Read API

![image](https://user-images.githubusercontent.com/61101012/177244806-9b41cfb6-87d2-4d75-9fa3-66215f3aada3.png)

## Connection postgresql  with centos and API

![image](https://user-images.githubusercontent.com/61101012/177244961-d22c67c8-52b9-45f0-b7df-83800272b3c3.png)

![image](https://user-images.githubusercontent.com/61101012/177245279-e00bec29-328c-470d-9aca-5a761462bc1a.png)

## Validate the column state has a length of 2 and only contains letters

![image](https://user-images.githubusercontent.com/61101012/177245498-e9347bc5-309c-4806-9859-aaca85c7d072.png)

![image](https://user-images.githubusercontent.com/61101012/177245596-37c2d113-e04a-4447-aeb4-1de30df1f552.png)

## Run on Docker

**Dockerfile:**

```Dockerfile
# Imagen oficial Python 3.8
FROM python:3.8

# Work Directory
WORKDIR /app

# Copiar codigo del proyecto en el work directory
COPY requirements.txt ./

# Actualizar pip
RUN pip install --upgrade pip

# Instalar dependencias del proyecto
RUN pip --no-cache-dir install -r requirements.txt

# Copiar codigo del proyecto en el work directory
COPY . /app

# Correr la aplicacion
CMD ["uvicorn", "app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "4000"]
```

## Support more request than just 'read', like 'create' or 'update'

![image](https://user-images.githubusercontent.com/61101012/177246974-4537f1c1-8e8c-4662-b009-b62689887edf.png)
