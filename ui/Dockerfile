FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /ui

COPY . .

RUN npm install
RUN npm run build

EXPOSE 4173
CMD ["npm", "run", "preview", "--", "--host"]