FROM node:26.4.0

WORKDIR /

RUN git clone https://github.com/smogon/pokemon-showdown.git

WORKDIR /pokemon-showdown

RUN npm install \
    && cp config/config-example.js config/config.js

EXPOSE 8000

CMD [ "node", "pokemon-showdown", "start", "--no-security" ]
