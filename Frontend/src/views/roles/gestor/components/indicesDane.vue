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
          <span><b>ÍNDICES DANE</b></span>
        </div>
        <div style="margin-bottom:140px;">
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
					</el-col>

					<el-col :span="24" style="border: 0px solid red; text-align: center; padding-top: 10px;">
						<el-row>
							<el-col :span="12" style="text-align:right;  padding-right: 2px;">
								<el-input
									type="number"
									placeholder="IPC"
									prefix-icon="el-icon-edit"
									v-model="input1"
									style="width: 16em;">
								</el-input>
							</el-col>
							<el-col :span="12" style="text-align:left; padding-left: 3px;">
								<el-button type="primary" icon="el-icon-refresh" style="width: 16em;">Modificar</el-button>
							</el-col>			
						</el-row>
					</el-col>

					<el-col :span="24" style="border: 0px solid red; text-align: center; padding-top: 10px;">
						<el-row>
							<el-col :span="12" style="text-align:right;  padding-right: 2px;">
								<el-input
									type="number"
									placeholder="IPP"
									prefix-icon="el-icon-edit"
									v-model="input2"
									style="width: 16em;">
								</el-input>
							</el-col>
							<el-col :span="12" style="text-align:left; padding-left: 3px;">
								<el-button type="primary" icon="el-icon-refresh" style="width: 16em;">Modificar</el-button>
							</el-col>			
						</el-row>
					</el-col>
        </div>
      </el-card>

			<el-col :span="24" style="border: 0px solid red; text-align: center; padding: 10px;">
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
		name: 'viewIndicesDane',
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
					value: '2007',
					label: '2007'
				}, {
					value: '2008',
					label: '2008'
				}, {
					value: '2009',
					label: '2009'
				}, {	
					value: '2010',
					label: '2010'
				}, {
					value: '2011',
					label: '2011'
				}, {
					value: '2012',
					label: '2012'
				}, {
					value: '2013',
					label: '2013'
				}, {
					value: '2014',
					label: '2014'
				}, {
					value: '2015',
					label: '2015'
				}, {
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
				input1: '',
				input2: '',
			}
		},
    computed: {
      ...mapGetters([
        'name',
        'roles'
      ])
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