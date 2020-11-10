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
					<!-- <span style="font-size: 120%;"><b>{{ form.name }}</b></span> -->
        </aside>
      </el-col>

			<el-card class="box-card">
        <div slot="header" class="clearfix">
          <span><b>INFORMACIÓN COMERCIAL</b></span>
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
        <div style="margin-bottom:285px;">

					<el-col :span="24" style="border: 0px solid red; text-align: center; padding-top: 10px;">
						<el-row>
							<el-col :span="14" style="text-align:right;  padding-right: 2px;">
								<el-tooltip class="item" effect="dark" content="Factor de productividad acumulado." placement="left">							
									<i class="el-icon-info" style="color: #304156;"></i>
								</el-tooltip>
								<el-select v-model="value3" clearable placeholder="Factor de productividad" style="width: 18.5em;">
									<el-option
										v-for="item in optionsFactor"
										:key="item.value"
										:label="item.label"
										:value="item.value">
									</el-option>
								</el-select>
							</el-col>
							<el-col :span="10" style="text-align:left; padding-left: 3px;">
								<el-button type="primary" @click="dialogFormVisible = true" icon="el-icon-circle-plus-outline" style="width: 10em;">Agregar</el-button>
							</el-col>
							<!-- <el-dialog
								title="Agregar Factor de productividad"
								:visible.sync="dialogVisible"
								width="30%"
								:before-close="handleClose">
								<span>Ingrese un valor</span>
								<el-input
									type="number"
									placeholder="Factor de productividad"
									prefix-icon="el-icon-edit"
									v-model="inputDialog"
									style="width: 21em;">
								</el-input>
								<span slot="footer" class="dialog-footer">
									<el-button @click="dialogVisible = false">Cancelar</el-button>
									<el-button type="primary" @click="dialogVisible = false">Confirmar</el-button>
								</span>
							</el-dialog>	 -->

							<!-- Form -->
							<!-- <el-button type="text" @click="dialogFormVisible = true">open a Form nested Dialog</el-button> -->

							<el-dialog title="Agregar Factor de productividad" :before-close="handleClose" :visible.sync="dialogFormVisible">
								<el-form :model="form">
									<el-form-item>										
										<hr>
										<span>Ingrese un valor</span><br>
										<el-input
											type="number"
											placeholder="Factor de productividad"
											prefix-icon="el-icon-edit"
											v-model="form.name"
											style="width: 21em;">
										</el-input>
									</el-form-item>
								</el-form>
								<span slot="footer" class="dialog-footer">
									<el-button @click="dialogFormVisible = false">Cancelar</el-button>
									<el-button type="primary" @click="functionConfirmar">Confirmar</el-button>
								</span>
							</el-dialog>

						</el-row>
					</el-col>
					
					<el-col :span="24" style="border: 0px solid red; text-align: center; padding-top: 10px;">
						<el-row>
							<el-col :span="14" style="text-align:right;  padding-right: 2px;">
								<el-tooltip class="item" effect="dark" content="Prima de riesgo de cartera." placement="left">							
									<i class="el-icon-info" style="color: #304156;"></i>
								</el-tooltip>
								<el-input
									type="number"
									placeholder="RCNU"
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
								<el-tooltip class="item" effect="dark" content="Costo de la contribución liquidado al comercializador minorista." placement="left">							
									<i class="el-icon-info" style="color: #304156;"></i>
								</el-tooltip>
								<el-input
									type="number"
									placeholder="Contribución CREG"
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
								<el-tooltip class="item" effect="dark" content="Costo de la contribución liquidado al comercializador minorista." placement="left">							
									<i class="el-icon-info" style="color: #304156;"></i>
								</el-tooltip>
								<el-input
									type="number"
									placeholder="Contribución SSPD"
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
								<el-input
									type="number"
									placeholder="N° Resolución CREG"
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

					<el-col :span="24" style="border: 0px solid red; text-align: center; padding-top: 10px;">
						<el-row>
							<el-col :span="14" style="text-align:right;  padding-right: 2px;">
								<el-input
									type="number"
									placeholder="N° Radicado SSPD"
									prefix-icon="el-icon-edit"
									v-model="input5"
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
				dialogFormVisible: false,
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        formLabelWidth: '120px',
				dialogVisible: false,
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
				value3: '',
				inputDialog: '',
				input1: '',
				input2: '',
				input3: '',
				input4: '',
				input5: '',
				inputDialog: ''
			}
		},
		methods: {
      handleClose(done) {
        this.$confirm('¿Realmente deseas cerrar la ventana?')
          .then(_ => {
            done();
          })
          .catch(_ => {});
			},
			functionConfirmar(){
				// alert('hola function!');
				this.optionsFactor.push({
					value: this.form.name,
					label: this.form.name
				})
				this.dialogFormVisible = false
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