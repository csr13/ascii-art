#syntax=docker/dockerfile:1
FROM python:3.10-alpine3.18

ENV USER=art

RUN apk add --update --no-cache gcc g++ make

RUN addgroup -S art

RUN adduser \
    --shell /bin/sh \
    --home /home/art \
    --gecos "" \
    --ingroup "$USER" \
    --disabled-password \
    -G wheel \
    "$USER"

WORKDIR /home/art/src

RUN chown -R art:art /home/art/src

COPY --chown=art:art requirements.txt .

RUN python3 -m pip install wheel && \
    python3 -m pip install -r requirements.txt

COPY --chown=art:art --chmod=700 docker/entrypoint.sh entrypoint.sh

COPY --chown=art:art src .

RUN if [ ! -d images ]; then mkdir images; fi && if [ ! -d output ]; then mkdir output; fi 

RUN chmod +x entrypoint.sh

USER art

ENTRYPOINT ["/home/art/src/entrypoint.sh"]

CMD ["/bin/echo", "-h"]
