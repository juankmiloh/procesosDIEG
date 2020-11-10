<template>
  <div class="components-container">



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