FROM debian:latest

USER root

RUN apt update  && \ 
    apt upgrade -y && \
    apt install -y wget sudo git
RUN wget https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb

RUN apt update && \
   sudo apt install -y dotnet-sdk-8.0 && \
   sudo apt install -y aspnetcore-runtime-8.0 dotnet-runtime-8.0

WORKDIR /app
RUN git clone https://github.com/Aif4thah/VulnerableLightApp.git
WORKDIR /app/VulnerableLightApp
CMD ["dotnet", "run" , "--url=https://0.0.0.0:3000" ]
