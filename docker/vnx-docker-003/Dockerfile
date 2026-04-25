FROM node:20-slim
WORKDIR /app
ARG DB_PASSWORD=supersecret123
ENV API_TOKEN=tok_live_abc123
COPY . .
RUN npm install
USER node
CMD ["node", "server.js"]
