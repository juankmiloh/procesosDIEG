<template>
  <div class="createPost-container">

    <div class="dashboard-editor-container" style="border: 0px solid red; padding-bottom: 0;">
      <panel-group-proceso @handleSetPieChartData="handleSetPieChartData" />
    </div>

    <sticky class-name="sub-navbar">
      <div style="text-align: center; color: white;">
        <label style="font-size: x-large;">Procesos {{ selectPie }}</label>
      </div>
    </sticky>

    <div class="dashboard-editor-container">
      <el-row :gutter="32">
        <el-col :xs="24" :sm="24" :lg="12">
          <div v-loading="loadingEmpresas" class="chart-wrapper">
            <div style="text-align: center;"><label for="">Empresas</label></div>
            <pie-chart :chart-data="pieChartDataEmpresas" />
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="12">
          <div v-loading="loadingCausas" class="chart-wrapper">
            <div style="text-align: center;"><label for="">Causa</label></div>
            <pie-chart :chart-data="pieChartDataCausas" />
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="12">
          <div v-loading="loadingEmpresas" class="chart-wrapper">
            <div style="text-align: center;"><label for="">Estado</label></div>
            <pie-chart :chart-data="pieChartDataEstado" />
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="12">
          <div v-loading="loadingEmpresas" class="chart-wrapper">
            <div style="text-align: center;"><label for="">Abogado</label></div>
            <pie-chart :chart-data="pieChartDataEstado" />
          </div>
        </el-col>
      </el-row>
      <!-- <el-row :gutter="32">
        <el-col :xs="24" :sm="24" :lg="8">
          <div v-loading="loadingEmpresas" class="chart-wrapper">
            <div style="text-align: center;"><label for="">Empresas</label></div>
            <pie-chart :chart-data="pieChartDataEmpresas" />
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="8">
          <div v-loading="loadingCausas" class="chart-wrapper">
            <div style="text-align: center;"><label for="">Causa</label></div>
            <pie-chart :chart-data="pieChartDataCausas" />
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="8">
          <div v-loading="loadingEmpresas" class="chart-wrapper">
            <div style="text-align: center;"><label for="">Estado</label></div>
            <pie-chart :chart-data="pieChartDataEstado" />
          </div>
        </el-col>
      </el-row> -->
    </div>
  </div>
</template>

<script>
import PanelGroupProceso from './components/PanelGroupProceso'
import PieChart from './components/PieChart'
import { getListProcesosEmpresa } from '@/api/procesosDIEG/informes'
import { getListProcesosCausal } from '@/api/procesosDIEG/informes'
import { getListProcesosEstado } from '@/api/procesosDIEG/informes'
import Sticky from '@/components/Sticky' // 粘性header组件

export default {
  name: 'DashboardAdmin',
  components: {
    PieChart,
    PanelGroupProceso,
    Sticky
  },
  data() {
    return {
      loadingEmpresas: true,
      dataEmpresas: {},
      pieChartDataEmpresas: {},
      loadingCausas: true,
      dataCausas: {},
      pieChartDataCausas: {},
      loadingEstado: true,
      dataEstado: {},
      pieChartDataEstado: {},
      selectPie: 'activos'
    }
  },
  async created() {
    await this.initView()
  },
  methods: {
    initView() {
      this.getDataEmpresas()
      this.getDataCausas()
      this.getDataEstado()
    },
    handleSetPieChartData(type) {
      this.selectPie = type
      this.pieChartDataEmpresas = this.dataEmpresas[type]
      this.pieChartDataCausas = this.dataCausas[type]
      this.pieChartDataEstado = this.dataEstado[type]
    },
    async getDataEmpresas() {
      await getListProcesosEmpresa().then((response) => {
        this.dataEmpresas = response
        this.pieChartDataEmpresas = this.dataEmpresas['activos']
        this.loadingEmpresas = false
      })
    },
    async getDataCausas() {
      await getListProcesosCausal().then((response) => {
        // console.log(response)
        this.dataCausas = response
        this.pieChartDataCausas = this.dataCausas['activos']
        this.loadingCausas = false
      })
    },
    async getDataEstado() {
      await getListProcesosEstado().then((response) => {
        // console.log(response)
        this.dataEstado = response
        this.pieChartDataEstado = this.dataEstado['activos']
        this.loadingEstado = false
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;
  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }
  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}
@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
