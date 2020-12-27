# HereIam
This was a small project I built in March 2019 to play with Here APIs, serverless (AWS Lambda and Google Firestore) & Vue.js. Very quick hack for a demo. 

## Client

### Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

### front-end configuration

You will need to create two configuration environment files, one for production (client/config/prod.env.js), one for dev (client/config/dev.env.js)
```
NODE_ENV: '"production"',
FIREBASE_API_KEY: '" "',
FIREBASE_AUTH_DOMAIN: '" Auth Domain you will get from your firestore db"',
FIREBASE_DATABASE_URL: '"URL of your firestore database"',
FIREBASE_PROJECT_ID: '"Firestore project ID"',
FIREBASE_STORAGE_BUCKET: '"Storage Bucket of your firestore project"',
FIREBASE_MESSAGING_SENDER_ID: '""',
HERE_APP_ID: '"the app ID you will get from HERE to use API"',
HERE_APP_CODE: '"the code you will get from HERE to use API"'
```

## Back-end

The back-end is a Lambda function with a layer. To build the Lambda layer, you need Docker client running on your workstation. Run 
```./backend/layer/get_layer_packages.sh``` 
It will create a ZIP file to upload on your AWS account as a Lamda layer. 