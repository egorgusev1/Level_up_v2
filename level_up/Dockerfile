FROM python:3.13-bullseye AS base
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install gettext -y

RUN mkdir /code

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

FROM base AS development 

RUN poetry install --no-root

RUN poetry run playwright install --with-deps

COPY . .
RUN chmod 755 /code/start-level_up.sh

EXPOSE 8000

ENTRYPOINT ["bash", "/code/start-level_up.sh"]

FROM base AS production

RUN poetry install --only main --no-root

COPY . .
RUN chmod 755 /code/start-level_up.sh

EXPOSE 8000

ENTRYPOINT ["bash", "/code/start-level_up.sh"]



