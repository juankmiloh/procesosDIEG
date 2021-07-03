<template>
  <div>

    <el-drawer
      ref="drawer"
      :before-close="handleClose"
      :visible.sync="drawervisible"
      direction="rtl"
      custom-class="demo-drawer"
      append-to-body
    >
      <div style="background: #f7fbff; height: 100%;">
        <sticky class-name="sub-navbar">
          <el-row>
            <el-col :span="24" style="text-align: center;">
              <label style="font-size: x-large; color: white;">{{ datosactos.nombre }}</label>
            </el-col>
          </el-row>
        </sticky>

        <!-- Card donde se listan las causales -->

        <div class="app-container">
          <el-row>
            <transition name="el-fade-in-linear">
              <el-col v-loading="loading" :span="24">
                <el-card class="box-card" style="overflow-y: scroll; height: 70vh;">
                  <el-card v-for="acto in datosactos['actos']" :key="acto.idetapa" style="width: 100%; margin-bottom: 3%;">
                    <div slot="header" class="clearfix">
                      <span style="color: #606266;"><b>Acto # {{ acto.numeroacto }}</b></span>
                      <div style="float: right;">
                        <el-button size="mini" type="danger" icon="el-icon-delete" :disabled="!editar" @click="handleDelete(acto)" />
                      </div>
                      <div style="float: right; padding-right: 2%;">
                        <el-button style="border: 1px solid #67C23A;" size="mini" type="success" icon="el-icon-edit" :disabled="!editar" @click="handleEdit(acto)"><b>Editar</b></el-button>
                      </div>
                    </div>
                    <div class="text item">
                      <span style="color: #606266;"><b>Radicado: </b>{{ acto.radicado }}</span>
                    </div>
                    <div class="text item">
                      <span v-if="acto.fechaInicio !== null" style="color: #606266;"><b>Fecha Inicio: </b><i class="el-icon-time" /> {{ acto.fechaInicio | formatDate }}</span>
                      <span v-else style="color: #606266;"><b>Fecha Fin: </b>No registra</span>
                    </div>
                    <div class="text item">
                      <span v-if="acto.fechaFin !== null" style="color: #606266;"><b>Fecha Fin: </b><i class="el-icon-time" /> {{ acto.fechaFin | formatDate }}</span>
                      <span v-else style="color: #606266;"><b>Fecha Fin: </b>No registra</span>
                    </div>
                    <div class="text item" style="width: 100%;">
                      <!-- <span style="color: #606266;"><b>Observación</b></span><br><br> -->
                      <el-input
                        v-model="acto.observacion"
                        type="textarea"
                        style="width: 100%;"
                        rows="4"
                        readonly
                      />
                    </div>
                  </el-card>
                </el-card>
              </el-col>
            </transition>
          </el-row>
          <el-row>
            <el-col :span="24" style="text-align: center; padding-top: 4%;">
              <el-button
                style="border: 1px solid #67c23a"
                type="primary"
                icon="el-icon-circle-plus"
                round
                :disabled="!editar"
                @click="handleAgregarActo()"
              >Agregar</el-button>
            </el-col>
          </el-row>
        </div>
      </div>
    </el-drawer>

    <!-- Modal de confirmacion para borrar una etapa -->

    <ModalDelete
      titulo="Advertencia"
      :mensaje="mensajeModalDelete"
      :modalvisible="deleteDialogVisible"
      @confirmar="submitDelete"
    />

  </div>
</template>

<script>
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import Sticky from '@/components/Sticky' // 粘性header组件
import ModalDelete from '@/components/ModalConfirm'
import { deleteActo } from '@/api/procesosDIEG/etapas'
// import moment from 'moment'

export default {
  directives: { elDragDialog },
  components: {
    Sticky,
    ModalDelete
  },
  props: {
    idproceso: {
      type: String,
      required: true
    },
    editar: {
      type: Boolean,
      required: true
    },
    drawervisible: {
      type: Boolean,
      required: false
    },
    datosactos: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      loading: false,
      mensajeModalDelete: '',
      deleteDialogVisible: false,
      delEtapa: '',
      delNumeroActo: '',
      x: ''
    }
  },
  async created() {
  },
  methods: {
    handleDelete(acto) {
      // console.log('Borrar acto --> ', acto)
      this.delEtapa = acto.etapa
      this.delNumeroActo = acto.numeroacto
      this.mensajeModalDelete = `¿Realmente desea eliminar el acto # <b>${acto.numeroacto}</b>?`
      this.deleteDialogVisible = true
    },
    async submitDelete(response) {
      // console.log(response)
      if (response) {
        const model = { idproceso: this.idproceso, etapa: this.delEtapa, numeroacto: this.delNumeroActo }
        await deleteActo(model).then(async(response) => {
          this.$notify({
            title: 'Información',
            message: 'Se ha eliminado el acto',
            type: 'success',
            duration: 2000
          })
        })
        this.$emit('confirmar', { response: false })
      }
      this.deleteDialogVisible = false
    },
    handleEdit(acto) {
      console.log(acto)
    },
    handleAgregarActo() {
      console.log('Agregar acto!')
    },
    handleClose() {
      this.$emit('confirmar', { response: false })
    }
  }
}
</script>

<style lang="scss" scoped>
  /* width */
  ::-webkit-scrollbar {
    width: 1.5px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    background: #f1f1f1;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #888;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #555;
  }

  // Pantallas superiores a 800px (PC)
  @media screen and (min-width: 800px) {
    .control-modal {
      width: 23em;
    }
  }

  // Pantallas inferiores a 800px (mobile)
  @media screen and (max-width: 800px) {
    .control-modal {
      width: 95%;
    }
  }
</style>

<style lang="scss">
// Pantallas superiores a 800px (PC)
@media screen and (min-width: 800px) {
  .dialog-class-lista {
    border-radius: 10px;
    // width: 10%;
  }

  .dialog-class-lista .el-dialog__body {
    padding-top: 0 !important;
  }

  .control-modal {
    width: 23em;
  }
}

// Pantallas inferiores a 800px (mobile)
@media screen and (max-width: 800px) {
  .dialog-class-lista {
    width: 100%;
  }

  .dialog-class-lista .el-dialog__body {
    padding: 0 !important;
  }

  .dialog-class-lista .el-dialog__header {
    display: none;
  }

  .control-modal {
    width: 95%;
  }
}
</style>

<style>
  /* Pantallas superiores a 800px (PC) */
  @media screen and (min-width: 800px) {
    .demo-drawer {
      width: 45% !important;
    }
  }

  /* Pantallas inferiores a 800px (mobile) */
  @media screen and (max-width: 800px) {
    .demo-drawer {
      width: 100% !important;
    }
  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 15px;
  }

  .badge-causal .item {
    border: 0px solid red;
    padding-right: 6%;
  }

  .div-causas .div-causas-header .el-card__header {
    padding-top: 4%;
    padding-left: 4%;
    height: 7vh;
  }

  .card-causas .el-card__body {
    border: 0px solid;
    padding-top: 4%;
  }

  .card-causa .el-card__body {
    border: 0px solid;
    padding-top: 2%;
  }
</style>
