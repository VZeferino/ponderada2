# ROS2 Chatbot

Bem-vindo ao Chatbot do Vitor para o Inteli!

Este projeto implementa um chatbot simples que interpreta comandos relacionados a movimentação em um ambiente fictício (A faculdade).

## Instalação

Clone este repositório, faça o build, coloque o source e rode o nó:

```bash
git clone https://github.com/VZeferino/ponderada2.git

cd ~/src/chatbot
colcon build

source ~/install/local_setup.bash #ou zsh
ros2 run chatbot guia
```

Siga as instruções apresentadas no terminal para interagir com o chatbot.

## Funcionamento
O chatbot aceita comandos como "Vá para...", "Dirija-se ao...", e "Me leve para...", interpretando a intenção do usuário e executando a ação associada.

[Vídeo de referência da minha solução](https://youtu.be/iFKid0hrY1g)
