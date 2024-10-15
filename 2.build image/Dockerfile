FROM ubuntu:24.10

# RUN ["apt","update","&&","apt","install","ncal","-y"]
RUN apt update && apt install ncal -y

WORKDIR /app

COPY file1.txt file2.txt ./

ARG NAME
ENV AGE=28

# RUN rm Dockerfile

EXPOSE 5000

CMD echo $NAME an my age is $AGE

