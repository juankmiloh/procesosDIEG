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

              <el-form-item label="Estado">
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
                    <span>Etapas</span>
                  </div>
                  <el-row>
                    <el-col :span="24" style="border: 0px solid red;">
                      <el-form-item label="" prop="etapa">
                        <el-row>
                          <el-col :span="24">
                            <label style="color: #606266">Actual</label>
                          </el-col>
                          <el-col :span="24">
                            <el-input
                              v-model="formProceso.etapa"
                              autocomplete="off"
                              placeholder="Etapa actual"
                              readonly
                            />
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
                              v-model="prox_etapa"
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
    >
      <div style="padding-bottom: 10px">
        <sticky
          :z-index="10"
          class-name="sub-navbar"
          style="position: fixed width: 99%;"
        >
          <div style="border: 0px solid red">

            <div style="text-align: center; color: white">
              <el-row>
                <el-col :span="19" style="padding-left: 15%;">
                  <label style="font-size: x-large">Etapas expediente {{ formProceso.expediente }}</label>
                </el-col>
                <el-col :span="5">
                  <!-- Boton para agregar nueva etapa al aplicativo -->
                  <transition name="el-zoom-in-center">
                    <div v-show="showButtonsModal">
                      <el-button
                        :disabled="!abogadoEditar"
                        style="border: 2px solid #67c23a"
                        size="medium"
                        icon="el-icon-circle-plus"
                        @click="clickAgregarEtapa();"
                      >Agregar etapa</el-button>
                      <el-button
                        style="border: 1px solid #67c23a"
                        type="warning"
                        size="medium"
                        @click="closeModalEtapa();"
                      >Cerrar</el-button>
                    </div>
                  </transition>
                </el-col>
              </el-row>
            </div>
          </div>
        </sticky>
      </div>
      <div v-loading="loadingEtapa" class="app-container" style="background: #f7fbff; padding-top: 0;">
        <el-row :gutter="30" style="border: 0px solid; padding-left: 6%; padding-right: 6%; overflow-y: scroll; height: 89vh;">
          <el-col v-for="item in datosEtapaProceso" :key="item.idtercero" :span="6" style="border: 0px solid red; padding-top: 1%; padding-bottom: 1.5%;">
            <el-card class="card-etapa" style="border: 1px solid #DCDFE6;">
              <div slot="header" class="clearfix" style="border: 0px solid red; padding: 0;">
                <div style="border-radius: 3px;padding-top: 2%;padding-right: 4%;height: 8vh;background: linear-gradient(38deg, rgba(255,255,255,1) 84%, rgba(33,133,208,1) 85%, rgba(33,133,208,1) 86%);">
                  <el-row>
                    <el-col :span="24" style="border: 0px solid red; text-align: right; color: white;">
                      <b>{{ item.idetapa }}</b>
                    </el-col>
                    <el-col :span="24" style="border: 0px solid red; padding-left: 8%; color: #2184d0;">
                      <b>{{ item.nombreEtapa }}</b>
                    </el-col>
                  </el-row>
                </div>
              </div>
              <el-row>
                <el-col :span="24" style="border: 0px solid; padding: 5% 10%;">
                  <div class="text item" style="text-align: center; padding-top: 3%;">
                    <span style="color: #303133;"><b>{{ item.radicadoEtapa }}</b></span>
                    <el-divider />
                  </div>
                  <div class="text item">
                    <el-row>
                      <el-col :span="7">
                        <span style="color: #303133;"><b>Inicio</b></span>
                      </el-col>
                      <el-col :span="17">
                        <span style="color: #606266;"><i class="el-icon-time" /> {{ item.fechaInicioEtapa }}</span>
                      </el-col>
                    </el-row>
                  </div>
                  <div class="text item">
                    <el-row>
                      <el-col :span="7">
                        <span style="color: #303133;"><b>Final</b></span>
                      </el-col>
                      <el-col :span="17">
                        <span style="color: #606266;"><i v-if="item.fechaFinEtapa !== 'No registra'" class="el-icon-time" /> {{ item.fechaFinEtapa }}</span>
                      </el-col>
                    </el-row>
                  </div>
                  <el-divider />
                  <div class="text item">
                    <span style="color: #303133;"><b>Observación</b></span><br><br>
                    <el-input
                      v-model="item.observacionEtapa"
                      type="textarea"
                      class="control-modal"
                      rows="4"
                      readonly
                    />
                  </div>
                </el-col>
                <el-col :span="24" style="border: 0px solid; text-align: center; padding: 2%; background: #F2F6FC;">
                  <el-button
                    :disabled="!abogadoEditar"
                    style="border: 1px solid #67C23A"
                    size="mini"
                    type="success"
                    plain
                    icon="el-icon-edit"
                    @click="handleEditarEtapa(item);"
                  ><b>Editar</b></el-button>
                  <el-button
                    :disabled="item.nombreEtapa === 'Memorando IG' || !abogadoEditar"
                    size="mini"
                    type="danger"
                    plain
                    icon="el-icon-delete"
                    @click="handleBorrarEtapa(item)"
                  />
                </el-col>
              </el-row>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </el-dialog>

    <!-- Cuadro de dialogo para editar o asignar etapa -->

    <el-dialog
      v-el-drag-dialog
      :visible.sync="msgAgregarEtapaVisible"
      :before-close="closeModalAgregar"
      width="31em"
      custom-class="dialog-class-ldetalle"
      :destroy-on-close="true"
    >
      <sticky class-name="sub-navbar">
        <div style="border: 0px solid red; color: white; text-align: center;">
          <h2 v-if="editarEtapa">Editar etapa</h2>
          <h2 v-else>Agregar etapa</h2>
        </div>
      </sticky>

      <div class="createPost-container" style="padding-top: 25px; padding-bottom: 20px;">
        <el-form
          ref="formAgregar"
          :model="formAgregar"
          :rules="rulesFormEtapa"
          label-width="120px"
          class="demo-ruleForm"
        >
          <el-form-item label="Etapa" prop="etapa">
            <el-select
              v-model="formAgregar.etapa"
              filterable
              placeholder="Seleccione una etapa"
              class="control-modal-agregar"
              :disabled="editarEtapa"
              @change="selectEtapa($event)"
            >
              <el-option
                v-for="item in datosEtapa"
                :key="item.idetapa"
                :label="item.nombre"
                :value="item.idetapa"
              />
            </el-select>
          </el-form-item>

          <el-form-item label="Radicado" prop="radicadoEtapa">
            <el-input
              v-model="formAgregar.radicadoEtapa"
              autocomplete="off"
              placeholder="Ingrese No. del radicado"
              maxlength="14"
              show-word-limit
              clearable
              class="control-modal-agregar"
            />
          </el-form-item>

          <el-form-item label="Fecha inicio" prop="fechaInicioEtapa">
            <el-date-picker
              v-model="formAgregar.fechaInicioEtapa"
              type="datetime"
              placeholder="Seleccione fecha inicio"
              class="control-modal-agregar"
            />
          </el-form-item>

          <el-form-item label="Fecha fin" prop="fechaFinEtapa">
            <el-date-picker
              v-model="formAgregar.fechaFinEtapa"
              type="datetime"
              placeholder="Seleccione fecha fin"
              class="control-modal-agregar"
            />
          </el-form-item>

          <el-form-item label="Observación" prop="observacionEtapa">
            <el-input
              v-model="formAgregar.observacionEtapa"
              type="textarea"
              class="control-modal-agregar"
              rows="7"
            />
          </el-form-item>

          <el-form-item>
            <el-button
              @click="closeModalAgregar();"
            >Cancelar</el-button>
            <el-button
              type="success"
              @click="handleEtapa();"
            >{{ textEditarEtapa }}</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-dialog>

    <!-- Dialogo que aparece cuando se va a eliminar una etapa -->

    <el-dialog
      v-el-drag-dialog
      title="Advertencia"
      :visible.sync="deleteDialogVisible"
      width="40%"
      center
      custom-class="dialog-class-lista"
    >
      <br>
      <center>
        <span>¿Realmente desea eliminar la etapa <b>{{ delEtapa }}</b>?</span>
      </center>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deleteDialogVisible = false">Cancelar</el-button>
        <el-button
          type="primary"
          @click="borrarEtapa"
        >Confirmar</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getProceso, getProcesoInicial } from '@/api/procesosDIEG/procesos'
import { getAllEmpresas } from '@/api/procesosDIEG/empresas'
import { getListUsuarios, getListRevisores } from '@/api/procesosDIEG/usuarios'
import { getListServicios } from '@/api/procesosDIEG/servicios'
import { getListEstado } from '@/api/procesosDIEG/estado'
import { getListTiposancion } from '@/api/procesosDIEG/tiposancion'
import { getListDecision } from '@/api/procesosDIEG/decision'
import { updateProceso } from '@/api/procesosDIEG/procesos'
import { getListEmpresas } from '@/api/procesosDIEG/empresas'
import { getListEtapas } from '@/api/procesosDIEG/etapas'
import { getEtapaProceso } from '@/api/procesosDIEG/etapas'
import { createEtapa } from '@/api/procesosDIEG/etapas'
import { deleteEtapa } from '@/api/procesosDIEG/etapas'
import { updateEtapa } from '@/api/procesosDIEG/etapas'
import Sticky from '@/components/Sticky' // 粘性header组件
import { CONSTANTS } from '@/constants/constants'
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import moment from 'moment'
import SwitchTerceros from './SwitchTerceros'
import TablaCausas from './TablaCausas'

export default {
  name: 'ProcesoDetalle',
  directives: { elDragDialog },
  components: { Sticky, SwitchTerceros, TablaCausas },
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
      /* Si es o no visible el cuadro de dialogo de agregar o editar etapa */
      msgAgregarEtapaVisible: false,
      /* Si es o no visible el cuadro de dialogo de las etapas */
      msgEtapasVisible: false,
      /* Si es o no para editar */
      editarProceso: false,
      textEditarProceso: 'Editar',
      textActualizar: 'Actualizar',
      loading: false,
      userListOptions: [],
      tempRoute: {},
      prox_etapa: '',
      datosEtapaProceso: [],
      tableColumns: CONSTANTS.tableColumnsEtapas,
      busquedaEtapa: '',
      formAgregar: CONSTANTS.formAgregarEtapa,
      rulesFormProceso: CONSTANTS.rulesDetalleProceso,
      rulesFormEtapa: CONSTANTS.rulesFormEtapa,
      datosEtapa: [],
      /* Si es o no visible el cuadro de confirmación de eliminación */
      deleteDialogVisible: false,
      delradEtapa: '',
      delIdetapa: '',
      delEtapa: '',
      estampillaEtapa: '',
      editarEtapa: false,
      textEditarEtapa: 'Agregar',
      showButtons: false,
      showButtonsModal: false,
      showOnlyAdmin: false,
      abogadoEditar: false,
      loadingEtapa: false
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
      this.getEtapasProceso(this.id) // Funcion para obtener las etapas del proceso
      this.initView()
    }

    // Why need to make a copy of this.$route here?
    // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
    // https://github.com/PanJiaChen/vue-element-admin/issues/1221
    this.tempRoute = Object.assign({}, this.$route)
  },
  methods: {
    async getEtapasProceso(idproceso) {
      await getEtapaProceso(idproceso).then((response) => {
        // console.log('ETAPA_PROCESO -> ', response)
        const modelResponse = response.map((data) => {
          data.fechaInicioEtapa = moment(data.fechaInicioEtapa).format('YYYY/MM/DD HH:mm:ss')
          if (data.fechaFinEtapa !== 'No registra') {
            data.fechaFinEtapa = moment(data.fechaFinEtapa).format('YYYY/MM/DD HH:mm:ss')
          }
          return data
        })
        this.datosEtapaProceso = modelResponse
        // console.log('NUEVO ETAPA_PROCESO -> ', this.datosEtapaProceso)
      })
    },
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
      // this.datosUsuarios = JSON.parse(this.$route.params.usuarios) // Se capturan los parametros de la URL
      // this.datosServicios = JSON.parse(this.$route.params.servicios) // Se capturan los parametros de la URL
      let modelProceso = {}
      await getProceso(id).then(async(response) => {
        // console.log('RESPONSE PROCESO -> ', response)
        if (response.length > 0) { // Se obtienen los datos del proceso si ya esta diligenciado en su totalidad
          console.log('RESPONSE proceso completo -> ', response)
          modelProceso = response[0]
          this.getEmpresasProceso(modelProceso)
          // modelProceso = await this.verificarDataModel(modelProceso, true)
        } else { // Sino se cargan los datos del proceso completos (Esto pasa cuando se crea un proceso nuevo)
          await getProcesoInicial(id).then(async(response) => {
            console.log('RESPONSE inicial -> ', response)
            modelProceso = response[0]
            modelProceso.tipo_sancion = 9 // Se agrega el atributo al modelo del proceso
            modelProceso.decision = 6 // Se agrega el atributo al modelo del proceso un valor por defecto
            modelProceso.sancion = 0 // Se agrega el atributo al modelo del proceso
            modelProceso.descripcion = '' // Se agrega el atributo al modelo del proceso
            this.getEmpresasProceso(modelProceso)
            // modelProceso = await this.verificarDataModel(modelProceso, false)
          })
        }
        // Condicional para permitir la edicion del proceso por el abogado
        if (this.roles[0] === 'proyectista' && modelProceso.usuario === this.idusuario) {
          this.abogadoEditar = true
        } else if (this.roles[0] === 'revisor' && modelProceso.revisor === this.idusuario) {
          this.abogadoEditar = true
        }
        if (modelProceso.etapa !== 'Memorando IG') {
          this.prox_etapa = modelProceso.proxetapa
        } else {
          this.prox_etapa = 'Por definir'
        }
        const countEtapas = this.datosEtapaProceso.length
        // console.log('countetapas -> ', countEtapas)
        if (countEtapas === 15 || modelProceso.proxetapa === null) {
          this.prox_etapa = 'No aplica'
        } else {
          console.log('Revisar proxima etapa')
          // console.log('etapas no finalizadas -> ', this.datosEtapaProceso[1]) // Revisar
          // const etapaActual = this.datosEtapaProceso[1]
          // console.log('this.datosEtapa -> ', this.datosEtapa)
          // const idxEtapaActual = this.datosEtapa.indexOf(etapaActual)
          // console.log('idxEtapaActual -> ', idxEtapaActual)
          // const etapaSiguiente = this.datosEtapa[idxEtapaActual + 1]
          // console.log('etapaSiguiente-> ', etapaSiguiente)
          // this.prox_etapa = etapaSiguiente.nombre
        }
        this.loading = false
        this.showButtons = true
        this.formProceso = modelProceso
        console.log('Model proceso -> ', this.formProceso)
        // set tagsview title
        this.setTagsViewTitle()
        // set page title
        this.setPageTitle()
        if (this.$refs['formProceso']) {
          this.$refs['formProceso'].resetFields()
        }
        // console.log('fetchData 3 -> ', this.$refs['formProceso'])
      }).catch((err) => {
        // console.log(err)
        return err
      })
    },
    async verificarDataModel(modelProceso, infoCompleta) {
      console.log('infoCompleta -> ', infoCompleta)
      if (infoCompleta) { // Si el proceso TRAE toda la informacion
        modelProceso.estado = await this.datosEstado.find((estado) => estado.nombre === modelProceso.estado).idestado
        modelProceso.empresa = await this.datosEmpresas.find((empresa) => empresa.nombre === modelProceso.empresa.toUpperCase()).id_empresa
        modelProceso.servicio = await this.datosServicios.find((servicio) => servicio.servicio === modelProceso.servicio).idservicio
        modelProceso.decision = await this.datosDecision.find((decision) => decision.nombre === modelProceso.decision).iddecision
        modelProceso.tipo_sancion = await this.datosTiposancion.find((tiposancion) => tiposancion.nombre === modelProceso.tipo_sancion).idtiposancion
      } else { // Si el proceso NO TRAE toda la informacion (Es nuevo)
        modelProceso.estado = await this.datosEstado.find((estado) => estado.nombre === modelProceso.estado).idestado
        modelProceso.empresa = await this.datosEmpresas.find((empresa) => empresa.nombre === modelProceso.empresa.toUpperCase()).id_empresa
        modelProceso.servicio = await this.datosServicios.find((servicio) => servicio.servicio === modelProceso.servicio).idservicio
      }
      return modelProceso
    },
    getEmpresasProceso(modelProceso) {
      // const empresas = JSON.parse(window.localStorage.getItem('empresas')) // Se capturan los datos de las empresas
      this.datosEmpresas = this.empresas.filter((empresa) => empresa.idservicio === modelProceso.servicio) // Se obtienen las empresas asociadas al servicio publico del proceso
      console.log('getEmpresasProceso -> ', this.datosEmpresas)
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
      this.showButtonsModal = true
    },
    closeModalEtapa() {
      this.msgEtapasVisible = false
      this.showButtons = true
      this.showButtonsModal = false
    },
    clickAgregarEtapa() {
      this.editarEtapa = false
      this.textEditarEtapa = 'Agregar'
      this.formAgregar = {}
      if (this.$refs['formAgregar']) {
        this.$refs['formAgregar'].resetFields()
      }
      this.msgAgregarEtapaVisible = true
    },
    async handleEtapa() {
      if (!this.editarEtapa) { // Condicion para AGREGAR una etapa (No es modo editar etapa)
        const modelAgregarEtapa = this.formAgregar
        this.$refs['formAgregar'].validate(async(valid) => {
          if (valid) {
            this.loadingEtapa = true
            modelAgregarEtapa.idproceso = this.formProceso.idproceso
            // modelAgregarEtapa.radicadoEtapa = `P${this.formProceso.idproceso}${this.estampillaEtapa}`
            if (!modelAgregarEtapa.hasOwnProperty('fechaFinEtapa')) {
              // console.log('esta vacio fecha fin!')
              modelAgregarEtapa.fechaFinEtapa = null
            }
            if (!modelAgregarEtapa.hasOwnProperty('observacionEtapa')) {
              // console.log('esta vacio observacion!')
              modelAgregarEtapa.observacionEtapa = ''
            }
            this.msgAgregarEtapaVisible = false
            this.loading = true
            this.datosEtapa = []
            // console.log('FORMAGREGAR -> ', modelAgregarEtapa)
            await createEtapa(modelAgregarEtapa).then(async(response) => {
              // console.log('RESPONSE AGREGAR -> ', response)
              this.$notify({
                title: 'Buen trabajo!',
                message: 'Etapa agregada con éxito',
                type: 'success',
                duration: 2000
              })
              await this.getEtapasProceso(this.formProceso.idproceso)
              await this.getEtapas()
              this.fetchData(this.formProceso.idproceso)
              this.loading = false
              this.loadingEtapa = false
            })
          } else {
            console.log('error submit!!')
            return false
          }
        })
      } else { // Condicion para EDITAR una etapa (modo editar etapa)
        const modelEditarEtapa = this.formAgregar
        this.$refs['formAgregar'].validate(async(valid) => {
          if (valid) {
            this.loadingEtapa = true
            this.loading = true
            this.datosEtapa = []
            delete modelEditarEtapa['etapa']
            modelEditarEtapa.idproceso = this.formProceso.idproceso
            console.log('FORMEDITAR -> ', modelEditarEtapa)
            await updateEtapa(modelEditarEtapa).then(async(response) => {
              // console.log('RESPONSE AGREGAR -> ', response)
              this.$notify({
                title: 'Buen trabajo!',
                message: 'Etapa modificada con éxito',
                type: 'success',
                duration: 2000
              })
              this.msgAgregarEtapaVisible = false
              await this.getEtapasProceso(this.formProceso.idproceso)
              await this.getEtapas()
              this.fetchData(this.formProceso.idproceso)
              this.loading = false
              this.loadingEtapa = false
            })
          } else {
            console.log('error submit!!')
            return false
          }
        })
      }
    },
    selectEtapa(data) {
      this.estampillaEtapa = this.datosEtapa.find(etapa => etapa.idetapa === data).estampilla
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
    handleBorrarEtapa(data) {
      this.delradEtapa = data.radicadoEtapa
      this.delIdetapa = data.idetapa
      this.delEtapa = data.nombreEtapa
      this.deleteDialogVisible = true
    },
    async borrarEtapa() {
      this.loadingEtapa = true
      const modelEtapaDel = {
        idproceso: this.formProceso.idproceso,
        idetapa: this.delIdetapa,
        radicadoEtapa: this.delradEtapa
      }
      await deleteEtapa(modelEtapaDel).then(async(response) => {
        this.deleteDialogVisible = false
        this.loading = true
        this.$notify({
          title: 'Información',
          message: 'Se ha eliminado la etapa',
          type: 'success',
          duration: 2000
        })
        await this.getEtapasProceso(this.formProceso.idproceso)
        await this.getEtapas()
        this.fetchData(this.formProceso.idproceso)
        this.loading = false
        this.loadingEtapa = false
      })
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
            await getProceso(this.id).then(async(response) => { // Se actulizan los datos del proceso
              // console.log('ACTUALIZAR PROCESO -> ', response)
              modelProceso = response[0]
              this.textEditarProceso = 'Editar'
              this.textActualizar = 'Actualizar'
              // modelProceso = await this.verificarDataModel(modelProceso, true)
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

<style lang="scss" scoped>
.control-modal-agregar {
  width: 25em;
}

.dashboard-editor-container {
  // padding: 32px;
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
    // padding: 16px 16px 0;
    // margin-bottom: 32px;
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

.dialog-class-ldetalle .el-dialog__header {
  border-radius: 10px;
  display: none;
}

.dialog-class-ldetalle .el-dialog__body {
  margin: 0 !important;
  padding: 0 !important;
  height: 100%;
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
