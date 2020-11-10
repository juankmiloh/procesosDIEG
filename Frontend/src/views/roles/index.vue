<template>
  <div>
    <component :is="currentRole" />
  </div>
</template>

<script>
	import { mapGetters } from 'vuex'
	import viewAdminsitrador from './administrador'
/* 	import viewUsuario from './usuario' */

	export default {
		name: 'menuRoles',
		components: { viewAdministrador, viewUsuario },
		data() {
			return {
				// currentRole: 'adminDashboard'
				// currentRole: 'defaultDashboard'
			}
		},
		computed: {
			...mapGetters([
				'roles' //obtiene el rol logueado
			])
		},
		created() {
			// console.log(this.roles)
			if (this.roles.includes('administrador')) {
				this.currentRole = 'viewAdministrador'
			}
/* 			if (this.roles.includes('usuario')) {
				this.currentRole = 'viewUsuario'
			} */
		}
	}
</script>
