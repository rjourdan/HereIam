import firebase from 'firebase/app'
import 'firebase/firestore'
import 'firebase/auth'

  // Initialize Firebase
  var config = {
    apiKey: process.env.FIREBASE_API_KEY,
    authDomain: process.env.FIREBASE_AUTH_DOMAIN,
    databaseURL: process.env.FIREBASE_DATABASE_URL,
    projectId: process.env.FIREBASE_PROJECT_ID,
    storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
    messagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID
  };

  const firebaseApp = firebase.initializeApp(config);
  //firebaseApp.firestore().settings( { timestampsInSnapshots: true})

  //export firestore database
  export const db = firebaseApp.firestore()
  export const firebaseAuth = firebaseApp.auth()