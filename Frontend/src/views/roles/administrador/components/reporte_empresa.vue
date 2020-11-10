<template>
  <div class="components-container">

    <!-- Cuadro de dialogo de los expedientes -->

    <el-dialog title="Expedientes de la empresa" :visible.sync="msgVisualizarExpedientes">

      Empresa: {{datosEmpresas[index].nombre}}
      <br>
      Servicio: {{datosEmpresas[index].servicio}}
      <br>
      <el-table
        ref="procesos"
        :data="datosEmpresas[index].Procesos"
        style="width:100%">

        <!-- Columna de expediente -->
        <el-table-column
          prop="expediente"
          label="Expediente"
          sortable
          column-key="expediente">     
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

        <!-- Columna de caducidad -->
        <el-table-column
          prop="caducidad"
          label="Caducidad"
          sortable
          column-key="caducidad">
        </el-table-column>
      </el-table>
    
      <span slot="footer" class="dialog-footer">
        <el-button 
        @click="msgVisualizarExpedientes = false">Salir</el-button>
      </span>

    </el-dialog>

    <!-- Tabla de la empresas -->

    <el-table
      ref="empresas"
      :data=datosEmpresas
      style="width:100%">

      <el-table-column
        prop="nombre"
        label="Empresa"
        sortable
        column-key="nombre"
        :filters="[{text:'Empresa 1', value:'Empresa 1'},{text:'Empresa 2', value:'Empresa 2'}]"
        :filter-method="filterHandler">
      </el-table-column>

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

      <el-table-column
        prop="Procesos.length"
        label="# Procesos"
        sortable
        column-key="cantidadProcesos">
      </el-table-column>

      <el-table-column>
        <template slot-scope="scope">
          <!-- Boton para visualizar los expedientes -->
          <el-button
            size="mini"
            @click="msgVisualizarExpedientes = true;
            index = scope.$index;">Expedientes</el-button>
        </template> 
      </el-table-column>

    </el-table>

  </div>
</template>
<script>
	import { mapGetters } from 'vuex'
	import BackToTop from '@/components/BackToTop'

  export default {
		name: 'viewEmpresas',
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
        /* Datos de las empresas y sus respectivos */
        datosEmpresas: [{
          nombre: 'Empresa 1',
          servicio: 'Energia',
          Procesos: [	{
            expediente: '20091010101010',
            estado: 'Estado 1',
            caducidad: '2020-12-20'
          },
          {
            expediente: '20091010101012',
            estado: 'Estado 1',
            caducidad: '2020-12-20'
          },
          {
            expediente: '20091010101014',
            estado: 'Estado 1',
            caducidad: '2020-12-20'
          },
          {
            expediente: '20091010101016',
            estado: 'Estado 2',
            caducidad: '2020-12-20'
          }]
        },
        {
          nombre: 'Empresa 2',
          servicio: 'GLP',
          Procesos: [{
            empresa: 'Empresa 2',
            expediente: '20091010101011',
            estado: 'Estado 2',
            servicio: 'GLP',
            caducidad: '2020-12-20'
          }]
        },
        {
          nombre: 'Empresa 2',
          servicio: 'Gas',
          Procesos: [{
            expediente: '20091010101013',
            estado: 'Estado 1',
            caducidad: '2020-12-20'
          }]            
        },
        {
          nombre: 'Empresa 1',
          servicio: 'Gas',
          Procesos: [{
            expediente: '20091010101015',
            estado: 'Estado 2',
            caducidad: '2020-12-20'
          }]
        }],
        /* Si es o no visible el cuadro de dialogo de expedientes */
        msgVisualizarExpedientes: false,
        /* Guarda la posición de la empresa y servicio seleccionado */
        index:'0'
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