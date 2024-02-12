FROM node:latest
WORKDIR /usr/src/app
COPY app/package.json .
RUN npm install
COPY app .
CMD [ "node", "app.js" ]
EXPOSE 300
