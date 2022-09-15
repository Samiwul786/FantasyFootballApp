FROM python:3.8-alpine




# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
COPY . /app



# switch the working directory
WORKDIR /app


# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py"]
