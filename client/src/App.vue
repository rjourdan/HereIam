<template>
  <div id="app">
    <HereMap
        appId=process.even.HERE_APP_ID
        appCode=process.even.HERE_APP_CODE
        width="100%"
        height="835px" />
  </div>
</template>

<script>
import HereMap from "@/components/HereMap.vue"

  export default {
    name: 'app',
    components: {
        HereMap
    }
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
