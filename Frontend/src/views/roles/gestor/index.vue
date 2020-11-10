<template>
  <div>
    <component :is="currentView" />
  </div>
</template>

<script>
	import viewTolerancia from './components/tolerancia'
	import viewIndicesDane from './components/indicesDane'
	import viewInfoComercial from './components/infoComercial'
	import viewResolucion from './components/infoD097/resolucion'
	import viewError from './components/infoD097/error'
	import viewPerdidas from './components/perdidasSTN'

	export default {
		name: 'menuGestor',
		components: { viewTolerancia, viewIndicesDane, viewInfoComercial, viewResolucion, viewError, viewPerdidas },
		data() {
			return {
				// currentView: 'defaultDashboard'
			}
		},
		created() {
			let route = this.$route // obtenemos los parametros de la URL
			let tempRoute = Object.assign({}, route) // creamos un objeto de la URL
			let view = tempRoute.fullPath // obtenemos la URL de la vista
			// console.log(view)
			
			if (view == '/tolerancia/nivel-tolerancia') {
				this.currentView = 'viewTolerancia'
			}
			else if (view == '/indices/indices-dane') {
				this.currentView = 'viewIndicesDane'
			}
			else if (view == '/comercial/Info-comercial') {
				this.currentView = 'viewInfoComercial'
			}
			else if (view == '/D097/modificar/resolucion') {
				this.currentView = 'viewResolucion'
			}
			else if (view == '/D097/modificar/error') {
				this.currentView = 'viewError'
			}
			else if (view == '/perdidas/perdidas-stn') {
				this.currentView = 'viewPerdidas'
			}
		}
	}
</script>