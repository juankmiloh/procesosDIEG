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
          <span><b>INFORMACIÓN D097 | Resolución</b></span>
        </div>
        <div style="margin-bottom:40px;">
          <el-col :span="24" style="border: 0px solid red; text-align: center;">
						<el-select v-model="value1" clearable placeholder="Año">
							<el-option
								v-for="item in optionsAno"
								:key="item.value"
								:label="item.label"
								:value="item.value">
							</el-option>
						</el-select>
						<el-select v-model="value2" clearable placeholder="Empresa">
							<el-option
								v-for="item in optionsEmpresa"
								:key="item.value"
								:label="item.label"
								:value="item.value">
							</el-option>
						</el-select>			
					</el-col>
        </div>
      </el-card>

			<el-card class="box-card" style="margin-top:20px;">
        <div style="margin-bottom:200px;">

					<el-col :span="24" style="border: 0px solid red; text-align: center; padding-top: 10px;">
						<el-row>
							<el-col :span="14" style="text-align:right;  padding-right: 2px;">
								<el-tooltip class="item" effect="dark" content="Cargo Nivel de Tensión 1 por inversión." placement="left">							
									<i class="el-icon-info" style="color: #304156;"></i>
								</el-tooltip>
								<el-input
									type="number"
									placeholder="CDI"
									prefix-icon="el-icon-edit"
									v-model="input1"
									style="width: 21em;">
								</el-input>
							</el-col>
							<el-col :span="10" style="text-align:left; padding-left: 3px;">
								<el-button type="primary" icon="el-icon-refresh" style="width: 10em;">Modificar</el-button>
							</el-col>			
						</el-row>
					</el-col>

					<el-col :span="24" style="border: 0px solid red; text-align: center; padding-top: 10px;">
						<el-row>
							<el-col :span="14" style="text-align:right;  padding-right: 2px;">
								<el-tooltip class="item" effect="dark" content="Cargo Nivel de Tensión 1 por mantenimiento." placement="left">							
									<i class="el-icon-info" style="color: #304156;"></i>
								</el-tooltip>
								<el-input
									type="number"
									placeholder="CDM"
									prefix-icon="el-icon-edit"
									v-model="input2"
									style="width: 21em;">
								</el-input>
							</el-col>
							<el-col :span="10" style="text-align:left; padding-left: 3px;">
								<el-button type="primary" icon="el-icon-refresh" style="width: 10em;">Modificar</el-button>
							</el-col>			
						</el-row>
					</el-col>

					<el-col :span="24" style="border: 0px solid red; text-align: center; padding-top: 10px;">
						<el-row>
							<el-col :span="14" style="text-align:right;  padding-right: 2px;">
								<el-tooltip class="item" effect="dark" content="Cargo Nivel de Tensión 2." placement="left">							
									<i class="el-icon-info" style="color: #304156;"></i>
								</el-tooltip>
								<el-input
									type="number"
									placeholder="CD2"
									prefix-icon="el-icon-edit"
									v-model="input3"
									style="width: 21em;">
								</el-input>
							</el-col>
							<el-col :span="10" style="text-align:left; padding-left: 3px;">
								<el-button type="primary" icon="el-icon-refresh" style="width: 10em;">Modificar</el-button>
							</el-col>			
						</el-row>
					</el-col>

					<el-col :span="24" style="border: 0px solid red; text-align: center; padding-top: 10px;">
						<el-row>
							<el-col :span="14" style="text-align:right;  padding-right: 2px;">
								<el-tooltip class="item" effect="dark" content="Cargo Nivel de Tensión 3." placement="left">							
									<i class="el-icon-info" style="color: #304156;"></i>
								</el-tooltip>
								<el-input
									type="number"
									placeholder="CD3"
									prefix-icon="el-icon-edit"
									v-model="input4"
									style="width: 21em;">
								</el-input>
							</el-col>
							<el-col :span="10" style="text-align:left; padding-left: 3px;">
								<el-button type="primary" icon="el-icon-refresh" style="width: 10em;">Modificar</el-button>
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
		name: 'viewInfoComercial',
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
				optionsEmpresa: [{
					value: '2103',
					label: 'CODENSA SA'
				}, {
					value: '2249',
					label: 'ELECTRIFICADORA DEL CARIBE SA'
				}, {
					value: '204',
					label: 'ELECTRIFICADORA DEL META SA'
				}],
				optionsFactor: [{
					value: '0',
					label: '0'
				}, {
					value: '0.00725',
					label: '0.00725'
				}, {
					value: '0.0145',
					label: '0.0145'
				},{
					value: '0.02175',
					label: '0.02175'
				},{
					value: '0.029',
					label: '0.029'
				}],
				value1: '',
				value2: '',
				input1: '',
				input2: '',
				input3: '',
				input4: '',
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

</style>