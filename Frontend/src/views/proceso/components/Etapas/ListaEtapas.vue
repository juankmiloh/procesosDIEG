<template>
  <div v-loading="loadingEtapa" class="main-article" style="background: #f7fbff; padding-left: 50px;">
    <el-row :gutter="30" class="header-agregar-etapa">
      <el-col v-for="etapa in etapas" :key="etapa.idtetapa" :sm="24" :md="8" style="border: 0px solid red; padding: 15px;">
        <el-card class="card-etapa" style="border: 0px solid #DCDFE6;">
          <div slot="header" class="clearfix" style="border: 0px solid red; padding: 0;">
            <div style="border-radius: 3px;padding-top: 2%;padding-right: 4%;height: 8vh;background: linear-gradient(38deg, rgba(255,255,255,1) 84%, rgba(33,133,208,1) 85%, rgba(33,133,208,1) 86%);">
              <el-row>
                <el-col :span="24" style="border: 0px solid red; text-align: right; color: white;">
                  <b>{{ etapa.idetapa }}</b>
                </el-col>
                <el-col :span="24" style="border: 0px solid red; text-align: center; color: #2184d0;">
                  <b>{{ etapa.nombre }}</b>
                </el-col>
              </el-row>
            </div>
          </div>
          <!-- Contenido de la card cuando la etapa NO tiene varios actos -->
          <el-row v-if="etapa.varios_actos === 'NO'" class="div-acto">
            <el-col :span="24" style="border: 0px solid; padding: 5% 10%;">
              <div class="text item" style="padding-top: 3%;">
                <el-row>
                  <el-col :span="6" :xs="7">
                    <span style="color: #606266;"><b>Radicado</b></span>
                  </el-col>
                  <el-col :span="18" :xs="17">
                    <span style="color: #606266;">{{ etapa['actos'][0].radicado }}</span>
                  </el-col>
                </el-row>
                <el-divider />
              </div>
              <div class="text item">
                <el-row>
                  <el-col :span="4" :xs="7">
                    <span style="color: #606266;"><b>Inicio</b></span>
                  </el-col>
                  <el-col :span="10" :xs="17">
                    <span v-if="etapa['actos'][0].fechaInicio !== 'No registra'" style="color: #606266;"><i class="el-icon-time" /> {{ etapa['actos'][0].fechaInicio | formatDate }}</span>
                    <span v-else style="color: #606266;"> {{ etapa['actos'][0].fechaInicio }}</span>
                  </el-col>

                  <el-col v-if="etapa.fecha_final === 'SI'" :span="3" :xs="7">
                    <span style="color: #606266;"><b>Final</b></span>
                  </el-col>
                  <el-col v-if="etapa.fecha_final === 'SI'" :span="7" :xs="17">
                    <span v-if="etapa['actos'][0].fechaFin !== 'No registra'" style="color: #606266;"><i class="el-icon-time" /> {{ etapa['actos'][0].fechaFin | formatDate }}</span>
                    <span v-else style="color: #606266;"> {{ etapa['actos'][0].fechaFin }}</span>
                  </el-col>
                </el-row>
              </div>
              <el-divider />
              <div v-if="etapa.observacion === 'SI'" class="text item">
                <span style="color: #606266;"><b>Observación</b></span><br><br>
                <el-input
                  v-model="etapa['actos'][0].observacion"
                  type="textarea"
                  class="control-modal"
                  rows="8"
                  readonly
                />
              </div>
            </el-col>
            <el-col :span="24" class="bottom">
              <el-button
                :disabled="!editar"
                style="border: 1px solid #67C23A"
                size="mini"
                type="success"
                plain
                icon="el-icon-edit"
                @click="handleEditarEtapa(etapa);"
              ><b>Editar</b></el-button>
              <el-button
                v-show="etapa.idetapa !== 1 || !editar"
                size="mini"
                type="danger"
                plain
                icon="el-icon-delete"
                @click="handleBorrarEtapa(etapa)"
              />
            </el-col>
          </el-row>
          <!-- Contenido de la card cuando la etapa tiene varios actos -->
          <el-row v-if="etapa.varios_actos === 'SI'" class="div-acto">
            <el-col :span="24" style="height: 100%;">
              <!-- {{ acto }} -->
              <el-card shadow="never" style="border: 0px solid #F2F6FC; height: 90%; overflow-y: scroll; padding: 5% 10%; 10%; 10%;">
                <div class="card-actuaciones">
                  <el-card v-for="acto in etapa['actos']" :key="acto.numeroacto" shadow="never" style="height: 5vh; margin-bottom: 4%;">
                    <span style="color: #606266; font-size: small;"><i class="el-icon-caret-right" /><b>Acto # {{ acto.numeroacto }}:</b> Radicado {{ acto.radicado }}</span>
                  </el-card>
                </div>
              </el-card>
            </el-col>
            <el-col :span="24" class="bottom">
              <el-button
                :disabled="!editar"
                style="border: 1px solid #67C23A"
                size="mini"
                type="success"
                plain
                icon="el-icon-zoom-in"
                @click="handleEditarEtapa(etapa);"
              ><b>Detalle</b></el-button>
              <el-button
                v-show="etapa.idetapa !== 1 || !editar"
                size="mini"
                type="danger"
                plain
                icon="el-icon-delete"
                @click="handleBorrarEtapa(etapa)"
              />
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>

    <!-- Cuadro de dialogo para editar o asignar etapa -->
    <AgregarEtapa />

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { CONSTANTS } from '@/constants/constants'
// import { getListEtapas } from '@/api/procesosDIEG/etapas'
import { getEtapaProceso } from '@/api/procesosDIEG/etapas'
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import moment from 'moment'
import AgregarEtapa from './AgregarEtapa'

export default {
  name: 'EtapasProceso',
  directives: { elDragDialog },
  components: { AgregarEtapa },
  props: {
    editar: {
      type: Boolean,
      default: false
    },
    id: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      loadingEtapa: false,
      formAgregar: CONSTANTS.formAgregarEtapa,
      etapas: [],
      textEditarEtapa: 'Agregar',
      msgAgregarEtapaVisible: false
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'idusuario', 'dependencia'])
  },
  created() {
    this.initView()
  },
  methods: {
    async initView() {
      this.getEtapasProceso(this.id) // Funcion para obtener las etapas del proceso
    },
    async getEtapasProceso(idproceso) {
      await getEtapaProceso(idproceso).then((response) => {
        console.log('ETAPA_PROCESO -> ', response)
        this.etapas = response
        // const modelResponse = response.map((data) => {
        //   data.fechaInicioEtapa = moment(data.fechaInicioEtapa).format('YYYY/MM/DD HH:mm:ss')
        //   if (data.fechaFinEtapa !== 'No registra') {
        //     data.fechaFinEtapa = moment(data.fechaFinEtapa).format('YYYY/MM/DD HH:mm:ss')
        //   }
        //   return data
        // })
        // this.etapas = modelResponse
        // console.log('NUEVO ETAPA_PROCESO -> ', this.etapas)
      })
    },
    handleEditarEtapa(etapa) {
      this.editarEtapa = true
      this.textEditarEtapa = 'Actualizar'
      this.formAgregar = CONSTANTS.formAgregarEtapa
      if (this.$refs['formAgregar']) {
        this.$refs['formAgregar'].resetFields()
      }
      this.msgAgregarEtapaVisible = true
      // console.log('clickAgregarEtapa -> ', this.$refs['formAgregar'])
      const modelEditarEtapa = {}
      try {
        modelEditarEtapa.idetapa = etapa.idetapa
        modelEditarEtapa.radicadoActual = etapa.radicadoEtapa
        modelEditarEtapa.radicadoEtapa = etapa.radicadoEtapa
        modelEditarEtapa.etapa = etapa.nombreEtapa
        modelEditarEtapa.observacionEtapa = etapa.observacionEtapa
        modelEditarEtapa.fechaInicioEtapa = moment(etapa.fechaInicioEtapa).format('YYYY/MM/DD HH:mm:ss')
        if (etapa.fechaFinEtapa !== 'No registra') {
          modelEditarEtapa.fechaFinEtapa = moment(etapa.fechaFinEtapa).format('YYYY/MM/DD HH:mm:ss')
        } else {
          modelEditarEtapa.fechaFinEtapa = null
        }
        this.formAgregar = modelEditarEtapa
        // console.log('handleEditarEtapa -> ', this.formAgregar)
      } catch (error) {
        // console.log(error)
      }
    },
    closeModalAgregar() {
      this.formAgregar = CONSTANTS.formAgregarEtapa
      if (this.$refs['formAgregar']) {
        this.$refs['formAgregar'].resetFields()
      }
      this.msgAgregarEtapaVisible = false
      this.loadingEtapa = false
      // console.log('closeModalAgregar -> ', this.$refs['formAgregar'])
    },
    handleBorrarEtapa(data) {
      this.delradEtapa = data.radicadoEtapa
      this.delIdetapa = data.idetapa
      this.delEtapa = data.nombreEtapa
      this.deleteDialogVisible = true
    }
  }
}
</script>

<style lang="scss" scoped>
  /* width */
  ::-webkit-scrollbar {
    width: 1px;
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

  .control-modal {
    width: 100%;
  }

  .bottom {
    position: absolute;
    bottom: 0%;
    border: 0px solid;
    text-align: center;
    padding: 2%;
    background: #F2F6FC;
  }

  // Pantallas superiores a 800px (PC)
  @media screen and (min-width: 800px) {
    .header-agregar-etapa {
      border: 0px solid;
      width: 100%;
      padding-left: 60px;
      padding-right: 60px;
      padding-bottom: 25px;
      overflow-y: scroll;
      height: 90vh;
    }

    .div-acto {
      height: 34em;
    }
  }

  // Pantallas inferiores a 800px (mobile)
  @media screen and (max-width: 800px) {
    .header-agregar-etapa {
      border: 0px solid;
      width: 100%;
      overflow-y: scroll;
      height: 90vh;
    }

    .div-acto {
      height: 32em;
    }
  }
</style>

<style lang="scss">
  .card-etapa .el-card__header {
    padding: 0;
  }

  .card-etapa .el-card__body {
    padding: 0;
  }

  .card-actuaciones .el-card__body {
    border: 0px solid;
    padding-top: 4%;
    padding-left: 3%;
  }
</style>
