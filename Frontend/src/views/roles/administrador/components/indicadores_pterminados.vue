<template>
  <div class="components-container">

		<pie-chart
			:data="empresa"
			value-title="Cantidad de procesos terminados por empresa"
			v-model="chartGraficoFiltroFinalizados"
		/>

		<br>

		<pie-chart
			:data="empresa"
			value-title="Cantidad de procesos terminados por empresa"
			v-model="chartGraficoFiltroFinalizados"
		/>

		<br>

		<div id="tablaEmpresa" style="display:none">

			<el-table
					ref="causalesEmpresa"
					:data="empresa"
					style="width:100%">

				<el-table-column
					prop="names"
					label="Causas"
					sortable
					column-key="names">
				</el-table-column>

				<el-table-column
					prop="values"
					label="Número de expedientes"
					sortable
					column-key="values">
				</el-table-column>

			</el-table>

		</div>


  </div>
</template>
<script>
	import { mapGetters } from 'vuex'
	import BackToTop from '@/components/BackToTop'
	import PieChart from './graph/PieChart'

  export default {
		name: 'viewEmpresas',
		components: { BackToTop, PieChart },
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
				empresa: []
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
		mounted() {
			this.empresa = 					
			[
				{
					names: 'Empresa 1',
					values: '70'
				},
				{
					names: 'Empresa 2',
					values: '20'
				},
				{
					names: 'Empresa 3',
					values: '10'
				}
			],
			document.getElementById('tablaEmpresa').style.display = null
		}
	}
</script>

<style lang="scss" scoped>
	.placeholder-container div {
		margin: 10px;
	}
</style>