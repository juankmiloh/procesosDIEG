<template>
  <div class="components-container">

    <!-- Cuadro de dialogo para agregar expediente -->

    <el-dialog title="Agregar Expediente" :visible.sync="msgAgregarVisible">
      <el-form :model="formAgregar">
        <el-form-item label="Expediente" :label-width="formLabelWidth">
          <el-input v-model="formAgregar.expediente" 
          autocomplete="off"
          placeholder="Ingrese el número del expediente"></el-input>
        </el-form-item>
        <el-form-item label="Servicio" :label-width="formLabelWidth">
          <el-select v-model="formAgregar.servicio" placeholder="Seleccione el servicio">
            <el-option label="Energia" value="energia"></el-option>
            <el-option label="Gas" value="gas"></el-option>
            <el-option label="GLP (Gas Licuado de Petroleo)" value="glp"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Empresa" :label-width="formLabelWidth">
          <el-select v-model="formAgregar.empresa" placeholder="Seleccione una empresa">
            <el-option label="Empresa 1" value="Empresa 1"></el-option>
            <el-option label="Empresa 2" value="Empresa 2"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Usuario" :label-width="formLabelWidth">
          <el-select v-model="formAgregar.usuario" placeholder="Seleccione un usuario">
            <el-option label="Usuario 1" value="Usuario 1"></el-option>
            <el-option label="Usuario 2" value="Usuario 2"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="msgAgregarVisible = false">Cancelar</el-button>
        <el-button type="primary" @click="msgAgregarVisible = false">Agregar</el-button>
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
            <el-option label="Usuario 1" value="Usuario 1"></el-option>
            <el-option label="Usuario 2" value="Usuario 2"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button 
        @click="msgUsuarioVisible = false; 
        this.formUsuario.expediente = ''">Cancelar</el-button>
        <el-button type="primary" 
        @click="msgUsuarioVisible = false; 
        this.formUsuario.expediente = ''">Agregar</el-button>
      </span>
    </el-dialog>
    
    <!-- Boton para agregar nuevo expediente al aplicativo -->

    <el-button size="mini" @click="msgAgregarVisible = true">Agregar</el-button>

    <!-- Tabla donde se lista, ordena y realiza busqueda de los expedientes -->

    <el-table
      ref="procesos"
      :data="datosProcesos.filter(data => !busquedaExpediente || data.expediente.toLowerCase().includes(busquedaExpediente.toLowerCase()))"
      style="width:100%">
      <!-- Columna de expediente -->
      <el-table-column
        prop="expediente"
        label="Expediente"
        sortable
        column-key="expediente">
        <template slot="header">
          <span style="aling=center;"> Expediente </span>
          <!-- Caja de texto para busqueda por expediente -->
          <el-input
            v-model="busquedaExpediente"
            size="mini"
            placeholder="# Expediente"/>
        </template>       
      </el-table-column>
      <!-- Columna de caducidad -->
      <el-table-column
        prop="caducidad"
        label="Caducidad"
        sortable
        column-key="caducidad">
      </el-table-column>
      <!-- Columna de empresa -->
      <el-table-column
        prop="empresa"
        label="Empresa"
        sortable
        column-key="empresa"
        :filters="[{text:'Empresa 1', value:'Empresa 1'},{text:'Empresa 2', value:'Empresa 2'}]"
        :filter-method="filterHandler">
      </el-table-column>
      <!-- Columna de estado -->
      <el-table-column
        prop="estado"
        label="Estado"
        sortable=""
        column-key="estado"
        :filters="[{text:'Estado 1', value:'Estado 1'},{text:'Estado 2', value:'Estado 2'}]"
        :filter-method="filterHandler">
      </el-table-column>
      <!-- Columna de servicio -->
      <el-table-column
        prop="servicio"
        label="Servicio"
        sortable=""
        column-key="servicio"
        :filters="[{text:'Energia', value:'Energia'},
                  {text:'Gas', value:'Gas'},
                  {text:'GLP (Gas licuado de petroleo)', value:'GLP'}]"
        :filter-method="filterHandler">
      </el-table-column>
      <!-- Columna donde se ponen los botones de permisos y quitar -->
      <el-table-column>
        <template slot-scope="scope">
          <!-- Boton de permisos -->
          <el-button
            size="mini"
            @click="handleClicPermisos(scope.row.expediente)">Permisos</el-button>
          <!-- Boton de eliminar -->
          <el-button
            size="mini"
            type="danger"
            @click="handleClicEliminar(scope.row.expediente)">Quitar</el-button>
        </template> 
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  import BackToTop from '@/components/BackToTop'

  export default {
		name: 'viewProcesos',
		components: { BackToTop, Element },
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
        /* Datos para mostrar en la tabla */
				datosProcesos: [{
          empresa: 'Empresa 1',
          expediente: '20091010101010',
          estado: 'Estado 1',
          servicio: 'Energia',
          caducidad: '2020-12-20'
        },
        {
          empresa: 'Empresa 2',
          expediente: '20091010101011',
          estado: 'Estado 2',
          servicio: 'GLP',
          caducidad: '2020-12-20'
        },
        {
          empresa: 'Empresa 1',
          expediente: '20091010101012',
          estado: 'Estado 1',
          servicio: 'Energia',
          caducidad: '2020-12-20'
        },
        {
          empresa: 'Empresa 2',
          expediente: '20091010101013',
          estado: 'Estado 1',
          servicio: 'Gas',
          caducidad: '2020-12-20'
        },
        {
          empresa: 'Empresa 1',
          expediente: '20091010101014',
          estado: 'Estado 1',
          servicio: 'Energia',
          caducidad: '2020-12-20'
        },
        {
          empresa: 'Empresa 1',
          expediente: '20091010101015',
          estado: 'Estado 2',
          servicio: 'GAS',
          caducidad: '2020-12-20'
        },
        {
          empresa: 'Empresa 1',
          expediente: '20091010101016',
          estado: 'Estado 2',
          servicio: 'Energia',
          caducidad: '2020-12-20'
        }],
        /* Datos para captar la creación */
        formAgregar: {
          expediente: '',
          empresa: '',
          servicio: '',
          usuario: ''
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
        /*quitarVisible: false,*/
        /* Tamaño del formulario */
        formLabelWidth: '120px'
			}
		},
    computed: {
      ...mapGetters([
        'name',
        'roles'
      ])
    },
    methods: {
      /* Metodo para realizar la busqueda de los filtro ubicado en las columnas */
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
      /* Evento click boton permisos */
      handleClicPermisos(expediente){
        this.formUsuario.expediente = expediente;
        this.msgUsuarioVisible = true;
      },
      /* Evento clic boton permisos */
      handleClicEliminar(expediente){
        
      }

    },
		created() {

		}
	}
</script>

<style lang="scss" scoped>
	.placeholder-container div {
		margin: 10px;
	}
</style>