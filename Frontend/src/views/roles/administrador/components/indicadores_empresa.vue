<template>
  <div class="components-container">

		<div class="block">
			<span class="demonstration">Seleccione el rango de fechas </span>
			<el-date-picker
				v-model="rangoFechas"
				type="daterange"
				range-separator="a"
				start-placeholder="Fecha inicio"
				end-placeholder="Fecha fin"
				@input="cambiarEmpresas()">
			</el-date-picker>
		</div>

		<br>
		
    <pie-chart
      :data="empresas"
      value-title="Empresas y procesos que han sido terminados"
			v-model="chartGraficoEmpresaFinalizados"
    />

		<br>
		
    <pie-chart
      :data="empresas"
      value-title="Empresas y procesos que han sido activos"
			v-model="chartGraficoEmpresaActivos"
    />

		<br>
		
		<div id="seleccionEmpresa" style="display:none">
			<span class="demonstration">Seleccione la empresa de la cual quiere obtener gráficos </span>
			<el-select 
				v-model="empresa" 
				placeholder="Select" 
				@input="cambiarEmpresa()">
				<el-option
					v-for="item in empresas"
					:key="item.names"
					:label="item.names"
					:value="item.names">
				</el-option>
			</el-select>

		</div>

		<br>

		<div id="tablaCausalesEmpresa" style="display:none">

			<pie-chart
				:data="empresa"
				value-title="Causa de los procesos finalizados de la empresa seleccionada"
				v-model="chartGraficoFiltroFinalizados"
			/>

			<br>

			<pie-chart
				:data="empresa"
				value-title="Causa de los procesos activos de la empresa seleccionada"
				v-model="chartGraficoFiltroActivos"
			/>

			<br>
			
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
	import PieChart from './graph/PieChart'
	import BackToTop from '@/components/BackToTop'

  export default {
		name: 'viewIndicadoresEmpresa',
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
				empresas: [],
				empresa: [],
				rangoFechas: '',
				empresa: ''
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
			cambiarEmpresas(){
				this.empresas = 					
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
				document.getElementById('seleccionEmpresa').style.display = null
			},
			cambiarEmpresa(){
				this.empresa =
				[
					{
						names: 'Causa 1',
						values: 40
					},
					{
						names: 'Causa 2',
						values: 30
					},
					{
						names: 'Causa 3',
						values: 30
					}
				],
				document.getElementById('tablaCausalesEmpresa').style.display = null
			}
    }
	}
</script>

<style lang="scss" scoped>
	.placeholder-container div {
		margin: 10px;
	}
</style>