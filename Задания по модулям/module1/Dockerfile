FROM openjdk:11-slim AS build

RUN apt-get update && apt-get install -y maven && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN mvn clean package

FROM openjdk:11-jre-slim

WORKDIR /app

COPY --from=build /app/target/ipcounter-1.0.1.jar /app/ipcounter-1.0.1.jar

CMD ["java", "-jar", "/app/ipcounter-1.0.1.jar", "/app/ip_addresses.txt", "False"]
