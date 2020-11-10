<template>
  <div class="components-container">
    <el-row>
      <el-col :span="24" style="border: 0px solid red; text-align: center;">
        <aside>
          <span style="color: black; font-size: 170%;"><b>DIRECCIÓN TÉCNICA DE GESTIÓN DE ENERGÍA</b></span>
        </aside>
      </el-col>
			<el-col :span="24" style="border: 0px solid red; text-align: center;">          
        <aside>
          <span style="font-size: 120%;"><b>{{ name }}</b></span>
        </aside>
      </el-col>

			<el-card class="box-card">
        <div slot="header" class="clearfix">
          <span><b>NIVEL DE TOLERANCIA</b></span>
        </div>
        <div style="margin-bottom:50px;">
          <el-col :span="24" style="border: 0px solid red; text-align: center;">
						<el-select v-model="value1" clearable placeholder="Año">
							<el-option
								v-for="item in optionsAno"
								:key="item.value"
								:label="item.label"
								:value="item.value">
							</el-option>
						</el-select>
						<el-select v-model="value2" clearable placeholder="Mes">
							<el-option
								v-for="item in optionsMes"
								:key="item.value"
								:label="item.label"
								:value="item.value">
							</el-option>
						</el-select>
						<el-input-number v-model="num" :precision="2" @change="handleChange" :step="0.1" :min="0" :max="10" placeholder="Tolerancia"></el-input-number>
						<el-button type="primary" icon="el-icon-refresh">Modificar</el-button>
					</el-col>
        </div>
      </el-card>

			<el-col :span="24" style="border: 0px solid red; text-align: center; padding: 10px;">
				<!-- <el-button icon="el-icon-check" style="background-color: #42b983">Cargar</el-button> -->
				<el-button type="success" icon="el-icon-check" :loading="false" round>Cargar</el-button>
			</el-col>
    </el-row>

    <!-- you can add element-ui's tooltip -->
    <el-tooltip placement="top" content="subir">
      <back-to-top :custom-style="myBackToTopStyle" :visibility-height="300" :back-position="50" transition-name="fade" />
    </el-tooltip>
  </div>
</template>

<script>
	import { mapGetters } from 'vuex'
	import BackToTop from '@/components/BackToTop'

  export default {
		name: 'viewTolerancia',
		components: { BackToTop },
		data() {
			return {
				myBackToTopStyle: {
					right: '50px',
					bottom: '50px',
					width: '40px',
					height: '40px',
					'border-radius': '4px',
					'line-height': '45px',
					background: '#e7eaf1'
				},
				optionsAno: [{
					value: '2016',
					label: '2016'
				}, {
					value: '2017',
					label: '2017'
				}, {
					value: '2018',
					label: '2018'
				}, {
					value: '2019',
					label: '2019'
				}],
				optionsMes: [{
					value: '1',
					label: 'Enero'
				}, {
					value: '2',
					label: 'Febrero'
				}, {
					value: '3',
					label: 'Marzo'
				}, {
					value: '4',
					label: 'Abril'
				}, {
					value: '5',
					label: 'Mayo'
				}, {
					value: '6',
					label: 'Junio'
				}, {
					value: '7',
					label: 'Julio'
				}, {
					value: '8',
					label: 'Agosto'
				}, {
					value: '9',
					label: 'Septiembre'
				}, {
					value: '10',
					label: 'Octubre'
				}, {
					value: '11',
					label: 'Noviembre'
				}, {
					value: '12',
					label: 'Diciembre'
				}],
				value1: '',
				value2: '',
				num: ''
			}
		},
    computed: {
      ...mapGetters([
        'name',
        'roles'
      ])
    },
    methods: {
      handleChange(value) {
        console.log(value);
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