<template>
  <div>
    <component :is="currentView" />
  </div>
</template>

<script>
	import viewProcesos from '../administrador/components/procesos'

	export default {
		name: 'menuUsuario',
		components: { viewProcesos },
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
			
			if (view == '/procesos') {
				this.currentView = 'viewProcesos'
			}
		}
	}
</script>