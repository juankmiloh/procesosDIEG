<template>
  <div class="dashboard-abogado-container">
    <div class=" clearfix">
      <pan-thumb :image="avatar" style="float: left">
        Usuario
        <span class="pan-info-roles">{{ name }}</span>
      </pan-thumb>
      <div class="info-container">
        <span class="display_name">{{ usuario }}</span>
        <span style="font-size:20px;padding-top:20px;display:inline-block;">{{ privilegio | uppercaseFirst }}</span>
      </div>
    </div>
    <div>
      <img :src="emptyGif" class="emptyGif">
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import PanThumb from '@/components/PanThumb'
import emptyGif from '@/assets/emptyGif.gif'

export default {
  name: 'DashboardAbogado',
  components: { PanThumb },
  data() {
    return {
      emptyGif: emptyGif
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'avatar',
      'roles',
      'usuario',
      'privilegio'
    ])
  }
}
</script>

<style lang="scss" scoped>
  .emptyGif {
    display: block;
    width: 45%;
    margin: 0 auto;
  }

  .dashboard-abogado-container {
    background-color: #e3e3e3;
    min-height: 89vh;
    padding: 50px 60px 0px;
    .pan-info-roles {
      font-size: 12px;
      font-weight: 700;
      color: #333;
      display: block;
    }
    .info-container {
      position: relative;
      margin-left: 190px;
      height: 150px;
      line-height: 200px;
      .display_name {
        font-size: 48px;
        line-height: 48px;
        color: #212121;
        position: absolute;
        top: 25px;
      }
    }
  }
</style>
