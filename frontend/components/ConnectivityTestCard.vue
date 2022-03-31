<template>
  <v-card class="mt-5" style="width: 60%" outlined>
    <v-card-title class="headline">Connectivity test</v-card-title>
    <v-card-text>
      <v-btn color="primary" @click="getData" depressed tile>Fetch data</v-btn>
    </v-card-text>
    <v-card-text>
      <pre class="mt-2">{{ sample }}</pre>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'ConnectivityTestCard',
  data () {
    return {
      sample: null,
    }
  },
  methods: {
    async getData() {
      const { data } = await this.$axios.get('articles')
      this.sample = data;
    },
  },
};
</script>

<style lang="scss" scoped></style>
