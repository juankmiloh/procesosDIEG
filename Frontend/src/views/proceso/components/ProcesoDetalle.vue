<template>
  <div class="createPost-container" style="background: #f7fbff; height: 89vh;">
    <sticky class-name="sub-navbar">
      <div style="border: 0px solid red">
        <!-- Boton para abrir modal de etapas -->
        <transition name="el-zoom-in-center">
          <el-button
            v-show="showButtons"
            style="border: 2px solid #67c23a"
            size="medium"
            icon="el-icon-top-right"
            round
            @click="msgEtapasVisible = true; showModalEtapas();"
          >Ingresar a las etapas</el-button>
        </transition>
      </div>
    </sticky>

    <!-- Formulario donde se cargan los datos del proceso -->

    <div v-loading="loading" class="app-container">
      <el-row :gutter="10">
        <!-- Card datos proceso -->
        <el-form
          ref="formProceso"
          :rules="rulesFormProceso"
          :model="formProceso"
          label-width="120px"
          class="demo-ruleForm"
        >
          <el-col :md="8" style="border: 0px solid blue">
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>Proceso</span>
              </div>

              <el-form-item label="Expediente" prop="expediente">
                <el-input
                  v-model="formProceso.expediente"
                  autocomplete="off"
                  placeholder="Ingrese No. del expediente"
                  maxlength="17"
                  show-word-limit
                  clearable
                  class="control-modal"
                  :disabled="!editarProceso"
                />
              </el-form-item>

              <el-form-item label="Servicio" prop="servicio">
                <el-select
                  v-model="formProceso.servicio"
                  filterable
                  placeholder="Seleccione el servicio"
                  class="control-modal"
                  :disabled="!editarProceso"
                  @change="selectServicio($event)"
                >
                  <el-option
                    v-for="item in datosServicios"
                    :key="item.idservicio"
                    :label="item.servicio"
                    :value="item.idservicio"
                  />
                </el-select>
              </el-form-item>

              <el-form-item label="Empresa" prop="empresa">
                <el-select
                  v-model="formProceso.empresa"
                  filterable
                  placeholder="Seleccione un prestador"
                  class="control-modal"
                  :disabled="!editarProceso"
                >
                  <el-option
                    v-for="item in datosEmpresas"
                    :key="item.id_empresa"
                    :label="item.nombre"
                    :value="item.id_empresa"
                  />
                </el-select>
              </el-form-item>

              <el-form-item label="Proyectista" prop="usuario">
                <el-select
                  v-model="formProceso.usuario"
                  filterable
                  placeholder="Seleccione un usuario"
                  class="control-modal"
                  :disabled="!editarProceso"
                >
                  <el-option
                    v-for="item in datosUsuarios"
                    :key="item.idusuario"
                    :label="item.nombre + ' ' + item.apellido"
                    :value="item.idusuario"
                  />
                </el-select>
              </el-form-item>

              <el-form-item label="Revisor" prop="revisor">
                <el-select
                  v-model="formProceso.revisor"
                  filterable
                  placeholder="Seleccione un revisor"
                  class="control-modal"
                  :disabled="!editarProceso"
                >
                  <el-option
                    v-for="item in datosRevisor"
                    :key="item.idusuario"
                    :label="item.nombre + ' ' + item.apellido"
                    :value="item.idusuario"
                  />
                </el-select>
              </el-form-item>

              <el-form-item label="Tipo decisión" prop="tipo_sancion">
                <el-select
                  v-model="formProceso.tipo_sancion"
                  :disabled="!abogadoEditar"
                  filterable
                  placeholder="Seleccione sanción"
                  class="control-modal"
                >
                  <el-option
                    v-for="item in datosTiposancion"
                    :key="item.idtiposancion"
                    :label="item.nombre"
                    :value="item.idtiposancion"
                  />
                </el-select>
              </el-form-item>

              <el-form-item label="Sanción" prop="sancion">
                <el-input
                  v-model.number="formProceso.sancion"
                  :disabled="!abogadoEditar"
                  class="control-modal"
                  autocomplete="off"
                />
              </el-form-item>

              <el-form-item label="Decisión final" prop="decision">
                <el-select
                  v-model="formProceso.decision"
                  :disabled="!abogadoEditar"
                  filterable
                  placeholder="Seleccione decisión"
                  class="control-modal"
                >
                  <el-option
                    v-for="item in datosDecision"
                    :key="item.iddecision"
                    :label="item.nombre"
                    :value="item.iddecision"
                  />
                </el-select>
              </el-form-item>
            </el-card>
          </el-col>

          <!-- Form datos causal -->

          <el-col :md="9" style="border: 0px solid blue">
            <el-row :gutter="10">
              <el-col :md="24">
                <!-- Tabla de causales -->
                <tabla-causas v-if="id" :idproceso="id" :editar="abogadoEditar" />
              </el-col>
              <el-col :md="24">
                <!-- Card terceros interesados -->
                <switch-terceros v-if="id" :idproceso="id" :editar="abogadoEditar" />
              </el-col>
            </el-row>
          </el-col>

          <!-- Datos caducidad / etapas -->

          <el-col :md="7" style="border: 0px solid blue">
            <el-row :gutter="10">
              <!-- Card datos caducidad -->
              <el-col :md="24" class="input-caducidad" style="border: 0px solid blue">
                <el-card class="box-card">
                  <div slot="header" class="clearfix">
                    <span>Caducidad</span>
                  </div>
                  <el-form-item label="" prop="caducidad">
                    <el-date-picker
                      v-model="formProceso.caducidad"
                      :disabled="!abogadoEditar"
                      type="date"
                      placeholder="Seleccione una fecha"
                      class="control-modal"
                    />
                  </el-form-item>
                </el-card>
              </el-col>

              <!-- card carpetas reservadas -->
              <!-- <el-col :md="24" style="border: 0px solid blue; padding-top: 0px;" class="div-causas">
                <el-card class="box-card div-causas-header" style="height: 8vh;">
                  <div slot="header" class="clearfix">
                    <el-row>
                      <el-col>
                        <span>Carpetas reservadas</span>
                      </el-col>
                    </el-row>
                  </div>
                </el-card>
              </el-col> -->

              <!-- Card datos etapa -->

              <el-col
                :md="24"
                class="input-etapas"
                style="border: 0px solid blue; padding-top: 10px"
              >
                <el-card class="box-card" style="padding: 0; margin: 0;">
                  <div slot="header" class="clearfix">
                    <span>Estado</span>
                  </div>
                  <el-row>
                    <el-col :span="24" style="border: 0px solid red;">
                      <el-form-item label="">
                        <el-row>
                          <el-col :span="24">
                            <label style="color: #606266">Actual</label>
                          </el-col>
                          <el-col :span="24">
                            <el-select
                              v-model="formProceso.estado"
                              placeholder="Seleccione un estado"
                              class="control-modal"
                            >
                              <el-option
                                v-for="item in datosEstado"
                                :key="item.idestado"
                                :label="item.nombre"
                                :value="item.idestado"
                                disabled
                              />
                            </el-select>
                          </el-col>
                        </el-row>
                      </el-form-item>
                    </el-col>
                    <el-col :span="24" style="border: 0px solid;">
                      <el-form-item label="" prop="prox_etapa">
                        <el-row>
                          <el-col :span="24">
                            <label style="color: #606266">Siguiente</label>
                          </el-col>
                          <el-col :span="24">
                            <el-input
                              v-model="formProceso.proxetapa"
                              autocomplete="off"
                              placeholder="Siguiente etapa"
                              readonly
                            />
                          </el-col>
                        </el-row>
                      </el-form-item>
                    </el-col>
                  </el-row>
                </el-card>
              </el-col>

              <!-- Boton  / editarProceso / actualizar -->

              <el-col :md="24" style="border: 0px solid blue">
                <el-card
                  class="box-card"
                  shadow="never"
                  style="background: none; border: 0; text-align: center"
                >
                  <el-button
                    v-show="showOnlyAdmin"
                    style="border: 0px solid #67c23a; width: 9em"
                    :type="editarProceso ? 'danger' : 'primary'"
                    :icon="editarProceso ? 'el-icon-error' : 'el-icon-edit'"
                    @click="editarProceso = !editarProceso; editarForm();"
                  >{{ textEditarProceso }}</el-button>
                  <el-button
                    :disabled="!abogadoEditar"
                    style="width: 9em"
                    :type="editarProceso ? 'primary' : 'success'"
                    :icon="editarProceso ? 'el-icon-circle-check' : 'el-icon-check'"
                    @click="submitForm('formProceso')"
                  >{{ textActualizar }}</el-button>
                </el-card>
              </el-col>
            </el-row>
          </el-col>
        </el-form>
      </el-row>
    </div>

    <!-- Cuadro de dialogo de etapas -->

    <el-dialog
      ref="modalEtapas"
      :visible.sync="msgEtapasVisible"
      :show-close="false"
      fullscreen
      custom-class="dialog-class-ldetalle dialog-color"
      :destroy-on-close="true"
    >
      <Etapas :idproceso="id" :expediente="formProceso.expediente" :editar="abogadoEditar" @close-modal-etapas="closeModalEtapa" />
    </el-dialog>

  </div>
</template>

<script>
import Sticky from '@/components/Sticky' // 粘性header组件
import { mapGetters } from 'vuex'
import { getProceso } from '@/api/procesosDIEG/procesos'
import { getAllEmpresas } from '@/api/procesosDIEG/empresas'
import { getListUsuarios, getListRevisores } from '@/api/procesosDIEG/usuarios'
import { getListServicios } from '@/api/procesosDIEG/servicios'
import { getListEstado } from '@/api/procesosDIEG/estado'
import { getListTiposancion } from '@/api/procesosDIEG/tiposancion'
import { getListDecision } from '@/api/procesosDIEG/decision'
import { updateProceso } from '@/api/procesosDIEG/procesos'
import { getListEmpresas } from '@/api/procesosDIEG/empresas'
import { getListEtapas } from '@/api/procesosDIEG/etapas'
import { CONSTANTS } from '@/constants/constants'
import SwitchTerceros from './SwitchTerceros'
import TablaCausas from './TablaCausas'
import Etapas from './Etapas'

export default {
  name: 'ProcesoDetalle',
  components: { Sticky, SwitchTerceros, TablaCausas, Etapas },
  props: {
    isDetail: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      id: '',
      datosUsuarios: [],
      datosRevisor: [],
      datosServicios: [],
      datosEmpresas: [],
      empresas: [],
      datosEstado: [],
      datosTiposancion: [],
      datosDecision: [],
      formProceso: CONSTANTS.formDetalleProceso,
      /* Si es o no visible el cuadro de dialogo de las etapas */
      msgEtapasVisible: false,
      /* Si es o no para editar */
      editarProceso: false,
      textEditarProceso: 'Editar',
      textActualizar: 'Actualizar',
      loading: false,
      tempRoute: {},
      prox_etapa: '',
      datosEtapaProceso: [],
      formAgregar: CONSTANTS.formAgregarEtapa,
      rulesFormProceso: CONSTANTS.rulesDetalleProceso,
      rulesFormEtapa: CONSTANTS.rulesFormEtapa,
      datosEtapa: [],
      showButtons: false,
      showOnlyAdmin: false,
      abogadoEditar: false
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'idusuario', 'dependencia'])
  },
  created() {
    if (this.isDetail) {
      this.loading = true
      // console.log('PARAMETROS URL -> ', this.$route.params)
      this.id = this.$route.params.id
      this.initView()
    }

    // Why need to make a copy of this.$route here?
    // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
    // https://github.com/PanJiaChen/vue-element-admin/issues/1221
    this.tempRoute = Object.assign({}, this.$route)
  },
  methods: {
    async initView() {
      if (this.roles[0] === 'administrador') {
        this.showOnlyAdmin = true
        this.abogadoEditar = true
      }
      this.getEmpresas()
      this.getUsuarios()
      this.getRevisores()
      this.getServicios()
      this.getEstado()
      this.getTiposancion()
      this.getDecision()
      await this.getEtapas()
      await this.fetchData(this.id)
    },
    async getEmpresas() {
      await getAllEmpresas().then((response) => {
        this.empresas = response.items
      })
    },
    async getUsuarios() {
      await getListUsuarios(this.dependencia).then((response) => {
        // console.log('Usuarios -> ', response)
        this.datosUsuarios = response
      })
    },
    async getRevisores() {
      await getListRevisores(this.dependencia).then((response) => {
        // console.log('Revisores -> ', response)
        this.datosRevisor = response
      })
    },
    async getServicios() {
      await getListServicios(this.dependencia).then((response) => {
        this.datosServicios = response
      })
    },
    async getEstado() {
      await getListEstado().then((response) => {
        this.datosEstado = response
      })
    },
    async getTiposancion() {
      await getListTiposancion().then((response) => {
        this.datosTiposancion = response
      })
    },
    async getDecision() {
      await getListDecision().then((response) => {
        this.datosDecision = response
      })
    },
    async getEtapas() {
      await getListEtapas().then((response) => {
        this.datosEtapa = response
        for (const iterator of this.datosEtapaProceso) {
          this.datosEtapa.filter((etapa) => {
            if (etapa.nombre === iterator.nombreEtapa) { // Verifica si la etapa ya esta en el proceso y se elimina del arreglo de etapas que se muestra en el select de etapas
              const posEtapa = this.datosEtapa.indexOf(etapa)
              this.datosEtapa.splice(posEtapa, 1)
            }
          })
        }
      })
    },
    async fetchData(id) {
      let modelProceso = {}
      await getProceso(id).then(async(response) => {
        // console.log('RESPONSE PROCESO -> ', response)
        if (response.length > 0) { // Se obtienen los datos del proceso si ya esta diligenciado en su totalidad
          console.log('RESPONSE proceso completo -> ', response)
          modelProceso = response[0]
          if (!modelProceso.decision) { // Sino se cargan los datos del proceso completos (Esto pasa cuando se crea un proceso nuevo)
            modelProceso.tipo_sancion = 9 // Se agrega el atributo al modelo del proceso
            modelProceso.decision = 6 // Se agrega el atributo al modelo del proceso un valor por defecto
            modelProceso.sancion = 0 // Se agrega el atributo al modelo del proceso
          }
          this.getEmpresasProceso(modelProceso)
        }
        // Condicional para permitir la edicion del proceso por el abogado
        if (this.roles[0] === 'proyectista' && modelProceso.usuario === this.idusuario) {
          this.abogadoEditar = true
        } else if (this.roles[0] === 'revisor' && modelProceso.revisor === this.idusuario) {
          this.abogadoEditar = true
        }
        if (modelProceso.proxetapa === null) {
          this.prox_etapa = 'No aplica'
        }
        this.loading = false
        this.showButtons = true
        this.formProceso = modelProceso
        // console.log('Model proceso -> ', this.formProceso)
        // set tagsview title
        this.setTagsViewTitle()
        // set page title
        this.setPageTitle()
        if (this.$refs['formProceso']) {
          this.$refs['formProceso'].resetFields()
        }
        // console.log('fetchData 3 -> ', this.$refs['formProceso'])
      }).catch((err) => {
        return err
      })
    },
    getEmpresasProceso(modelProceso) {
      this.datosEmpresas = this.empresas.filter((empresa) => empresa.idservicio === modelProceso.servicio) // Se obtienen las empresas asociadas al servicio publico del proceso
      // console.log('getEmpresasProceso -> ', this.datosEmpresas)
    },
    setTagsViewTitle() {
      const title = 'Expediente'
      const route = Object.assign({}, this.tempRoute, {
        title: `${title} ${this.formProceso.expediente}`
      })
      this.$store.dispatch('tagsView/updateVisitedView', route)
    },
    setPageTitle() {
      const title = 'Expediente'
      document.title = `${title} - ${this.formProceso.expediente}`
    },
    showModalEtapas() {
      this.showButtons = false
    },
    async closeModalEtapa() {
      await this.fetchData(this.id)
      this.msgEtapasVisible = false
      this.showButtons = true
    },
    async selectServicio(idservicio) {
      if (this.editarProceso) {
        this.formProceso.empresa = ''
      }
      if (idservicio) {
        await getListEmpresas(idservicio).then((response) => {
          this.datosEmpresas = response.items
        })
      }
    },
    editarForm() {
      if (this.editarProceso) { // Si se activa el boton editar proceso
        this.$notify({
          title: 'Advertencia',
          message: 'Has activado el modo edición!',
          type: 'warning',
          duration: 2000
        })
        this.textEditarProceso = 'Cancelar'
        this.textActualizar = 'Guardar'
        window.localStorage.setItem('form_save', JSON.stringify(this.formProceso)) // Se envia una copia del proceso al localstorage
      } else { // Cuando Se desactiva el boton editar proceso (Se restablece el proceso a como estaba antes de darle editar)
        this.$notify({
          title: 'info',
          message: 'Has desactivado el modo edición!',
          type: 'info',
          duration: 2000
        })
        this.textEditarProceso = 'Editar'
        this.textActualizar = 'Actualizar'
        this.formProceso = JSON.parse(window.localStorage.getItem('form_save')) // Se carga la copia del proceso guardado en localstorage
        this.selectServicio(this.formProceso.servicio) // Se carga de nuevo la lista de las empresas del servicio guardado en localstorage
        window.localStorage.removeItem('form_save')
      }
    },
    submitForm() {
      let modelProceso = this.formProceso
      console.log('THISFORMPROCESO -> ', modelProceso)
      this.$refs.formProceso.validate(async(valid) => {
        if (valid) {
          this.loading = true
          this.showButtons = false
          await updateProceso(modelProceso).then(async(response) => {
            if (this.editarProceso) {
              this.$notify({
                title: 'info',
                message: 'Se ha desactivado el modo edición!',
                type: 'info',
                duration: 2000
              })
            }
            await getProceso(this.id).then(async(response) => { // Se actualizan los datos del proceso
              // console.log('ACTUALIZAR PROCESO -> ', response)
              modelProceso = response[0]
              this.textEditarProceso = 'Editar'
              this.textActualizar = 'Actualizar'
              this.$notify({
                title: 'Bien hecho!',
                message: 'Expediente actualizado con éxito',
                position: this.editarProceso ? 'top-right' : 'bottom-right',
                type: 'success',
                duration: 2000
              })
              this.editarProceso = false
              this.loading = false
              this.showButtons = true
            })
          })
        } else {
          // console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  .control-modal {
    width: 100%;
  }
</style>

<style lang="scss">
  .dialog-class-ldetalle .el-dialog__header {
    border-radius: 10px;
    display: none;
  }

  .dialog-class-ldetalle .el-dialog__body {
    margin: 0 !important;
    padding: 0 !important;
    height: 100%;
    overflow: hidden;
  }

  .dialog-color {
    background: #f7fbff;
  }

  .input-caducidad .el-form-item .el-form-item__content {
    margin-left: 0% !important;
  }

  .input-etapas .el-form-item .el-form-item__content {
    margin-left: 0% !important;
  }

  .div-causas .div-causas-header .el-card__header {
    padding-top: 4%;
    padding-left: 4%;
    height: 7vh;
  }
</style>
