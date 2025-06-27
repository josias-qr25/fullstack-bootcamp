# ./client/Dockerfile
FROM node:16-alpine

WORKDIR /app

# Only copy package.json and lock file first to cache dependencies
COPY package*.json ./

RUN npm install

# Now bring in the rest of the app
COPY . .

EXPOSE 3000

CMD ["npm", "start"]
