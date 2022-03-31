<template>
  <v-container class="">
      <v-row class="mt-10" justify="center" align="center">
        <v-col class="mt-5" cols="12">
            <h1>Dockerized Django, Postgres, Nuxt boilerplate!</h1>
        </v-col>
        <v-col class="mt-5" cols="12">
          <connectivity-test-card />
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
import ConnectivityTestCard from '@/components/ConnectivityTestCard';

export default {
  components: { ConnectivityTestCard },
};
</script>
