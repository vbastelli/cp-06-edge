# Projeto: Visualizador de Dados MQTT com Dash e ESP32
Este projeto consiste em dois componentes principais: uma aplicação **Dash** para visualização de dados de sensores e um código **ESP32** para coleta e envio desses dados via MQTT para um broker. Os dados visualizados incluem luminosidade, temperatura e umidade. O sistema é capaz de se conectar a um broker MQTT, receber os dados dos sensores e exibi-los em gráficos interativos.
## Sumário
- [Descrição](#descrição)
- [Pré-requisitos](#pré-requisitos)
- [Configuração do Dash](#configuração-do-dash)
- [Configuração do ESP32](#configuração-do-esp32)
- [Estrutura de Arquivos](#estrutura-de-arquivos)
- [Captura de Tela do Dashboard](#captura-de-tela-do-dashboard)
- [Licença](#licença)
---
## Descrição
A aplicação Dash exibe dados coletados por um ESP32 conectado a sensores de luminosidade, temperatura e umidade. Esses dados são enviados via MQTT para um broker, onde o Dash coleta e exibe as informações em gráficos interativos.
O ESP32 coleta dados periódicos e publica em tópicos MQTT específicos. O Dash faz a assinatura desses tópicos, recebendo os dados e atualizando os gráficos a cada 10 segundos.
## Pré-requisitos
### Para rodar o Dash:
- **Python 3.x**
- Bibliotecas Python necessárias (instale com `pip install`):
 - `dash`
 - `plotly`
 - `paho-mqtt`
### Para rodar no ESP32:
- **ESP32**
- **Arduino IDE** com suporte para ESP32
- Bibliotecas Arduino necessárias:
 - `WiFi.h`
 - `PubSubClient.h`
 - `DHT.h`
---
## Configuração do Dash
1. Clone o repositório:
  git clone https://github.com/vbastelli/cp-06-edge.git
  cd cp-06-edge
2. Instale as dependências:
pip install dash plotly paho-mqtt

3. Edite as variáveis do broker MQTT no arquivo Python para refletir seu ambiente:
BROKER_MQTT = "34.203.196.154"  # IP do Broker MQTT
BROKER_PORT = 1883              # Porta do Broker

4. Execute a aplicação:
python app.py

Configuração do ESP32
1. Abra o Arduino IDE e carregue o código ESP32 disponível no diretório esp32/.
2. Edite as credenciais da rede Wi-Fi e do broker MQTT:
const char* default_SSID = "FIAP-IBM";               // Nome da rede Wi-Fi
const char* default_PASSWORD = "Challenge@24!";      // Senha da rede Wi-Fi
const char* default_BROKER_MQTT = "34.203.196.154";  // IP do Broker MQTT

3. Conecte o ESP32 e faça o upload do código.
Estrutura de Arquivos
├── app.py                  # Código da aplicação Dash
├── esp32/
│   └── esp32_sensor_code.ino  # Código para o ESP32
├── README.md


##Imagem do dashboard
![image](https://github.com/user-attachments/assets/34401c12-1302-4897-b1f3-8a98bc3a82c5)
