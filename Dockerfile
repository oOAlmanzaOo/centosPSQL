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
