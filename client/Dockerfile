FROM node:latest

WORKDIR /usr/app

COPY package*.json ./

RUN npm ci 

COPY . .

CMD ["npm", "run", "dev"]