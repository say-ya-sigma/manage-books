FROM python:3.12
WORKDIR /backend

RUN apt-get update &&\
    apt-get -y install\
    locales\
    curl\
    git\
    bash-completion &&\
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN pip install --upgrade pip

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH /root/.local/bin:$PATH
RUN poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./
COPY docker/backend/.extra_bashrc /root/.extra_bashrc
RUN echo "source /root/.extra_bashrc" >> /root/.bashrc
RUN poetry install
