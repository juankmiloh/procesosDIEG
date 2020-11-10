<template>
  <div class="dashboard-container">
    <component :is="currentView" />
  </div>
</template>

<script>
import viewCostoUnitario from './components/costoUnitario'
import viewd097 from './components/d097'
import viewd015 from './components/d015'
import viewTarifas from './components/tarifas'
import viewSensibilidad from './components/sensibilidad'
import viewHistorico from './components/historico'
import viewReportes from './components/reportes'

export default {
  name: 'menuRevisor',
  components: { viewCostoUnitario, viewd097, viewd015, viewTarifas, viewSensibilidad, viewHistorico, viewReportes },
	data() {
		return {
			// currentView: 'defaultDashboard'
		}
	},
	created() {
		let route = this.$route //obtenemos los parametros de la URL
		let tempRoute = Object.assign({}, route) //creamos un objeto de la URL
		let view = tempRoute.fullPath //obtenemos la URL de la vista
		console.log(view)
		
		if (view == '/verificacion/costo-unitario') {
			this.currentView = 'viewCostoUnitario'
		}
		else if (view == '/verificacion/componentes/d097') {
			this.currentView = 'viewd097'
		}
		else if (view == '/verificacion/componentes/d015') {
			this.currentView = 'viewd015'
		}
		else if (view == '/verificar-tarifas/tarifas') {
			this.currentView = 'viewTarifas'
		}
		else if (view == '/analisis-sensibilidad/sensibilidad') {
			this.currentView = 'viewSensibilidad'
		}
		else if (view == '/historico-verificaciones/verificaciones') {
			this.currentView = 'viewHistorico'
		}
		else if (view == '/reportes-revisor/reportes') {
			this.currentView = 'viewReportes'
		}
	}
}
</script>