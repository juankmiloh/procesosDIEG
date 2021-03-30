<template>
  <div class="app-container" style="text-align: center;">
    <upload-excel-component
      :on-success="handleSuccess"
      :before-upload="beforeUpload"
    />
    <div style="padding-top: 2%;">
      <el-button
        v-if="tableData.length"
        style="border: 1px solid #67c23a;"
        size="medium"
        icon="el-icon-upload"
        round
        @click="clickCargar();"
      >Cargar expedientes</el-button>
    </div>
    <el-table
      :data="tableData"
      border
      highlight-current-row
      style="width: 100%; margin-top: 20px"
    >
      <el-table-column
        v-for="item of tableHeader"
        :key="item"
        :prop="item"
        :label="item"
      />
    </el-table>
  </div>
</template>

<script>
import UploadExcelComponent from '@/components/UploadExcel/index.vue'
import { createProceso } from '@/api/procesosDIEG/procesos'
import moment from 'moment'
export default {
  name: 'UploadExcel',
  components: { UploadExcelComponent },
  data() {
    return {
      tableData: [],
      tableHeader: []
    }
  },
  methods: {
    beforeUpload(file) {
      const isLt1M = file.size / 1024 / 1024 < 1
      if (isLt1M) {
        return true
      }
      this.$message({
        message: 'Please do not upload files larger than 1m in size.',
        type: 'warning'
      })
      return false
    },
    handleSuccess({ results, header }) {
      this.tableData = results
      this.tableHeader = header
    },
    clickCargar() {
      // console.log(this.tableData)
      this.tableData.forEach(element => {
        // console.log(moment(this.numeroAFecha(element.fecha_caducidad, true)).format('DD/MM/YYYY'))
        if (!isNaN(element.fecha_caducidad)) { // Si es un numero
          element.fecha_caducidad = moment(this.numeroAFecha(element.fecha_caducidad, true)).format('DD/MM/YYYY')
        }
        createProceso(element).then((response) => {
          console.log('Expediente cargado con exito')
        })
      })
      this.$notify({
        title: 'Buen trabajo!',
        message: 'Expedientes cargados con éxito',
        type: 'success',
        duration: 2000
      })
      this.tableData = []
    },
    numeroAFecha(numeroDeDias, esExcel = false) {
      var diasDesde1900 = esExcel ? 25567 + 1 : 25567
      // 86400 es el número de segundos en un día, luego multiplicamos por 1000 para obtener milisegundos.
      return new Date((numeroDeDias - diasDesde1900) * 86400 * 1000)
    }
  }
}
</script>
