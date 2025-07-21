1. docker build -t ipaddr .
2. docker run --rm -v "$(pwd)/ip_addresses.txt:/app/ip_addresses.txt" ipaddr
3. kubectl apply -f tomcat.yml
4. Starting service [Catalina]
5. Apache Tomcat/9.0.98
6. Значение переменных:
HOSTNAME=tomcat-f98d9b9c-qpptb
JAVA_HOME=/opt/java/openjdk
LANG=en_US.UTF-8
CATALINA_HOME=/usr/local/tomcat
KUBERNETES_PORT_443_TCP_PROTO=tcp