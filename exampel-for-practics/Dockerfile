FROM node:16-alpine

WORKDIR site
RUN wget https://js-dos.com/6.22/current/js-dos.js && \ 
    wget https://js-dos.com/6.22/current/wdosbox.js && \    
    wget https://js-dos.com/6.22/current/wdosbox.wasm.js
RUN npm install -g serve


ARG GAME_URL
RUN wget -O game.zip $GAME_URL

ARG GAME_ARGS
COPY index.html .
RUN sed -i s/GAME_ARGS/$GAME_ARGS/ index.html

ENTRYPOINT npx serve -l tcp://0.0.0.0:8000

# # pacman
# --build-arg GAME_TAG=pacman
# --build-arg GAME_URL=https://code.s3.yandex.net/Kubernetes/pacman.zip?etag=914e810db328253ff2db6073036ea032
# --build-arg GAME_ARGS=PACMAN.exe

# # bomberman
# --build-arg GAME_TAG=bomberman
# --build-arg GAME_URL=https://code.s3.yandex.net/Kubernetes/dyna.zip
# --build-arg GAME_ARGS=dyna.exe

# # keen
# --build-arg GAME_TAG=keen
# --build-arg GAME_URL=https://code.s3.yandex.net/Kubernetes/Keen.zip?etag=43ee6d837c7551ab400ef8ea2c19c4da
# --build-arg GAME_ARGS=KEEN.BAT

# # doom
# --build-arg GAME_TAG=doom
# --build-arg GAME_URL=https://code.s3.yandex.net/Kubernetes/Doom2.zip?etag=45dffe4dc2664b8c59302590cfc81a9b
# --build-arg GAME_ARGS=DOOM.EXE

# # scorch
# --build-arg GAME_TAG=scorch
# --build-arg GAME_URL=https://code.s3.yandex.net/Kubernetes/Scorcher.zip?etag=99ccc295530ac9608d7b9e9fac0e9d0d
# --build-arg GAME_ARGS=SCORCH.EXE 