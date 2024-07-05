FROM node:20-alpine

WORKDIR /vue

COPY package.json /vue/
COPY package-lock.json /vue/

RUN npm install

COPY . /vue/

RUN npm run build

EXPOSE 5173

CMD ["npm", "run", "dev"]
