<template>
  <div>
    <sticky class-name="sub-navbar">
      <div style="border: 0px solid red; color: white; text-align: center;">
        <h2 v-if="editarEtapa">Editar etapa</h2>
        <h2 v-else>Agregar etapa</h2>
      </div>
    </sticky>

    <div class="createPost-container" style="padding-top: 25px; padding-bottom: 20px;">
      <el-form
        ref="formAgregar"
        :model="formAgregar"
        :rules="rulesFormEtapa"
        label-width="120px"
        class="demo-ruleForm"
      >
        <el-form-item label="Etapa" prop="etapa">
          <el-select
            v-model="formAgregar.etapa"
            filterable
            placeholder="Seleccione una etapa"
            class="control-modal-agregar"
            :disabled="editarEtapa"
            @change="selectEtapa($event)"
          >
            <el-option
              v-for="item in datosEtapa"
              :key="item.idetapa"
              :label="item.nombre"
              :value="item.idetapa"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="Radicado" prop="radicadoEtapa">
          <el-input
            v-model="formAgregar.radicadoEtapa"
            autocomplete="off"
            placeholder="Ingrese No. del radicado"
            maxlength="14"
            show-word-limit
            clearable
            class="control-modal-agregar"
          />
        </el-form-item>

        <el-form-item label="Fecha inicio" prop="fechaInicioEtapa">
          <el-date-picker
            v-model="formAgregar.fechaInicioEtapa"
            type="datetime"
            placeholder="Seleccione fecha inicio"
            class="control-modal-agregar"
          />
        </el-form-item>

        <el-form-item label="Fecha fin" prop="fechaFinEtapa">
          <el-date-picker
            v-model="formAgregar.fechaFinEtapa"
            type="datetime"
            placeholder="Seleccione fecha fin"
            class="control-modal-agregar"
          />
        </el-form-item>

        <el-form-item label="Observación" prop="observacionEtapa">
          <el-input
            v-model="formAgregar.observacionEtapa"
            type="textarea"
            class="control-modal-agregar"
            rows="7"
          />
        </el-form-item>

        <el-form-item>
          <el-button
            @click="closeModalAgregar();"
          >Cancelar</el-button>
          <el-button
            type="success"
            @click="handleEtapa();"
          >{{ textEditarEtapa }}</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Sticky from '@/components/Sticky' // 粘性header组件
import { CONSTANTS } from '@/constants/constants'
import { createEtapa } from '@/api/procesosDIEG/etapas'
// import { deleteEtapa } from '@/api/procesosDIEG/etapas'
import { updateEtapa } from '@/api/procesosDIEG/etapas'

export default {
  name: 'AgregarEtapas',
  components: { Sticky },
  props: {
    editar: {
      type: Boolean,
      default: false
    },
    id: {
      type: String,
      default: ''
    },
    editarEtapa: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      formAgregar: CONSTANTS.formAgregarEtapa,
      textEditarEtapa: 'Agregar',
      rulesFormEtapa: CONSTANTS.rulesFormEtapa,
      datosEtapa: []
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'idusuario', 'dependencia'])
  },
  created() {},
  methods: {
    async handleEtapa() {
      if (!this.editarEtapa) { // Condicion para AGREGAR una etapa (No es modo editar etapa)
        const modelAgregarEtapa = this.formAgregar
        this.$refs['formAgregar'].validate(async(valid) => {
          if (valid) {
            this.loadingEtapa = true
            modelAgregarEtapa.idproceso = this.formProceso.idproceso
            // modelAgregarEtapa.radicadoEtapa = `P${this.formProceso.idproceso}${this.estampillaEtapa}`
            if (!modelAgregarEtapa.hasOwnProperty('fechaFinEtapa')) {
              // console.log('esta vacio fecha fin!')
              modelAgregarEtapa.fechaFinEtapa = null
            }
            if (!modelAgregarEtapa.hasOwnProperty('observacionEtapa')) {
              // console.log('esta vacio observacion!')
              modelAgregarEtapa.observacionEtapa = ''
            }
            // this.msgAgregarEtapaVisible = false
            this.loading = true
            this.datosEtapa = []
            // console.log('FORMAGREGAR -> ', modelAgregarEtapa)
            await createEtapa(modelAgregarEtapa).then(async(response) => {
              // console.log('RESPONSE AGREGAR -> ', response)
              this.$notify({
                title: 'Buen trabajo!',
                message: 'Etapa agregada con éxito',
                type: 'success',
                duration: 2000
              })
              await this.getEtapasProceso(this.formProceso.idproceso)
              await this.getEtapas()
              this.fetchData(this.formProceso.idproceso)
              this.loading = false
              this.loadingEtapa = false
            })
          } else {
            console.log('error submit!!')
            return false
          }
        })
      } else { // Condicion para EDITAR una etapa (modo editar etapa)
        const modelEditarEtapa = this.formAgregar
        this.$refs['formAgregar'].validate(async(valid) => {
          if (valid) {
            this.loadingEtapa = true
            this.loading = true
            this.datosEtapa = []
            delete modelEditarEtapa['etapa']
            modelEditarEtapa.idproceso = this.formProceso.idproceso
            console.log('FORMEDITAR -> ', modelEditarEtapa)
            await updateEtapa(modelEditarEtapa).then(async(response) => {
              // console.log('RESPONSE AGREGAR -> ', response)
              this.$notify({
                title: 'Buen trabajo!',
                message: 'Etapa modificada con éxito',
                type: 'success',
                duration: 2000
              })
              // this.msgAgregarEtapaVisible = false
              await this.getEtapasProceso(this.formProceso.idproceso)
              await this.getEtapas()
              this.fetchData(this.formProceso.idproceso)
              this.loading = false
              this.loadingEtapa = false
            })
          } else {
            console.log('error submit!!')
            return false
          }
        })
      }
    },
    closeModalAgregar() {
      this.formAgregar = CONSTANTS.formAgregarEtapa
      if (this.$refs['formAgregar']) {
        this.$refs['formAgregar'].resetFields()
      }
      this.msgAgregarEtapaVisible = false
      this.loadingEtapa = false
      // console.log('closeModalAgregar -> ', this.$refs['formAgregar'])
    }
  }
}
</script>

<style lang="scss" scoped>
  .control-modal-agregar {
    width: 28em;
  }
</style>
