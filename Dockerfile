#syntax=docker/dockerfile:1
FROM python:3.10

WORKDIR /src

COPY docker/entrypoint.sh entrypoint.sh

COPY requirements.txt .

COPY src .

RUN if [ ! -d images ]; then mkdir images; fi && if [ ! -d output ]; then mkdir output; fi 

RUN python3 -m pip install -r requirements.txt

RUN chmod +x entrypoint.sh

RUN apt-get update -y && \
    apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6

ENTRYPOINT ["/src/entrypoint.sh"]

CMD ["/bin/echo", "-h"]
