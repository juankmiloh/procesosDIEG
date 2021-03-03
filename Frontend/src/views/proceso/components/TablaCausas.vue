<template>
  <el-col :md="24" style="border: 0px solid blue; padding-top: 0px;" class="div-causas">
    <el-card class="box-card div-causas-header" style="height: 64vh;">
      <div slot="header" class="clearfix">
        <!-- <el-row :style="countCausal ? '' : 'padding-top: 9px; padding-bottom: 4px;'"> -->
        <el-row>
          <el-col :md="countCausal > 0 ? 17 : 20">
            <span>Causales del proceso</span>
            <!-- (<count-to :start-val="0" :end-val="countCausal" :duration="5000" class="card-panel-num" />) -->
          </el-col>
          <el-col :md="countCausal > 0 ? 5 : 4">
            <el-switch v-model="valSwitch" active-color="#13ce66" :disabled="switchDisable || !abogadoEditar" />
          </el-col>
          <el-col v-show="countCausal > 0" :md="countCausal > 0 ? 2 : 0">
            <div class="badge-causal">
              <el-badge :value="countCausal" class="item" type="success">
                <el-link icon="el-icon-star-on" :underline="false" @click="dialogDrawer=true" />
              </el-badge>
            </div>
          </el-col>
        </el-row>
      </div>
      <el-row>
        <el-col v-loading="loading" :span="24">
          <el-card shadow="never" style="height: 5vh; border: 1px solid #F2F6FC; height: 52vh;" class="card-causas">
            <div v-if="datosCausal.length === 0" style="border: 0px solid; height: 43vh; text-align: center; display: flex; align-items: center; padding-left: 28%;">
              <span style="color: #C0C4CC; font-size: small;"><b>Proceso no registra causas</b></span>
            </div>
            <transition name="el-fade-in-linear">
              <div v-show="datosCausal.length" class="card-causa">
                <el-card v-for="item in datosCausal" :key="item.idcausal" shadow="never" style="height: 5vh; margin-bottom: 2%;">
                  <span style="color: #606266; font-size: small;">■ {{ item.nombrecausal }}</span>
                </el-card>
              </div>
            </transition>
          </el-card>
        </el-col>
      </el-row>
    </el-card>

    <!-- Cuadro de dialogo para agregar / editar causal -->

    <el-dialog
      v-el-drag-dialog
      :visible.sync="openModalCausal"
      :before-close="closeModalCausal"
      width="34em"
      custom-class="dialog-class-lista"
      :show-close="false"
    >
      <sticky class-name="sub-navbar">
        <div style="border: 0px solid red; color: white; text-align: center">
          <h2>{{ textActionCausal }} causal</h2>
        </div>
      </sticky>
      <div
        class="createPost-container"
        style="padding-top: 35px; padding-bottom: 20px; padding-left: 13px"
      >
        <el-form
          ref="formCausal"
          :model="formCausal"
          :rules="rulesFormCausal"
          label-width="120px"
          class="demo-ruleForm"
        >
          <el-form-item label="Causa" prop="idcausal">
            <el-select
              v-model="formCausal.idcausal"
              :disabled="!abogadoEditar || textActionCausal === 'Editar'"
              filterable
              placeholder="Seleccione una causal"
              class="control-modal"
              size="medium"
            >
              <el-option
                v-for="item in listaCausal"
                :key="item.idcausal"
                :label="item.nombre"
                :value="item.idcausal"
              />
            </el-select>
          </el-form-item>

          <el-form-item label="Fecha hechos" prop="f_hechos">
            <el-date-picker
              v-model="formCausal.f_hechos"
              :disabled="!abogadoEditar"
              type="date"
              placeholder="Seleccione una fecha"
              class="control-modal"
            />
          </el-form-item>

          <el-form-item label="Descripción">
            <el-input
              v-model="formCausal.descripcion"
              :disabled="!abogadoEditar"
              type="textarea"
              class="control-modal"
              rows="5"
            />
          </el-form-item>
          <el-form-item>
            <el-button
              @click="closeModalCausal();"
            >Cancelar</el-button>
            <el-button
              type="success"
              @click="submitFormCausal('formCausal')"
            >{{ textActionCausal }}</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-dialog>

    <el-drawer
      ref="drawer"
      :before-close="handleClose"
      :visible.sync="dialogDrawer"
      direction="rtl"
      custom-class="demo-drawer"
      size="38%"
    >
      <div style="background: #f7fbff; height: 100%;">
        <sticky class-name="sub-navbar">
          <el-row>
            <el-col :span="24" style="text-align: center;">
              <label style="font-size: x-large; color: white;">Causales</label>
            </el-col>
          </el-row>
        </sticky>

        <!-- Card donde se listan las causales -->

        <div class="app-container">
          <el-row>
            <transition name="el-fade-in-linear">
              <el-col v-show="countCausal > 0" v-loading="loading" :span="24">
                <el-card class="box-card" style="overflow-y: scroll; height: 70vh;">
                  <el-card v-for="item in datosCausal" :key="item.idcausal" style="width: 100%; margin-bottom: 3%;">
                    <div slot="header" class="clearfix">
                      <el-row>
                        <el-col :span="18">
                          <span style="color: #303133;"><b>{{ item.nombrecausal }}</b></span>
                        </el-col>
                        <el-col :span="3">
                          <div style="float: right; padding-right: 2%;">
                            <el-button style="border: 1px solid #67C23A;" size="mini" type="success" icon="el-icon-edit" :disabled="!abogadoEditar" @click="handleEditCausal(item)"><b>Editar</b></el-button>
                          </div>
                        </el-col>
                        <el-col :span="3">
                          <div style="float: right;">
                            <el-button size="mini" type="danger" icon="el-icon-delete" :disabled="!abogadoEditar" @click="handleDelete(item)" />
                          </div>
                        </el-col>
                      </el-row>
                    </div>
                    <div class="text item" style="width: 100%; border: 0px solid;">
                      <el-row>
                        <el-col :span="18">
                          <span style="color: #606266;"><b>Fecha hechos: </b></span>
                        </el-col>
                        <el-col :span="6">
                          <i v-if="item.f_hechos !== 'None'" class="el-icon-time" /> {{ convertDate(item.f_hechos) }}
                        </el-col>
                      </el-row>
                    </div>
                    <div class="text item" style="width: 100%;">
                      <!-- <span style="color: #606266;"><b>Descripción</b></span><br><br> -->
                      <el-input
                        v-model="item.descripcion"
                        type="textarea"
                        style="width: 100%;"
                        rows="4"
                        readonly
                      />
                    </div>
                  </el-card>
                </el-card>
              </el-col>
            </transition>
          </el-row>
          <el-row>
            <el-col :span="24" style="text-align: center; padding-top: 4%;">
              <el-button
                style="border: 1px solid #67c23a"
                type="primary"
                icon="el-icon-circle-plus"
                round
                :disabled="!abogadoEditar"
                @click="handleAgregarCausal()"
              >Agregar</el-button>
            </el-col>
          </el-row>
        </div>
      </div>
    </el-drawer>

    <!-- Modal de confirmacion para borrar un causal -->
    <modal-delete
      titulo="Advertencia"
      :mensaje="mensajeModalConfirm"
      :modalvisible="deleteDialogVisible"
      @confirmar="submitDelete"
    />
  </el-col>
</template>

<script>
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import Sticky from '@/components/Sticky' // 粘性header组件
import ModalDelete from '@/components/ModalConfirm'
import { CONSTANTS } from '../constants/constants'
import { getCausalProceso } from '@/api/procesosDIEG/causal'
import { createCausal } from '@/api/procesosDIEG/causal'
import { updateCausal } from '@/api/procesosDIEG/causal'
import { deleteCausal } from '@/api/procesosDIEG/causal'
import { getListCausal } from '@/api/procesosDIEG/causal'
import moment from 'moment'

export default {
  directives: { elDragDialog },
  components: {
    Sticky,
    ModalDelete
  },
  props: {
    idproceso: {
      type: String,
      required: true
    },
    editar: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      tableColumns: CONSTANTS.tableColumnsCausal,
      valSwitch: false,
      switchDisable: false,
      formCausal: CONSTANTS.formCausal,
      rulesFormCausal: CONSTANTS.rulesFormCausal,
      openModalCausal: false,
      dialogDrawer: false,
      datosCausal: [],
      listaCausal: [],
      countCausal: 0,
      busquedaCausal: '',
      textActionCausal: 'Agregar',
      dataPersona: CONSTANTS.dataPersona,
      mensajeModalConfirm: '',
      deleteDialogVisible: false,
      causalDel: '',
      loading: false,
      abogadoEditar: this.editar
    }
  },
  watch: {
    valSwitch: {
      deep: true,
      handler(val) {
        this.formCausal = {}
        this.resetForm()
        // console.log('valSwitch - > ', val)
        if (this.countCausal > 0) {
          this.valSwitch = true
          this.switchDisable = true
        } else {
          this.switchDisable = false
          this.valSwitch = false
          if (!this.dialogDrawer) {
            this.openModalCausal = true
          }
        }
      }
    },
    editar: {
      deep: true,
      handler(val) {
        console.log('antes !abogadoEditar" -> ', this.editar)
        this.abogadoEditar = val
        console.log('despues !abogadoEditar" -> ', this.editar)
      }
    }
  },
  async created() {
    await this.getCausal(this.idproceso)
    this.getCausales()
  },
  methods: {
    convertDate(val) {
      // console.log('convertDate -> ', val)
      if (val !== 'No registra') {
        return moment(val).format('DD/MM/YYYY')
      } else {
        return 'No registra'
      }
    },
    handleDelete(data) {
      // console.log(data)
      this.causalDel = { idproceso: data.idproceso, idcausal: data.idcausal }
      this.mensajeModalConfirm = `¿Realmente desea eliminar a <b>${data.nombrecausal}</b>?`
      this.deleteDialogVisible = true
    },
    async submitDelete(confirm) {
      if (confirm) {
        this.loading = true
        await deleteCausal(this.causalDel).then(async(response) => {
          this.$notify({
            title: 'Información',
            message: 'Se ha eliminado la causal!',
            position: 'bottom-right',
            type: 'success',
            duration: 2000
          })
          await this.getCausal(this.idproceso)
          this.getCausales()
          this.deleteDialogVisible = false
        })
      } else {
        this.deleteDialogVisible = false
      }
    },
    resetForm() {
      if (this.$refs['formCausal']) {
        this.formCausal = {}
        this.$refs['formCausal'].resetFields()
      }
    },
    handleAgregarCausal() {
      this.resetForm()
      this.textActionCausal = 'Agregar'
      this.openModalCausal = true
    },
    handleEditCausal(data) {
      // console.log('Editar causal -> ', data)
      this.resetForm()
      this.textActionCausal = 'Editar'
      this.openModalCausal = true
      const modelCausal = data
      this.formCausal = modelCausal
      this.formCausal.codcausal = data.idcausal
      this.formCausal.idcausal = data.nombrecausal
    },
    handleClose(done) {
      done()
    },
    closeModalCausal() {
      this.formCausal = {}
      this.openModalCausal = false
    },
    submitFormCausal(formName) {
      this.$refs[formName].validate(async(valid) => {
        if (valid) { // Crear causal
          this.loading = true
          // console.log('GUARDAR -> ', this.formCausal)
          if (this.textActionCausal === 'Agregar') {
            if (!this.formCausal.hasOwnProperty('descripcion')) {
              this.formCausal.descripcion = ''
            }
            this.formCausal.idproceso = this.idproceso
            await createCausal(this.formCausal).then(async(response) => {
              this.resetForm()
              this.$notify({
                title: 'Buen trabajo!',
                message: 'Causal agregada con éxito',
                position: 'bottom-right',
                type: 'success',
                duration: 2000
              })
              await this.getCausal(this.idproceso)
              this.getCausales()
            }, (err) => {
              console.log(err)
              this.$notify({
                title: 'Advertencia',
                message: 'No se pudo completar la operación!',
                position: 'bottom-right',
                type: 'warning',
                duration: 2000
              })
            })
          } else { // Actualizar causal
            await updateCausal(this.formCausal).then(async(response) => {
              this.resetForm()
              this.$notify({
                title: 'Buen trabajo!',
                message: 'Causal actualizada con éxito',
                position: 'bottom-right',
                type: 'success',
                duration: 2000
              })
              this.textActionCausal = 'Agregar'
              await this.getCausal(this.idproceso)
              this.getCausales()
            }, (err) => {
              console.log(err)
            })
          }
          this.openModalCausal = false
        }
      })
    },
    async getCausal(idproceso) {
      await getCausalProceso(idproceso).then((response) => {
        // console.log('CANTIDAD CAUSALES -> ', response.length)
        this.countCausal = response.length
        this.datosCausal = response
        if (this.countCausal > 0) {
          this.valSwitch = true
        } else {
          this.valSwitch = false
        }
        this.loading = false
      })
    },
    async getCausales() {
      await getListCausal().then((response) => {
        this.listaCausal = response
        for (const iterator of this.datosCausal) {
          this.listaCausal.filter((causa) => {
            if (causa.idcausal === iterator.idcausal) { // Verifica si la causa ya esta en el proceso y se elimina del arreglo de causas que se muestra en el select de causas
              const posEtapa = this.listaCausal.indexOf(causa)
              this.listaCausal.splice(posEtapa, 1)
            }
          })
        }
        // console.log('this.listaCausal - > ', this.listaCausal)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.control-modal {
  width: 23em;
}
</style>

<style lang="scss">
.dialog-class-lista {
  border-radius: 10px;
}

.dialog-class-lista .el-dialog__body {
  padding-top: 0 !important;
}
</style>

<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 15px;
  }

  .badge-causal .item {
    border: 0px solid red;
    padding-right: 6%;
  }

  .div-causas .div-causas-header .el-card__header {
    padding-top: 4%;
    padding-left: 4%;
    height: 7vh;
  }

  .card-causas .el-card__body {
    border: 0px solid;
    padding-top: 4%;
  }

  .card-causa .el-card__body {
    border: 0px solid;
    padding-top: 2%;
  }
</style>
