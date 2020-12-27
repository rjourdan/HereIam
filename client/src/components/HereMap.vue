<template>
  
  <div class="here-map">
      <div class="alert" v-if="alert"> <p>Potential Fraud detected!</p> </div>
      <div ref="map_container" style="width: 100%; height: 768px; background: white;margin-top:0;"></div>
    </div>
</template>

<script>
import { db,auth } from '@/firebase/init'
export default {
  name: 'HereMap',
  data() {
    return {
        alert: false,
        payments: [],
        map : {
        'Init' : { // developer.here.com for app_id and app_code
          'app_id':   this.appId,
          'app_code': this.app_code,
          useHTTPS: true
        },
        'Behavior' :    {},         // Manage map behaviors
        'Container' :   {},         // Reference to DOM object containing map
        'Geo' :         {},         // Geocoder service
        'Lat' :         37.777429,   // Latitude
        'Layers' :      {},         // Map layers
        'Lng' :         -122.430399,       // Longitude
        'Map' :         {},         // Map object
        'Platform' :    {},         // Core to HERE API
        'UI' :          {},         // User interface and interaction
        'Zoom' :        10           // 1 == global, 15 == street level
      }
    }
  },
  props: {
    appId: String,
    appCode: String,
    width: String,
    height: String
  },
  methods:{
    displayMap() {
      this.map.Map.setCenter({lat:this.map.Lat, lng:this.map.Lng});
      this.map.Map.setZoom(this.map.Zoom);
      },
      addStaticMarker(lat,lng,name) {
        let paymentMarker = new H.map.Marker({lat:lat,lng:lng});
        paymentMarker.setData(name);
        this.map.Map.addObject(paymentMarker);
    }
  },
  created(){
    //initialize with HERE platform
    // Store initialized platform object
      this.map.Platform = new H.service.Platform(this.map.Init);
       // Store reference to geocoding service
      this.map.Geo = this.map.Platform.getGeocodingService();
      // Store reference to layers object
      this.map.Layers = this.map.Platform.createDefaultLayers();

    //fetch data from the firestore
 //   let ref = db.collection('payments').get()
 //   ref.then(snapshot => {
 //     snapshot.forEach(doc => {
 
//        let payment = doc.data()
//        payment.id = doc.id
//        this.payments.push(payment)
//        this.addStaticMarker(payment.latitude,payment.longitude,payment.name);
//      })
      let ref = db.collection('payments')
      ref.onSnapshot(snapshot => {
        snapshot.docChanges().forEach(change => {
          let doc = change.doc
          let payment = doc.data()
          payment.id = doc.id
          if(payment.alert=="alert") this.alert=true
          this.payments.push(payment)
          this.addStaticMarker(payment.latitude,payment.longitude,payment.name);
        
        });

    })
  },
  mounted() {
    this.map.Container = this.$refs.map_container
    this.map.Map = new H.Map(this.map.Container, this.map.Layers.normal.map);
      
      // Create behavior object initialized with map object
      this.map.Behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(this.map.Map));
      
      // Store UI object associated with map object and layers object
      this.map.UI = H.ui.UI.createDefault(this.map.Map, this.map.Layers);
      
      // Call function to display map using values stored in xy object
      this.displayMap();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.alert{
  width: 100%;
  height: 20px;
  background: white;
  font-weight: bold;
  color: red;
  padding-top: 0;
  margin-top:0;
}
</style>
