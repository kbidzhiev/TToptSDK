FROM python:3.12-bookworm

RUN mkdir -p /ttoptSDK

WORKDIR /ttoptSDK

COPY . .

COPY ./examples/python/example1.py /home/


ENV VIRTUAL_ENV=/ttoptSDK/

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /ttoptSDK
RUN pip install -e .

# Set the working directory in the container
WORKDIR /home/
# Run the application:
CMD ["/bin/bash"]