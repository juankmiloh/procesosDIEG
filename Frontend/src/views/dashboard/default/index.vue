<template>
  <div class="dashboard-default-container">
    <el-row>
      <el-col :span="24" style="border: 0px solid red; text-align: center;">          
        <aside>
          <span style="color: black; font-size: 170%;"><b>DIRECCIÓN DE INVESTIGACIONES DE ENERGÍA Y GAS</b></span>
        </aside>
      </el-col>
      <el-col :span="24" style="border: 0px solid red; text-align: center;">          
        <aside type="success">
          <span style="font-size: 120%;"><b>{{ name }}</b></span>
        </aside>
      </el-col>
      <div style="padding-top: 17%;">
        <el-col :span="11" style="border: 0px solid red; text-align: right; margin-right: -2%;">
          <img :src="logo" class="imagePng">
        </el-col>
        <el-col :span="13" style="border: 0px solid red; padding-top: 7%;">
          <span style="font-size: 250%;"><b>Superservicios</b></span><br>
          <span style="font-size: 130%;">Superintendencia de Servicios</span><br>
          <span style="font-size: 130%;">Públicos Domiciliarios</span>
        </el-col>   
      </div>     
    </el-row>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  import PanThumb from '@/components/PanThumb'
  import GithubCorner from '@/components/GithubCorner'
  import logSuper from '@/assets/superservicios1.png'
  import RightPanel from '@/components/RightPanel';

  export default {
    name: 'DashboardDefault',
    components: { PanThumb, GithubCorner },
    data() {
      return {
        logo: logSuper
      }
    },
    computed: {
      ...mapGetters([
        'name',
        'avatar',
        'roles'
      ])
    }
  }
</script>

<style lang="scss" scoped>
  .dashboard-default-container {
    // background-color: #e3e3e3;
    // min-height: 100vh;
    padding: 20px 60px 0px;
  }

  .imagePng {
    width: 45%;
  }
</style>
