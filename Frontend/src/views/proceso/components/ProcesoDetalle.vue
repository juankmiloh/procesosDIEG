<template>
  <div v-loading="loading" class="createPost-container">
    <el-form ref="postForm" :model="proceso" class="form-container">
      <sticky :z-index="10" class-name="sub-navbar">
        <div style="border: 0px solid red">
          <!-- Boton para agregar nuevo expediente al aplicativo -->

          <el-button
            style="border: 1px solid #67c23a"
            size="medium"
            icon="el-icon-top-right"
            round
            @click="
              msgEtapasVisible = true;
            "
          >Ingresar a las etapas</el-button>
        </div>
      </sticky>
      <div class="app-container">
        <el-form-item
          label="Número de Expediente"
          :label-width="formLabelWidth"
        >
          <el-input
            v-model="proceso.radicado"
            placeholder="Ingrese el número del radicado"
            :disabled="edicion"
          />
        </el-form-item>

        <el-form-item label="Empresa" :label-width="formLabelWidth">
          <el-select
            v-model="proceso.empresa"
            placeholder="Seleccione una empresa"
            :disabled="edicion"
          >
            <el-option label="Empresa 1" value="Empresa 1" />
            <el-option label="Empresa 2" value="Empresa 2" />
          </el-select>
        </el-form-item>

        <el-form-item label="Usuario Asignado" :label-width="formLabelWidth">
          <el-select
            v-model="proceso.usuarioAsignado"
            placeholder="Seleccione un usuario"
            :disabled="edicion"
          >
            <el-option label="Usuario 1" value="Usuario 1" />
            <el-option label="Usuario 2" value="Usuario 2" />
          </el-select>
        </el-form-item>

        <el-form-item label="Estado" :label-width="formLabelWidth">
          <el-input
            v-model="proceso.estado"
            placeholder="Ingrese el estado"
            :disabled="edicion"
          />
        </el-form-item>

        <el-form-item label="Causa" :label-width="formLabelWidth">
          <el-select
            v-model="proceso.usuarioAsignado"
            placeholder="Seleccione una causa"
            :disabled="edicion"
          >
            <el-option label="Causal 1" value="Causal 1" />
            <el-option label="Causal 2" value="Causal 2" />
          </el-select>
        </el-form-item>

        <el-form-item label="Fecha Hechos" :label-width="formLabelWidth">
          <el-date-picker
            v-model="proceso.fechaHechos"
            type="date"
            placeholder="Seleccione un dia"
            :disabled="edicion"
          />
        </el-form-item>

        <el-form-item label="Fecha Caducidad" :label-width="formLabelWidth">
          <el-date-picker
            v-model="proceso.fechaCaducidad"
            type="date"
            placeholder="Seleccione un dia"
            :disabled="edicion"
          />
        </el-form-item>

        <el-form-item label="Siguiente etapa" :label-width="formLabelWidth">
          <el-select
            v-model="proceso.usuarioAsignado"
            placeholder="Seleccione la etapa siguiente"
            :disabled="edicion"
          >
            <el-option label="Etapa 1" value="Etapa 1" />
            <el-option label="Etapa 2" value="Etapa 2" />
          </el-select>
        </el-form-item>

        <el-form-item label="Tipo de sanción" :label-width="formLabelWidth">
          <el-select
            v-model="proceso.tipoSancion"
            placeholder="Seleccione el tipo de Sanción"
            :disabled="edicion"
          >
            <el-option label="Sanción 1" value="Sanción 1" />
            <el-option label="Sanción 2" value="Sanción 2" />
          </el-select>
        </el-form-item>

        <el-form-item label="Monto de la sanción" :label-width="formLabelWidth">
          <el-input-number
            v-model="proceso.montoSancion"
            placeholder="Ingrese el valor de la sanción"
            :disabled="edicion"
          />
        </el-form-item>

        <el-form-item
          label="Descisión del recurso"
          :label-width="formLabelWidth"
        >
          <el-select
            v-model="proceso.descisionRecurso"
            placeholder="Seleccione la descisión tomada"
            :disabled="edicion"
          >
            <el-option label="Descisión 1" value="Descisión 1" />
            <el-option label="Descisión 2" value="Descisión 2" />
          </el-select>
        </el-form-item>
      </div>
    </el-form>

    <el-button>Cancelar</el-button>
    <el-button>Guardar</el-button>

    <!-- Cuadro de dialogo de etapas -->

    <el-dialog :visible.sync="msgEtapasVisible" :show-close="false" fullscreen>
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
          style="width: 100%"
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

    <el-dialog title="Etapas" :visible.sync="msgEtapaVisible">
      <el-form :model="proceso.etapas[etapaEditar]">
        <el-form-item label="Etapa" :label-width="formLabelWidth">
          <el-select
            v-model="proceso.etapas[etapaEditar].nombreEtapa"
            placeholder="Seleccione la etapa siguiente"
            :disabled="edicion"
          >
            <el-option label="Etapa 1" value="Etapa 1" />
            <el-option label="Etapa 2" value="Etapa 2" />
          </el-select>
        </el-form-item>

        <el-form-item label="Radicado" :label-width="formLabelWidth">
          <input
            v-model="proceso.etapas[etapaEditar].radicadoEtapa"
            :disabled="edicion"
          >
        </el-form-item>

        <el-form-item label="Fecha Inicio" :label-width="formLabelWidth">
          <el-date-picker
            v-model="proceso.etapas[etapaEditar].fechaInicioEtapa"
            type="date"
            placeholder="Seleccione un dia"
            :disabled="edicion"
          />
        </el-form-item>

        <el-form-item label="Fecha Fin" :label-width="formLabelWidth">
          <el-date-picker
            v-model="proceso.etapas[etapaEditar].fechaFinEtapa"
            type="date"
            placeholder="Seleccione un dia"
            :disabled="edicion"
          />
        </el-form-item>

        <el-form-item label="Observación" :label-width="formLabelWidth">
          <input
            v-model="proceso.etapas[etapaEditar].observacionEtapa"
            :disabled="edicion"
          >
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="msgEtapaVisible = false">Cancelar</el-button>
        <el-button
          type="primary"
          @click="msgEtapaVisible = false"
        >Aceptar</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getProceso } from '@/api/procesosDIEG/procesos'
import Sticky from '@/components/Sticky' // 粘性header组件

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
      proceso: {
        radicado: '20091010101010',
        empresa: 'Empresa 1',
        usuarioAsignado: 'Usuario 1',
        estado: 'Estado 1',
        causal: 'Causal 1',
        fechaHechos: '2017-12-20',
        fechaCaducidad: '2020-12-20',
        nombreSiguienteEtapa: 'Finalizado',
        tipoSancion: 'Sanción 1',
        montoSancion: '1000000',
        descisionRecurso: 'Descisión 2',
        etapas: [
          {
            nombreEtapa: 'Radicación',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2017-12-20',
            fechaFinEtapa: '2018-01-20',
            observacionEtapa: ''
          },
          {
            nombreEtapa: 'Memorando',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-01-20',
            fechaFinEtapa: '2018-01-30',
            observacionEtapa: ''
          },
          {
            nombreEtapa: 'Informe de Gestión',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-01-30',
            fechaFinEtapa: '2018-07-30',
            observacionEtapa:
              'Se requrio explicación mediante radicado 2000XYX'
          },
          {
            nombreEtapa: 'Indagación Preeliminar - Auto',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-07-30',
            fechaFinEtapa: '2018-09-30',
            observacionEtapa: ''
          },
          {
            nombreEtapa: 'Probatoria - Auto de pruebas',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-09-30',
            fechaFinEtapa: '2018-12-02',
            observacionEtapa: ''
          },
          {
            nombreEtapa: 'Translado de alegatos - Auto',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-12-02',
            fechaFinEtapa: '2019-02-03',
            observacionEtapa:
              'Se dio translado a todos por parte de gestión documental'
          },
          {
            nombreEtapa: 'Translado de alegatos - Alegatos',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-02-03',
            fechaFinEtapa: '2019-02-12',
            observacionEtapa: ''
          },
          {
            nombreEtapa: 'Pliego de cargos',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-02-12',
            fechaFinEtapa: '2019-04-15',
            observacionEtapa: ''
          },
          {
            nombreEtapa: 'Descargos',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-04-15',
            fechaFinEtapa: '2019-04-30',
            observacionEtapa: ''
          },
          {
            nombreEtapa: 'Sancion',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-04-30',
            fechaFinEtapa: '2019-06-01',
            observacionEtapa: 'Sanción por monto de $ 1.000.000'
          },
          {
            nombreEtapa: 'Recurso de reposición - Radicación',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-06-01',
            fechaFinEtapa: '2019-06-10',
            observacionEtapa: ''
          },
          {
            nombreEtapa: 'Resolución recurso',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-06-10',
            fechaFinEtapa: '2019-11-01',
            observacionEtapa: ''
          },
          {
            nombreEtapa: 'Firmeza',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-11-01',
            fechaFinEtapa: '2019-12-18',
            observacionEtapa: 'En espera a tutela'
          }
        ]
      },
      /* Si es o no visible el cuadro de dialogo de agregar o editar etapa */
      msgEtapaVisible: false,
      /* Para la edición de una etapa */
      etapaEditar: '0',
      /* Si es o no visible el cuadro de dialogo de las etapas */
      msgEtapasVisible: false,
      /* Si es o no para editar */
      edicion: false,
      /* Tamaño del formulario */
      formLabelWidth: '200px',
      // postForm: Object.assign({}, defaultForm),
      postForm: Object.assign({}),
      loading: false,
      userListOptions: [],
      tempRoute: {}
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    if (this.isDetail) {
      const id = this.$route.params && this.$route.params.id
      console.log('ID PARAMS -> ', id)
      this.fetchData(id)
    } else {
      this.postForm = Object.assign({})
    }

    // Why need to make a copy of this.$route here?
    // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
    // https://github.com/PanJiaChen/vue-element-admin/issues/1221
    this.tempRoute = Object.assign({}, this.$route)
  },
  methods: {
    fetchData(id) {
      getProceso(id)
        .then((response) => {
          this.postForm = response[0]
          console.log('DATA PROCESO -> ', this.postForm)

          // set tagsview title
          this.setTagsViewTitle()

          // set page title
          this.setPageTitle()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    setTagsViewTitle() {
      const title = 'Proceso'
      const route = Object.assign({}, this.tempRoute, {
        title: `${title} ${this.postForm.expediente}`
      })
      this.$store.dispatch('tagsView/updateVisitedView', route)
    },
    setPageTitle() {
      const title = 'Proceso'
      document.title = `${title} - ${this.postForm.expediente}`
    },
    submitForm() {
      console.log(this.postForm)
      this.$refs.postForm.validate((valid) => {
        if (valid) {
          this.loading = true
          this.$notify({
            title: '成功',
            message: '发布文章成功',
            type: 'success',
            duration: 2000
          })
          this.postForm.status = 'published'
          this.loading = false
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

<style lang="scss">
  .dialog-class .el-dialog__header {
    border: 1px solid red;
    border-radius: 10px;
    display: none;
  }

  .dialog-class .el-dialog__body {
    margin: 0 !important;
    padding: 0 !important;
  }
</style>
