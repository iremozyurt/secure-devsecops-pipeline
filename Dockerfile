FROM python:3.10-slim 
#Debian tabanlı ,Python hazır,“slim” = küçük image (güvenlik + performans)
WORKDIR /app
#Container içindeki çalışma dizini
RUN apt-get update && apt-get install -y iputils-ping \
    && rm -rf /var/lib/apt/lists/*
#Container OS’ine:, ping komutunu ekledik ,Son satır: image şişmesin diye cache siliyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#Python bağımlılıklarını kurduk
COPY app.py .
#Uygulama kodunu image içine koyduk
CMD ["python", "app.py"]
#Container ayağa kalkınca: app.py çalışsın


#Image
#Kalıp / şablon
#Çalışmıyor
#Read-only

#Image’dan üretilen çalışan instance
#Canlı süreç
#Image = class
#Container = object



#docker build -t devsecops-test .
#Dockerfile’ı okudu
#Her satırı sırayla çalıştırdı
#Sonunda image üretti
#Henüz uygulama çalışmıyor Sadece paketlendi

#docker run -p 5000:5000 devsecops-test
#Image’dan container oluşturur,Çalıştırır,Port açar