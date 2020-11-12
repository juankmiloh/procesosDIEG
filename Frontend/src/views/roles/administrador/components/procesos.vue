<template>
  <div class="components-container">
    <!-- Cuadro de dialogo para agregar expediente -->

    <el-dialog title="Agregar Expediente" :visible.sync="msgAgregarVisible">
      <el-form :model="formAgregar">
        <el-form-item label="Expediente" :label-width="formLabelWidth">
          <el-input
            v-model="formAgregar.radicado"
            autocomplete="off"
            placeholder="Ingrese el número del expediente"
          />
        </el-form-item>
        <el-form-item label="Servicio" :label-width="formLabelWidth">
          <el-select v-model="formAgregar.servicio" placeholder="Seleccione el servicio" @change="selectServicio($event)">
            <el-option
              v-for="item in datosServicios"
              :key="item.idservicio"
              :label="item.servicio"
              :value="item.idservicio"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="Empresa" :label-width="formLabelWidth">
          <el-select v-model="formAgregar.empresa" :disabled="disableEmpresas" placeholder="Seleccione una empresa">
            <el-option
              v-for="item in datosEmpresas"
              :key="item.id_empresa"
              :label="item.nombre"
              :value="item.id_empresa"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="Usuario" :label-width="formLabelWidth">
          <el-select v-model="formAgregar.usuario" placeholder="Seleccione un usuario">
            <el-option
              v-for="item in datosUsuarios"
              :key="item.idusuario"
              :label="item.nombre + ' ' + item.apellido"
              :value="item.idusuario"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="Caducidad" :label-width="formLabelWidth">
          <el-date-picker
            v-model="formAgregar.fecha_caducidad"
            type="date"
            placeholder="Seleccione la fecha"
          />
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="msgAgregarVisible = false">Cancelar</el-button>
        <el-button type="primary" @click="agregarExpediente(); msgAgregarVisible = false">Agregar</el-button>
      </span>
    </el-dialog>

    <!-- Cuadro de dialogo para asignar abogado -->

    <el-dialog title="Asignar Usuario" :visible.sync="msgUsuarioVisible">
      <el-form :model="formUsuario">
        <el-form-item label="Expediente" :label-width="formLabelWidth">
          <input v-model="formUsuario.expediente" disabled>
        </el-form-item>
        <el-form-item label="Usuario" :label-width="formLabelWidth">
          <el-select v-model="formUsuario.usuario" placeholder="Seleccione un usuario">
            <el-option
              v-for="item in datosUsuarios"
              :key="item.idusuario"
              :label="item.nombre + ' ' + item.apellido"
              :value="item.idusuario"
            />
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button
          @click="
            msgUsuarioVisible = false;
          "
        >Cancelar</el-button>
        <el-button
          type="primary"
          @click="
            msgUsuarioVisible = false;
            asignarUsuario();
          "
        >Asignar</el-button>
      </span>
    </el-dialog>

    <!-- Dialogo que se aparece cuando se va a eliminar un expediente -->
    <el-dialog
      title="Advertencia"
      :visible.sync="deleteDialogVisible"
      width="35%"
      center
    >
      <center><span>¿Realmente desea eliminar el expediente <b>No. {{ delExpediente }}</b>?</span></center>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deleteDialogVisible = false">Cancelar</el-button>
        <el-button type="primary" @click="borrarExpediente">Confirmar</el-button>
      </span>
    </el-dialog>

    <!-- Boton para agregar nuevo expediente al aplicativo -->

    <el-button size="mini" type="primary" icon="el-icon-circle-plus" @click="clickAgregar(); msgAgregarVisible = true">Agregar expediente</el-button>

    <!-- Tabla donde se lista, ordena y realiza busqueda de los expedientes -->

    <el-table
      v-loading="loading"
      :data="datosProcesos.filter(data => !busquedaExpediente || data.expediente.toLowerCase().includes(busquedaExpediente.toLowerCase()))"
      style="width: 100%"
    >
      <el-table-column
        v-for="column in tableColumns"
        :key="column.label"
        :label="column.label"
        :prop="column.prop"
        align="center"
        sortable
      />
      <el-table-column
        prop="servicio"
        label="Servicio"
        align="center"
        sortable
        :filters="[{text:'Energía', value:'Energía'},{text:'Gas', value:'Gas'},{text:'GLP', value:'GLP'}]"
        :filter-method="filterHandler"
      />
      <el-table-column align="left">
        <template slot="header" slot-scope="scope">
          <el-input v-model="busquedaExpediente" size="mini" placeholder="No. Expediente" />
        </template>
        <template slot-scope="scope">
          <el-button style="border: 1px solid #409EFF;" size="mini" @click="handlePermisos(scope.row)"><b>Permisos</b></el-button>
          <el-button
            size="mini"
            type="danger"
            icon="el-icon-delete-solid"
            @click="handleDelete(scope.row)"
          />
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { CONSTANTS } from '@/constants/constants'
import { getListProcesos, createProceso, updateProcesoUsuario, deleteProceso } from '@/api/procesosDIEG/procesos'
import { getListUsuarios } from '@/api/procesosDIEG/usuarios'
import { getListServicios } from '@/api/procesosDIEG/servicios'
import { getListEmpresas } from '@/api/procesosDIEG/empresas'

export default {
  name: 'ViewProcesos',
  components: { },
  data() {
    return {
      /* Datos para mostrar en la tabla */
      tableColumns: CONSTANTS.tableColumns,
      datosProcesos: [],
      datosUsuarios: [],
      datosServicios: [],
      datosEmpresas: [],
      /* Datos para captar la creación */
      formAgregar: {
        radicado: '',
        empresa: '',
        servicio: '',
        usuario: '',
        fecha_caducidad: null
      },
      formUsuario: {
        usuario: '',
        expediente: ''
      },
      /* Aqui se guarda el valor escrito en el cuadro de texto para la busqueda */
      busquedaExpediente: '',
      /* Si es o no visible el fomulario de agregar */
      msgAgregarVisible: false,
      /* Si es o no visible el formulario de asginación de usuario */
      msgUsuarioVisible: false,
      /* Si es o no visible el cuadro de confirmación de eliminación */
      /* quitarVisible: false,*/
      /* Tamaño del formulario */
      formLabelWidth: '120px',
      deleteDialogVisible: false,
      delExpediente: '',
      delIdproceso: '',
      loading: true,
      disableEmpresas: true
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    this.initView()
  },
  methods: {
    async initView() {
      this.getProcesos()
      this.getUsuarios()
      this.getServicios()
    },
    async getProcesos() {
      await getListProcesos().then((response) => {
        console.log('Procesos -> ', response)
        this.datosProcesos = response
        this.loading = false
      })
    },
    async getUsuarios() {
      await getListUsuarios().then((response) => {
        console.log('Usuarios -> ', response)
        this.datosUsuarios = response
      })
    },
    async getServicios() {
      await getListServicios().then((response) => {
        console.log('Servicios -> ', response)
        this.datosServicios = response
      })
    },
    /* Metodo para realizar la busqueda de los filtro ubicado en las columnas */
    filterHandler(value, row, column) {
      const property = column['property']
      return row[property] === value
    },
    /* Evento click boton permisos */
    handlePermisos(data) {
      console.log(data)
      this.formUsuario.expediente = data.expediente
      this.formUsuario.usuario = data.idusuario
      this.msgUsuarioVisible = true
    },
    /* Evento clic boton permisos */
    handleDelete(data) {
      console.log(data.idproceso)
      this.delIdproceso = data.idproceso
      this.delExpediente = data.expediente
      this.deleteDialogVisible = true
    },
    async borrarExpediente() {
      this.loading = true
      console.log('Expediente a borrar -> ', this.delIdproceso)
      await deleteProceso(this.delIdproceso).then((response) => {
        console.log('RESPONSE PROCESO BORRADO -> ', response)
        this.getProcesos()
      })
      this.deleteDialogVisible = false
    },
    async asignarUsuario() {
      console.log(this.formUsuario)
      this.loading = true
      await updateProcesoUsuario(this.formUsuario).then((response) => {
        console.log('RESPONSE PROCESO ACTUALIZADO -> ', response)
        this.getProcesos()
      })
    },
    async selectServicio(idservicio) {
      console.log(idservicio)
      await getListEmpresas(idservicio).then((response) => {
        console.log('EMPRESAS -> ', response.items)
        this.datosEmpresas = response.items
        this.disableEmpresas = false
      })
    },
    clickAgregar() {
      this.formAgregar = {}
      this.disableEmpresas = true
    },
    async agregarExpediente() {
      console.log(this.formAgregar)
      this.loading = true
      await createProceso(this.formAgregar).then((response) => {
        console.log('RESPONSE PROCESO AGREGADO -> ', response)
        this.getProcesos()
      })
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
