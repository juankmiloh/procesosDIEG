<template>
  <div class="createPost-container" style="background: #f7fbff; height: 89vh;">
    <sticky class-name="sub-navbar">
      <div style="border: 0px solid red">

        <!-- Boton para abrir modal de etapas -->
        <transition name="el-zoom-in-center">
          <el-button
            v-show="!loading"
            style="border: 2px solid #67c23a"
            size="medium"
            icon="el-icon-top-right"
            round
            @click="msgEtapasVisible = true"
          >Ingresar a las etapas</el-button>
        </transition>
      </div>
    </sticky>

    <!-- Cuadro de dialogo de etapas -->

    <el-dialog :visible.sync="msgEtapasVisible" :show-close="false" fullscreen custom-class="dialog-class-ldetalle">
      <!-- Boton para agregar nuevo expediente al aplicativo -->
      <div style="padding-bottom: 60px;">
        <sticky :z-index="10" class-name="sub-navbar" style="position: fixed; width: 99%;">
          <div style="border: 0px solid red">
            <!-- Boton para agregar nuevo expediente al aplicativo -->

            <el-button
              style="border: 1px solid #67c23a"
              type="success"
              size="medium"
              icon="el-icon-circle-plus"
              @click="
                msgEtapaVisible = true;
              "
            >Agregar etapa</el-button>
            <el-button
              style="border: 1px solid #67c23a"
              type="warning"
              size="medium"
              @click="msgEtapasVisible = false"
            >Cerrar</el-button>
          </div>
        </sticky>
      </div>
      <div class="app-container">
        <el-table
          def="etapas"
          :data="proceso.etapas"
          :default-sort="{ prop: 'fechaInicioEtapa', order: 'descending' }"
          style="width: 100%; z-index: 0;"
          border
        >
          <!-- Etapa -->
          <el-table-column
            prop="nombreEtapa"
            label="Etapa"
            sortable
            column-key="nombreEtapa"
            align="center"
          />

          <!-- Radicado -->
          <el-table-column
            prop="radicadoEtapa"
            label="Radicado"
            sortable
            column-key="radicadoEtapa"
          />

          <!-- Fecha de Inicio -->
          <el-table-column
            prop="fechaInicioEtapa"
            label="Fecha de Inicio"
            sortable
            column-key="fechaInicioEtapa"
          />

          <!-- Fecha de Fin -->
          <el-table-column
            prop="fechaFinEtapa"
            label="Fecha de Fin"
            sortable
            column-key="fechaFinEtapa"
          />

          <!-- Observación -->
          <el-table-column
            prop="observacionEtapa"
            label="Observación"
            sortable
            column-key="observacionEtapa"
          />

          <!-- Columna donde se ponen los botones de permisos y quitar -->
          <el-table-column>
            <template slot-scope="scope">
              <!-- Boton de permisos -->
              <el-button
                size="mini"
                @click="
                  msgEtapaVisible = true;
                  etapaEditar = scope.$index;
                "
              >Editar</el-button>

              <!-- Boton de eliminar -->
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)"
              >Quitar</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </el-dialog>

    <!-- Cuadro de dialogo para editar o asignar etapa -->

    <!-- Formulario donde se cargan los datos del proceso -->

    <div v-loading="loading" class="app-container">
      <el-row :gutter="10">

        <!-- Card datos proceso -->
        <el-form ref="formProceso" :model="formProceso" label-width="120px">

          <el-col :md="8" style="border: 0px solid blue">
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>Proceso</span>
              </div>

              <el-form-item label="Expediente" prop="radicado">
                <el-input
                  v-model="formProceso.expediente"
                  autocomplete="off"
                  placeholder="Ingrese No. del expediente"
                  maxlength="14"
                  show-word-limit
                  class="control-modal"
                />
              </el-form-item>

              <el-form-item label="Servicio" prop="servicio">
                <el-select
                  v-model="formProceso.servicio"
                  filterable
                  placeholder="Seleccione el servicio"
                  class="control-modal"
                  :disabled="!editar"
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
                  :disabled="!editar"
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
                  :disabled="!editar"
                >
                  <el-option
                    v-for="item in datosUsuarios"
                    :key="item.idusuario"
                    :label="item.nombre + ' ' + item.apellido"
                    :value="item.idusuario"
                  />
                </el-select>
              </el-form-item>

              <el-form-item label="Estado" prop="estado">
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
                    :disabled="!editar"
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

              <el-form-item
                label="Monto sanción"
                prop="sancion"
              >
                <el-input-number v-model.number="formProceso.sancion" class="control-modal" autocomplete="off" />
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
                <el-input v-model="formProceso.descripcion" type="textarea" class="control-modal" rows="15" />
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
                  <el-form-item label="Caducidad" prop="fecha_caducidad">
                    <el-date-picker
                      v-model="formProceso.caducidad"
                      type="date"
                      placeholder="Seleccione una fecha"
                      class="control-modal"
                      :disabled="!editar"
                    />
                  </el-form-item>
                </el-card>
              </el-col>

              <!-- Card datos etapa -->

              <el-col :md="24" style="border: 0px solid blue; padding-top: 10px;">
                <el-card class="box-card">
                  <div slot="header" class="clearfix">
                    <span>Etapas</span>
                  </div>
                  <el-form-item label="Actual" prop="etapa">
                    <el-input
                      v-model="formProceso.etapa"
                      autocomplete="off"
                      placeholder="Etapa actual"
                      style="width: 18em;"
                      readonly
                    />
                  </el-form-item>

                  <el-form-item label="Siguiente" prop="prox_etapa">
                    <el-input
                      v-model="formProceso.proxetapa"
                      autocomplete="off"
                      placeholder="Siguiente etapa"
                      style="width: 18em;"
                      readonly
                    />
                  </el-form-item>
                </el-card>
              </el-col>

              <!-- Boton  / editar / actualizar -->

              <el-col :md="24" style="border: 0px solid blue">
                <el-card class="box-card" shadow="never" style="background: none; border: 0; text-align: center;">
                  <el-button
                    style="border: 0px solid #67c23a; width: 10em;"
                    :type="editar ? 'danger' : 'primary'"
                    :icon="editar ? 'el-icon-error' : 'el-icon-edit'"
                    @click="editar = !editar; editarForm()"
                  >{{ textEditar }}</el-button>
                  <el-button
                    style="width: 10em;"
                    :type="editar ? 'primary' : 'success'"
                    :icon="editar ? 'el-icon-circle-check' : 'el-icon-check'"
                    @click="submitForm('formProceso')"
                  >{{ textActualizar }}</el-button>
                </el-card>
              </el-col>
            </el-row>
          </el-col>
        </el-form>
      </el-row>
    </div>
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
import Sticky from '@/components/Sticky' // 粘性header组件
import { CONSTANTS } from '@/constants/constants'

export default {
  name: 'ProcesoDetalle',
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
      formProceso: Object.assign({}),
      /* Si es o no visible el cuadro de dialogo de agregar o editar etapa */
      msgEtapaVisible: false,
      /* Para la edición de una etapa */
      etapaEditar: '0',
      /* Si es o no visible el cuadro de dialogo de las etapas */
      msgEtapasVisible: false,
      /* Si es o no para editar */
      editar: false,
      textEditar: 'Editar',
      textActualizar: 'Actualizar',
      loading: false,
      userListOptions: [],
      tempRoute: {},
      proceso: CONSTANTS.etapas
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
      this.initView()
      this.fetchData(this.id)
    }

    // Why need to make a copy of this.$route here?
    // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
    // https://github.com/PanJiaChen/vue-element-admin/issues/1221
    this.tempRoute = Object.assign({}, this.$route)
  },
  methods: {
    initView() {
      this.getEstado()
      this.getTiposancion()
      this.getDecision()
      this.getCausal()
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
    async fetchData(id) {
      this.datosUsuarios = JSON.parse(this.$route.params.usuarios)
      this.datosServicios = JSON.parse(this.$route.params.servicios)
      const empresas = JSON.parse(window.localStorage.getItem('empresas'))
      await getProceso(id).then(async(response) => {
        console.log('RESPONSE -> ', response)
        if (response.length > 0) {
          this.formProceso = response[0]
          this.datosEmpresas = empresas.filter(empresa => empresa.servicio === this.formProceso.servicio)
          this.updateModel()
        } else {
          await getProcesoInicial(id).then((response) => {
            // console.log('RESPONSE inicial -> ', response)
            this.formProceso = response[0]
            this.datosEmpresas = empresas.filter(empresa => empresa.servicio === this.formProceso.servicio)
          })
        }
        // set tagsview title
        this.setTagsViewTitle()
        // set page title
        this.setPageTitle()
        this.loading = false
      }).catch((err) => {
        console.log(err)
      })
      this.updateModelInicial()
      if (!this.formProceso.hasOwnProperty('descripcion')) { this.formProceso.descripcion = '' }
    },
    updateModelInicial() {
      this.formProceso.estado = this.datosEstado.find(estado => estado.nombre === this.formProceso.estado).idestado
      this.formProceso.empresa = this.datosEmpresas.find(empresa => empresa.nombre === this.formProceso.empresa.toUpperCase()).id_empresa
      this.formProceso.servicio = this.datosServicios.find(servicio => servicio.servicio === this.formProceso.servicio).idservicio
      this.formProceso.usuario = this.datosUsuarios.find(usuario => `${usuario.nombre} ${usuario.apellido}` === this.formProceso.usuario).idusuario
    },
    updateModel() {
      this.formProceso.causa = this.datosCausal.find(causal => causal.nombre === this.formProceso.causa).idcausal
      this.formProceso.decision = this.datosDecision.find(decision => decision.nombre === this.formProceso.decision).iddecision
      this.formProceso.tipo_sancion = this.datosTiposancion.find(tiposancion => tiposancion.nombre === this.formProceso.tipo_sancion).idtiposancion
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
    async selectServicio(idservicio) {
      if (this.editar) { this.formProceso.empresa = '' }
      if (idservicio) {
        await getListEmpresas(idservicio).then((response) => {
          this.datosEmpresas = response.items
        })
      }
    },
    editarForm() {
      if (this.editar) {
        this.$notify({
          title: 'Advertencia',
          message: 'Has activado el modo edición!',
          type: 'warning',
          duration: 2000
        })
        this.textEditar = 'Cancelar'
        this.textActualizar = 'Aceptar'
        window.localStorage.setItem('form_save', JSON.stringify(this.formProceso))
      } else {
        this.$notify({
          title: 'info',
          message: 'Has desactivado el modo edición!',
          type: 'info',
          duration: 2000
        })
        this.textEditar = 'Editar'
        this.textActualizar = 'Actualizar'
        this.formProceso = JSON.parse(window.localStorage.getItem('form_save'))
        this.selectServicio(this.formProceso.servicio) // Se carga de nuevo la lista de las empresas del servicio guardado en memoria
        window.localStorage.removeItem('form_save')
      }
    },
    submitForm() {
      console.log('THISFORMPROCESO -> ', this.formProceso)
      this.$refs.formProceso.validate(async(valid) => {
        if (valid) {
          this.loading = true
          await updateProceso(this.formProceso).then(async(response) => {
            if (this.editar) {
              this.$notify({
                title: 'info',
                message: 'Se ha desactivado el modo edición!',
                type: 'info',
                duration: 2000
              })
            }
            await getProceso(this.id).then(async(response) => {
              console.log('ACTUALIZAR PROCESO -> ', response)
              this.formProceso = response[0]
              this.textEditar = 'Editar'
              this.textActualizar = 'Actualizar'
              await this.updateModelInicial()
              await this.updateModel()
              this.$notify({
                title: 'Bien hecho!',
                message: 'Expediente actualizado con éxito',
                position: this.editar ? 'top-right' : 'bottom-right',
                type: 'success',
                duration: 2000
              })
              this.editar = false
              this.loading = false
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
