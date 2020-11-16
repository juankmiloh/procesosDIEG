<template>
  <div class="components-container">

    <el-form :model="proceso">
      <el-form-item label="Número de Expediente" :label-width="formLabelWidth">
        <el-input
          v-model="proceso.radicado"
          placeholder="Ingrese el número del radicado"
          :disabled="edicion"
        />
      </el-form-item>

      <el-form-item label="Empresa" :label-width="formLabelWidth">
        <el-select v-model="proceso.empresa" placeholder="Seleccione una empresa" :disabled="edicion">
          <el-option label="Empresa 1" value="Empresa 1" />
          <el-option label="Empresa 2" value="Empresa 2" />
        </el-select>
      </el-form-item>

      <el-form-item label="Usuario Asignado" :label-width="formLabelWidth">
        <el-select v-model="proceso.usuarioAsignado" placeholder="Seleccione un usuario" :disabled="edicion">
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
        <el-select v-model="proceso.usuarioAsignado" placeholder="Seleccione una causa" :disabled="edicion">
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
        <el-select v-model="proceso.usuarioAsignado" placeholder="Seleccione la etapa siguiente" :disabled="edicion">
          <el-option label="Etapa 1" value="Etapa 1" />
          <el-option label="Etapa 2" value="Etapa 2" />
        </el-select>
      </el-form-item>

      <el-form-item label="Tipo de sanción" :label-width="formLabelWidth">
        <el-select v-model="proceso.tipoSancion" placeholder="Seleccione el tipo de Sanción" :disabled="edicion">
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

      <el-form-item label="Descisión del recurso" :label-width="formLabelWidth">
        <el-select v-model="proceso.descisionRecurso" placeholder="Seleccione la descisión tomada" :disabled="edicion">
          <el-option label="Descisión 1" value="Descisión 1" />
          <el-option label="Descisión 2" value="Descisión 2" />
        </el-select>

      </el-form-item>
    </el-form>

    <el-button>Cancelar</el-button>
    <el-button>Guardar</el-button>

    <!-- Boton para agregar nuevo expediente al aplicativo -->

    <el-button
      style="margin-bottom:20px"
      @click="msgEtapasVisible = true"
    >Ingresar a las Etapas</el-button>

    <!-- Cuadro de dialogo de etapas -->

    <el-dialog title="Etapas" :visible.sync="msgEtapasVisible">

      <!-- Boton para agregar nuevo expediente al aplicativo -->

      <el-button size="mini" :disabled="edicion" @click="msgEtapaVisible = true">Agregar</el-button>

      <el-table
        def="etapas"
        :data="proceso.etapas"
        :default-sort="{prop: 'fechaInicioEtapa', order: 'descending'}"
        style="width:100%"
      >

        <!-- Etapa -->
        <el-table-column
          prop="nombreEtapa"
          label="Etapa"
          sortable
          column-key="nombreEtapa"
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
              @click="msgEtapaVisible = true;etapaEditar = scope.$index"
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

      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="msgEtapasVisible = false">Cancelar</el-button>
      </span>
    </el-dialog>

    <!-- Cuadro de dialogo para editar o asignar etapa -->

    <el-dialog title="Etapas" :visible.sync="msgEtapaVisible">

      <el-form :model="proceso.etapas[etapaEditar]">

        <el-form-item label="Etapa" :label-width="formLabelWidth">
          <el-select v-model="proceso.etapas[etapaEditar].nombreEtapa" placeholder="Seleccione la etapa siguiente" :disabled="edicion">
            <el-option label="Etapa 1" value="Etapa 1" />
            <el-option label="Etapa 2" value="Etapa 2" />
          </el-select>
        </el-form-item>

        <el-form-item label="Radicado" :label-width="formLabelWidth">
          <input v-model="proceso.etapas[etapaEditar].radicadoEtapa" :disabled="edicion">
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
          <input v-model="proceso.etapas[etapaEditar].observacionEtapa" :disabled="edicion">
        </el-form-item>

      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button
          @click="msgEtapaVisible = false"
        >Cancelar</el-button>
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
import BackToTop from '@/components/BackToTop'

export default {
  name: 'ViewProceso',
  components: { BackToTop },
  data() {
    return {
      /* Estilo */
      myBackToTopStyle: {
        right: '50px',
        bottom: '50px',
        width: '40px',
        height: '40px',
        'border-radius': '4px',
        'line-height': '45px',
        background: '#e7eaf1'
      },
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
        etapas:
          [{
            nombreEtapa: 'Radicación',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2017-12-20',
            fechaFinEtapa: '2018-01-20',
            observacionEtapa: ''
          }, {
            nombreEtapa: 'Memorando',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-01-20',
            fechaFinEtapa: '2018-01-30',
            observacionEtapa: ''
          }, {
            nombreEtapa: 'Informe de Gestión',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-01-30',
            fechaFinEtapa: '2018-07-30',
            observacionEtapa: 'Se requrio explicación mediante radicado 2000XYX'
          }, {
            nombreEtapa: 'Indagación Preeliminar - Auto',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-07-30',
            fechaFinEtapa: '2018-09-30',
            observacionEtapa: ''
          }, {
            nombreEtapa: 'Probatoria - Auto de pruebas',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-09-30',
            fechaFinEtapa: '2018-12-02',
            observacionEtapa: ''
          }, {
            nombreEtapa: 'Translado de alegatos - Auto',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2018-12-02',
            fechaFinEtapa: '2019-02-03',
            observacionEtapa: 'Se dio translado a todos por parte de gestión documental'
          }, {
            nombreEtapa: 'Translado de alegatos - Alegatos',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-02-03',
            fechaFinEtapa: '2019-02-12',
            observacionEtapa: ''
          }, {
            nombreEtapa: 'Pliego de cargos',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-02-12',
            fechaFinEtapa: '2019-04-15',
            observacionEtapa: ''
          }, {
            nombreEtapa: 'Descargos',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-04-15',
            fechaFinEtapa: '2019-04-30',
            observacionEtapa: ''
          }, {
            nombreEtapa: 'Sancion',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-04-30',
            fechaFinEtapa: '2019-06-01',
            observacionEtapa: 'Sanción por monto de $ 1.000.000'
          }, {
            nombreEtapa: 'Recurso de reposición - Radicación',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-06-01',
            fechaFinEtapa: '2019-06-10',
            observacionEtapa: ''
          }, {
            nombreEtapa: 'Resolución recurso',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-06-10',
            fechaFinEtapa: '2019-11-01',
            observacionEtapa: ''
          }, {
            nombreEtapa: 'Firmeza',
            radicadoEtapa: '2000XXXXXX',
            fechaInicioEtapa: '2019-11-01',
            fechaFinEtapa: '2019-12-18',
            observacionEtapa: 'En espera a tutela'
          }]
      },
      /* Si es o no visible el cuadro de dialogo de agregar o editar etapa */
      msgEtapaVisible: false,
      /* Para la edición de una etapa */
      etapaEditar: '0',
      /* Si es o no visible el cuadro de dialogo de las etapas */
      msgEtapasVisible: false,
      /* Si es o no para editar */
      edicion: true,
      /* Tamaño del formulario */
      formLabelWidth: '200px'
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  },
  created() {

  },
  methods: {
    /* Metodo para realizar la busqueda de los filtro ubicado en las columnas */
    filterHandler(value, row, column) {
      const property = column['property']
      return row[property] === value
    }
  }
}
</script>

<style lang="scss" scoped>
	.placeholder-container div {
		margin: 10px;
	}
</style>
