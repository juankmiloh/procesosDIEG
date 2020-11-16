<template>
  <div>
    <component :is="currentView" />
  </div>
</template>

<script>
// ///////////////////////////////////////////////////////////////////////////////////////
/* Listado de importaciones de componentes */
// ///////////////////////////////////////////////////////////////////////////////////////
import viewProcesos from './components/procesos'
import viewEmpresas from './components/reporte_empresa'
import viewProceso from './components/visualizar_proceso'
import viewIndicadoresEmpresa from './components/indicadores_empresa'
import viewIndicadoresProcesosActivos from './components/indicadores_pactivos'
import viewIndicadoresProcesosTerminados from './components/indicadores_pterminados'

export default {
  name: 'MenuAdministrador',
  // ///////////////////////////////////////////////////////////////////////////////////////
  /* Listado del nombre de los componentes importados */
  // ///////////////////////////////////////////////////////////////////////////////////////
  components: {
    viewProcesos,
    viewEmpresas,
    viewProceso,
    viewIndicadoresEmpresa,
    viewIndicadoresProcesosActivos,
    viewIndicadoresProcesosTerminados
  },
  data() {
    return {
      // currentView: 'defaultDashboard'
    }
  },
  created() {
    const route = this.$route // obtenemos los parametros de la URL
    const tempRoute = Object.assign({}, route) // creamos un objeto de la URL
    const view = tempRoute.fullPath // obtenemos la URL de la vista
    console.log(view)
    // ///////////////////////////////////////////////////////////////////////////////////////
    /* Cargamos cada uno de los componentes con la ruta propuesta */
    // ///////////////////////////////////////////////////////////////////////////////////////
    if (view === '/procesos/expedientes') {
      this.currentView = 'viewProcesos'
    } else if (view === '/administrador/reporte_empresa') {
      this.currentView = 'viewEmpresas'
    } else if (view === '/administrador/proceso') {
      this.currentView = 'viewProceso'
    } else if (view === '/administrador/indicadores_empresa') {
      this.currentView = 'viewIndicadoresEmpresa'
    } else if (view === '/administrador/indicadores_pactivos') {
      this.currentView = 'viewIndicadoresProcesosActivos'
    } else if (view === '/administrador/indicadores_pterminados') {
      this.currentView = 'viewIndicadoresProcesosTerminados'
    }
  }
}
</script>
