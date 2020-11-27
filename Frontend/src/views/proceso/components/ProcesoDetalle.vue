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
                  maxlength="15"
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

              <el-form-item label="Usuario" prop="usuario">
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

              <el-form-item label="Estado">
                <el-select
                  v-model="formProceso.estado"
                  filterable
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

              <el-form-item label="Tipo sancion" prop="tipo_sancion">
                <el-select
                  v-model="formProceso.tipo_sancion"
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
                  class="control-modal"
                  autocomplete="off"
                />
              </el-form-item>

              <el-form-item label="Decisión" prop="decision">
                <el-select
                  v-model="formProceso.decision"
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

          <el-col :md="8" style="border: 0px solid blue">
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>Causal</span>
              </div>

              <el-form-item label="Causa" prop="causa">
                <el-select
                  v-model="formProceso.causa"
                  filterable
                  placeholder="Seleccione una causal"
                  class="control-modal"
                >
                  <el-option
                    v-for="item in datosCausal"
                    :key="item.idcausal"
                    :label="item.nombre"
                    :value="item.idcausal"
                  />
                </el-select>
              </el-form-item>

              <el-form-item label="Fecha hechos" prop="fecha_hechos">
                <el-date-picker
                  v-model="formProceso.fecha_hechos"
                  type="date"
                  placeholder="Seleccione una fecha"
                  class="control-modal"
                />
              </el-form-item>

              <el-form-item label="Descripción">
                <el-input
                  v-model="formProceso.descripcion"
                  type="textarea"
                  class="control-modal"
                  rows="15"
                />
              </el-form-item>
            </el-card>
          </el-col>

          <!-- Datos caducidad / etapas -->

          <el-col :md="8" style="border: 0px solid blue">
            <el-row :gutter="10">
              <!-- Card datos caducidad -->

              <el-col :md="24" style="border: 0px solid blue">
                <el-card class="box-card">
                  <div slot="header" class="clearfix">
                    <span>Caducidad</span>
                  </div>
                  <el-form-item label="Caducidad" prop="caducidad">
                    <el-date-picker
                      v-model="formProceso.caducidad"
                      type="date"
                      placeholder="Seleccione una fecha"
                      class="control-modal"
                      :disabled="!editarProceso"
                    />
                  </el-form-item>
                </el-card>
              </el-col>

              <!-- Card datos etapa -->

              <el-col
                :md="24"
                style="border: 0px solid blue; padding-top: 10px"
              >
                <el-card class="box-card">
                  <div slot="header" class="clearfix">
                    <span>Etapas</span>
                  </div>
                  <el-form-item label="Actual" prop="etapa">
                    <el-input
                      v-model="formProceso.etapa"
                      autocomplete="off"
                      placeholder="Etapa actual"
                      style="width: 18em"
                      readonly
                    />
                  </el-form-item>

                  <el-form-item label="Siguiente" prop="prox_etapa">
                    <el-input
                      v-model="prox_etapa"
                      autocomplete="off"
                      placeholder="Siguiente etapa"
                      style="width: 18em"
                      readonly
                    />
                  </el-form-item>
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
                    style="border: 0px solid #67c23a; width: 10em"
                    :type="editarProceso ? 'danger' : 'primary'"
                    :icon="editarProceso ? 'el-icon-error' : 'el-icon-edit'"
                    @click="editarProceso = !editarProceso; editarForm();"
                  >{{ textEditarProceso }}</el-button>
                  <el-button
                    style="width: 10em"
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
      custom-class="dialog-class-ldetalle"
    >
      <div style="padding-bottom: 10px">
        <sticky
          :z-index="10"
          class-name="sub-navbar"
          style="position: fixed width: 99%;"
        >
          <div style="border: 0px solid red">

            <!-- Boton para agregar nueva etapa al aplicativo -->
            <transition name="el-zoom-in-center">
              <div v-show="showButtonsModal">
                <el-button
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
          </div>
        </sticky>
      </div>
      <div class="app-container">
        <el-table
          v-loading="loading"
          :z-index="0"
          :data="
            datosEtapaProceso.filter(
              (data) =>
                !busquedaEtapa ||
                data.nombreEtapa
                  .toLowerCase()
                  .includes(busquedaEtapa.toLowerCase())
            )
          "
          style="width: 100%; border: 1px solid #d8ebff"
          border
        >
          <el-table-column
            v-for="column in tableColumns"
            :key="column.label"
            :label="column.label"
            :prop="column.prop"
            align="center"
            :width="column.prop === 'observacionEtapa' ? 400 : ''"
            sortable
          />
          <el-table-column align="center" width="230">
            <!-- eslint-disable-next-line -->
            <template slot="header" slot-scope="scope">
              <el-input
                v-model="busquedaEtapa"
                size="mini"
                placeholder="Nombre etapa"
              />
            </template>
            <template slot-scope="scope">
              <el-button
                style="border: 1px solid #409eff"
                size="mini"
                type="success"
                icon="el-icon-edit"
                @click="handleEditarEtapa(scope);"
              ><b>Editar</b></el-button>
              <el-button
                :disabled="scope.row.nombreEtapa === 'Memorando IG'"
                size="mini"
                type="danger"
                icon="el-icon-delete-solid"
                @click="handleBorrarEtapa(scope.row)"
              />
            </template>
          </el-table-column>
        </el-table>
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

          <el-form-item label="Fecha inicio" prop="fecha_inicio">
            <el-date-picker
              v-model="formAgregar.fecha_inicio"
              type="date"
              placeholder="Seleccione fecha inicio"
              class="control-modal-agregar"
            />
          </el-form-item>

          <el-form-item label="Fecha fin" prop="fecha_fin">
            <el-date-picker
              v-model="formAgregar.fecha_fin"
              type="date"
              placeholder="Seleccione fecha fin"
              class="control-modal-agregar"
            />
          </el-form-item>

          <el-form-item label="Observación" prop="observacion">
            <el-input
              v-model="formAgregar.observacion"
              type="textarea"
              class="control-modal-agregar"
              rows="8"
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
import { getListEstado } from '@/api/procesosDIEG/estado'
import { getListTiposancion } from '@/api/procesosDIEG/tiposancion'
import { getListDecision } from '@/api/procesosDIEG/decision'
import { getListCausal } from '@/api/procesosDIEG/causal'
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

export default {
  name: 'ProcesoDetalle',
  directives: { elDragDialog },
  components: { Sticky },
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
      datosServicios: [],
      datosEmpresas: [],
      datosEstado: [],
      datosTiposancion: [],
      datosDecision: [],
      datosCausal: [],
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
      formAgregar: {},
      rulesFormProceso: CONSTANTS.rulesDetalleProceso,
      rulesFormEtapa: CONSTANTS.rulesFormEtapa,
      datosEtapa: [],
      /* Si es o no visible el cuadro de confirmación de eliminación */
      deleteDialogVisible: false,
      delradEtapa: '',
      delEtapa: '',
      estampillaEtapa: '',
      editarEtapa: false,
      textEditarEtapa: 'Agregar',
      showButtons: false,
      showButtonsModal: false
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
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
        console.log('ETAPA_PROCESO -> ', response)
        this.datosEtapaProceso = response
        // const nuevoarray = this.datosEtapaProceso.map((data) => {
        //   data.fechaInicioEtapa = moment(data.fechaInicioEtapa).format('DD/MM/YYYY HH:mm:ss')
        //   if (data.fechaFinEtapa === 'No registra') {
        //     data.fechaFinEtapa = null
        //   } else {
        //     data.fechaFinEtapa = moment(data.fechaFinEtapa).format('DD/MM/YYYY HH:mm:ss')
        //   }
        //   return data
        // })
        // console.log(nuevoarray)
      })
    },
    async initView() {
      this.getEstado()
      this.getTiposancion()
      this.getDecision()
      this.getCausal()
      await this.getEtapas()
      await this.fetchData(this.id)
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
    async getCausal() {
      await getListCausal().then((response) => {
        this.datosCausal = response
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
      this.datosUsuarios = JSON.parse(this.$route.params.usuarios) // Se capturan los parametros de la URL
      this.datosServicios = JSON.parse(this.$route.params.servicios) // Se capturan los parametros de la URL
      let modelProceso = {}
      await getProceso(id).then(async(response) => {
        console.log('RESPONSE -> ', response)
        if (response.length > 0) { // Se obtienen los datos del proceso si ya esta diligenciado en su totalidad
          console.log('RESPONSE proceso completo -> ', response)
          modelProceso = response[0]
          this.getEmpresasProceso(modelProceso)
          modelProceso = await this.verificarDataModel(modelProceso, true)
        } else { // Sino se cargan los datos del proceso completos (Esto pasa cuando se crea un proceso nuevo)
          await getProcesoInicial(id).then(async(response) => {
            console.log('RESPONSE inicial -> ', response)
            modelProceso = response[0]
            modelProceso.tipo_sancion = 9 // Se agrega el atributo al modelo del proceso
            modelProceso.decision = 6 // Se agrega el atributo al modelo del proceso un valor por defecto
            modelProceso.sancion = 0 // Se agrega el atributo al modelo del proceso
            modelProceso.descripcion = '' // Se agrega el atributo al modelo del proceso
            this.getEmpresasProceso(modelProceso)
            modelProceso = await this.verificarDataModel(modelProceso, false)
          })
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
        console.log('fetchData 3 -> ', this.$refs['formProceso'])
      }).catch((err) => {
        console.log(err)
      })
    },
    async verificarDataModel(modelProceso, infoCompleta) {
      if (infoCompleta) { // Si el proceso TRAE toda lainformacion
        modelProceso.estado = await this.datosEstado.find((estado) => estado.nombre === modelProceso.estado).idestado
        modelProceso.empresa = await this.datosEmpresas.find((empresa) => empresa.nombre === modelProceso.empresa.toUpperCase()).id_empresa
        modelProceso.servicio = await this.datosServicios.find((servicio) => servicio.servicio === modelProceso.servicio).idservicio
        modelProceso.causa = await this.datosCausal.find((causal) => causal.nombre === modelProceso.causa).idcausal
        modelProceso.decision = await this.datosDecision.find((decision) => decision.nombre === modelProceso.decision).iddecision
        modelProceso.tipo_sancion = await this.datosTiposancion.find((tiposancion) => tiposancion.nombre === modelProceso.tipo_sancion).idtiposancion
      } else { // Si el proceso NO TRAE toda lainformacion (Es nuevo)
        modelProceso.estado = await this.datosEstado.find((estado) => estado.nombre === modelProceso.estado).idestado
        modelProceso.empresa = await this.datosEmpresas.find((empresa) => empresa.nombre === modelProceso.empresa.toUpperCase()).id_empresa
        modelProceso.servicio = await this.datosServicios.find((servicio) => servicio.servicio === modelProceso.servicio).idservicio
      }
      return modelProceso
    },
    getEmpresasProceso(modelProceso) {
      const empresas = JSON.parse(window.localStorage.getItem('empresas')) // Se capturan los datos de las empresas
      this.datosEmpresas = empresas.filter((empresa) => empresa.servicio === modelProceso.servicio) // Se obtienen las empresas asociadas al servicio publico del proceso
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
      console.log('clickAgregarEtapa -> ', this.$refs['formAgregar'])
    },
    async handleEtapa() {
      if (!this.editarEtapa) { // Condicion para AGREGAR una etapa (No es modo editar etapa)
        const modelAgregarEtapa = this.formAgregar
        modelAgregarEtapa.idproceso = this.formProceso.idproceso
        modelAgregarEtapa.radicado = `P${this.formProceso.idproceso}${this.estampillaEtapa}`
        if (!modelAgregarEtapa.hasOwnProperty('fecha_fin')) {
          console.log('esta vacio fecha fin!')
          modelAgregarEtapa.fecha_fin = null
        }
        if (!modelAgregarEtapa.hasOwnProperty('observacion')) {
          console.log('esta vacio observacion!')
          modelAgregarEtapa.observacion = ''
        }
        this.$refs['formAgregar'].validate(async(valid) => {
          if (valid) {
            this.msgAgregarEtapaVisible = false
            this.loading = true
            this.datosEtapa = []
            console.log('FORMAGREGAR -> ', modelAgregarEtapa)
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
            this.msgAgregarEtapaVisible = false
            this.loading = true
            this.datosEtapa = []
            delete modelEditarEtapa['etapa']
            console.log('FORMEDITAR -> ', modelEditarEtapa)
            await updateEtapa(modelEditarEtapa).then(async(response) => {
              // console.log('RESPONSE AGREGAR -> ', response)
              this.$notify({
                title: 'Buen trabajo!',
                message: 'Etapa modificada con éxito',
                type: 'success',
                duration: 2000
              })
              await this.getEtapasProceso(this.formProceso.idproceso)
              await this.getEtapas()
              this.fetchData(this.formProceso.idproceso)
              this.loading = false
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
      this.formAgregar = {}
      if (this.$refs['formAgregar']) {
        this.$refs['formAgregar'].resetFields()
      }
      this.msgAgregarEtapaVisible = false
      console.log('closeModalAgregar -> ', this.$refs['formAgregar'])
    },
    handleEditarEtapa(etapa) {
      this.editarEtapa = true
      this.textEditarEtapa = 'Actualizar'
      this.formAgregar = {}
      if (this.$refs['formAgregar']) {
        this.$refs['formAgregar'].resetFields()
      }
      this.msgAgregarEtapaVisible = true
      // console.log('clickAgregarEtapa -> ', this.$refs['formAgregar'])
      const modelEditarEtapa = {}
      try {
        modelEditarEtapa.radicado = etapa.row.radicadoEtapa
        modelEditarEtapa.etapa = etapa.row.nombreEtapa
        modelEditarEtapa.observacion = etapa.row.observacionEtapa
        modelEditarEtapa.fecha_inicio = moment(etapa.row.fechaInicioEtapa).format()
        if (etapa.row.fechaFinEtapa === 'No registra') {
          modelEditarEtapa.fecha_fin = null
        } else {
          modelEditarEtapa.fecha_fin = moment(etapa.row.fechaFinEtapa).format()
        }
        this.formAgregar = modelEditarEtapa
        console.log('handleEditarEtapa -> ', this.formAgregar)
      } catch (error) {
        console.log(error)
      }
    },
    handleBorrarEtapa(data) {
      this.delradEtapa = data.radicadoEtapa
      this.delEtapa = data.nombreEtapa
      this.deleteDialogVisible = true
    },
    async borrarEtapa() {
      await deleteEtapa(this.delradEtapa).then(async(response) => {
        this.deleteDialogVisible = false
        this.loading = true
        this.$notify({
          title: 'Información',
          message: 'Se ha eliminado la etapa',
          type: 'warning',
          duration: 2000
        })
        await this.getEtapasProceso(this.formProceso.idproceso)
        await this.getEtapas()
        this.fetchData(this.formProceso.idproceso)
        this.loading = false
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
              console.log('ACTUALIZAR PROCESO -> ', response)
              modelProceso = response[0]
              this.textEditarProceso = 'Editar'
              this.textActualizar = 'Actualizar'
              modelProceso = await this.verificarDataModel(modelProceso, true)
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
          console.log('error submit!!')
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
</style>

<style lang="scss">
.dialog-class-ldetalle .el-dialog__header {
  border: 1px solid red;
  border-radius: 10px;
  display: none;
}

.dialog-class-ldetalle .el-dialog__body {
  margin: 0 !important;
  padding: 0 !important;
}
</style>
