<template>
  <el-col :md="24" style="border: 0px solid blue; padding-top: 10px">
    <el-card class="box-card">
      <el-row>
        <el-col :md="19">
          <span>Terceros interesados</span>
          (<count-to :start-val="0" :end-val="countTerceros" :duration="5000" class="card-panel-num" />)
        </el-col>
        <el-col :md="countTerceros > 0 ? 4 : 5">
          <el-switch v-model="valSwitch" :disabled="switchDisable" />
        </el-col>
        <el-col v-if="countTerceros > 0" :md="countTerceros > 0 ? 1 : 0">
          <div>
            <el-link icon="el-icon-user-solid" :underline="false" @click="dialogDrawer=true" />
          </div>
        </el-col>
      </el-row>
    </el-card>

    <!-- Cuadro de dialogo para agregar / editar tercero -->

    <el-dialog
      v-el-drag-dialog
      :visible.sync="openModalTercero"
      :before-close="closeModalTercero"
      width="34em"
      custom-class="dialog-class-lista"
      :show-close="false"
    >
      <sticky class-name="sub-navbar">
        <div style="border: 0px solid red; color: white; text-align: center">
          <h2>{{ textActionTercero }} tercero</h2>
        </div>
      </sticky>
      <div
        class="createPost-container"
        style="padding-top: 35px; padding-bottom: 20px; padding-left: 13px"
      >
        <el-form
          ref="formTercero"
          :model="formTercero"
          :rules="rulesFormTercero"
          label-width="120px"
          class="demo-ruleForm"
        >
          <el-form-item label="" prop="persona">
            <el-radio-group v-model="formTercero.persona">
              <el-radio-button label="Persona natural" />
              <el-radio-button label="Persona jurídica" />
              <!-- <el-radio-button
                v-for="item in datapersona"
                :key="item.idpersona"
                :label="item.nombre"
              /> -->
            </el-radio-group>
          </el-form-item>
          <transition name="el-zoom-in-center">
            <el-form-item v-show="formTercero.persona" :label="formTercero.persona === 'Persona natural' ? 'Documento' : 'NIT'" prop="documento">
              <el-input
                v-model.number="formTercero.documento"
                autocomplete="off"
                class="control-modal"
              />
            </el-form-item>
          </transition>
          <el-form-item label="Nombre" prop="nombre">
            <el-input
              v-model="formTercero.nombre"
              autocomplete="off"
              clearable
              class="control-modal"
            />
          </el-form-item>
          <el-form-item label="Dirección" prop="direccion">
            <el-input
              v-model="formTercero.direccion"
              autocomplete="off"
              clearable
              class="control-modal"
            />
          </el-form-item>
          <el-form-item label="E-mail" prop="email">
            <el-input
              v-model="formTercero.email"
              autocomplete="off"
              clearable
              class="control-modal"
            />
          </el-form-item>
          <el-form-item>
            <el-button
              @click="closeModalTercero('formTercero');"
            >Cancelar</el-button>
            <el-button
              type="success"
              @click="submitFormTercero('formTercero')"
            >Agregar</el-button>
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
      size="70%"
    >
      <div style="background: #f7fbff; height: 100%;">
        <sticky class-name="sub-navbar">
          <el-row>
            <el-col :span="24" style="text-align: center;">
              <label style="font-size: x-large; color: white;">Terceros interesados</label>
            </el-col>
          </el-row>
        </sticky>

        <!-- Tabla donde se listan los terceros interesados -->

        <div class="app-container">
          <el-card class="box-card">
            <el-table
              :z-index="0"
              :data="
                datosTerceros.filter(
                  (data) =>
                    !busquedaTercero ||
                    String(data.documento)
                      .toLowerCase()
                      .includes(busquedaTercero.toLowerCase())
                )
              "
              style="width: 100%; border: 1px solid #d8ebff"
              border
            >
              <el-table-column
                v-for="column in tableColumns"
                :key="column.label"
                :label="column.label"
                :prop="column.prop"
                align="center"
                sortable
                :width="column.width"
              />
              <el-table-column align="center" :width="140">
                <!-- eslint-disable-next-line -->
              <template slot="header" slot-scope="scope">
                  <el-input
                    v-model="busquedaTercero"
                    size="mini"
                    placeholder="No. documento"
                  />
                </template>
                <template slot-scope="scope">
                  <el-button
                    size="mini"
                    type="success"
                    icon="el-icon-edit"
                    @click="handleEditTercero(scope.row)"
                  />
                  <el-button
                    size="mini"
                    type="danger"
                    icon="el-icon-delete-solid"
                    @click="handleDelete(scope.row)"
                  />
                </template>
              </el-table-column>
            </el-table>
          </el-card>
          <el-row>
            <el-col :span="24" style="text-align: center; padding-top: 2%;">
              <el-button
                style="border: 1px solid #67c23a"
                type="primary"
                icon="el-icon-circle-plus"
                round
                @click="handleAgregarTercero()"
              >Agregar</el-button>
            </el-col>
          </el-row>
        </div>
      </div>
    </el-drawer>
  </el-col>
</template>

<script>
import CountTo from 'vue-count-to'
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import Sticky from '@/components/Sticky' // 粘性header组件
import { CONSTANTS } from '../constants/constants'
import { getTercerosProceso } from '@/api/procesosDIEG/terceros'

export default {
  directives: { elDragDialog },
  components: {
    CountTo,
    Sticky
  },
  props: {
    idproceso: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      tableColumns: CONSTANTS.tableColumnsTerceros,
      valSwitch: false,
      switchDisable: false,
      formTercero: CONSTANTS.formTercero,
      rulesFormTercero: CONSTANTS.rulesFormTercero,
      openModalTercero: false,
      dialogDrawer: false,
      datosTerceros: [],
      countTerceros: 0,
      agregarTerceroInit: true,
      busquedaTercero: '',
      textActionTercero: 'Agregar'
    }
  },
  watch: {
    valSwitch: {
      deep: true,
      handler(val) {
        this.formTercero = {}
        if (this.countTerceros > 0) {
          this.valSwitch = true
          this.switchDisable = true
        } else {
          if (this.agregarTerceroInit) {
            this.resetForm()
            this.openModalTercero = true
          } else {
            this.agregarTerceroInit = true
          }
        }
      }
    }
  },
  created() {
    this.getTerceros(this.idproceso)
  },
  methods: {
    resetForm() {
      if (this.$refs['formTercero']) {
        this.formTercero = {}
        this.$refs['formTercero'].resetFields()
      }
    },
    handleAgregarTercero() {
      this.resetForm()
      this.textActionTercero = 'Agregar'
      this.openModalTercero = true
    },
    handleEditTercero(data) {
      // console.log(data)
      this.resetForm()
      this.textActionTercero = 'Editar'
      this.openModalTercero = true
      const modelTercero = data
      this.formTercero = modelTercero
    },
    handleClose(done) {
      done()
    },
    closeModalTercero(formName) {
      this.formTercero = {}
      this.agregarTerceroInit = false
      this.valSwitch = false
      this.openModalTercero = false
    },
    submitFormTercero(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          console.log(this.formTercero)
        }
      })
    },
    async getTerceros(idproceso) {
      await getTercerosProceso(idproceso).then((response) => {
        // console.log('TERCEROS -> ', response)
        this.countTerceros = response.length
        this.datosTerceros = response
        if (this.countTerceros > 0) {
          this.valSwitch = true
        }
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
