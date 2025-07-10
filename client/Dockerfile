# ./client/Dockerfile
FROM node:16-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Only copy package.json and lock file first to cache dependencies
COPY package*.json ./

RUN npm install

# Now bring in the rest of the app
COPY . .

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 3000

CMD ["npm", "start"]
