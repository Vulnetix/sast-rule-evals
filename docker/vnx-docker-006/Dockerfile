# vnx-docker-006 eval target: ADD instead of COPY for local files
FROM node:20-alpine

WORKDIR /app

ADD package.json .  # TRIGGERS rule (local file, should be COPY)
ADD src/ ./src/     # TRIGGERS rule (local directory, should be COPY)

RUN npm install

CMD ["node", "src/index.js"]
