<template>
  <div style="border: 0px solid blue;">
    <div style="padding-bottom: 65px">
      <sticky class-name="sub-navbar" style="position: fixed; width: 100%;">
        <div style="text-align: center; color: white">
          <el-row>
            <el-col :span="13" :xs="9" class="div-header">
              <label v-if="x.matches" style="font-size: small">{{ expediente }}</label>
              <label v-else style="font-size: x-large">Etapas expediente {{ expediente }}</label>
            </el-col>
            <el-col :span="11" :xs="15" style="border: 0px solid red; text-align: right;">
              <!-- Boton para agregar nueva etapa al aplicativo -->
              <el-button
                :disabled="!editar"
                style="border: 2px solid #67c23a"
                size="medium"
                icon="el-icon-circle-plus"
                @click="clickAgregarEtapa();"
              >Agregar etapa</el-button>
              <el-button
                style="border: 1px solid #67c23a"
                type="warning"
                size="medium"
                @click="closeModalEtapa()"
              >{{ btnClose() }}</el-button>
            </el-col>
          </el-row>
        </div>
      </sticky>
    </div>

    <!-- Cuadro de dialogo para editar o asignar etapa -->
    <!-- <AgregarEtapa
      :modaltitulo="tituloModalItem"
      :modalvisible="dialogVisibleItem"
    /> -->

    <el-dialog
      v-el-drag-dialog
      :visible.sync="msgAgregarEtapaVisible"
      :before-close="closeModalAgregar"
      width="34em"
      custom-class="dialog-agregar-etapa"
      :destroy-on-close="true"
      append-to-body
    >
      <AgregarEtapa />
    </el-dialog>

    <!-- Listado de etapas -->
    <ListaEtapas :id="id" :editar="editar" />

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Sticky from '@/components/Sticky' // 粘性header组件
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import { CONSTANTS } from '@/constants/constants'
import ListaEtapas from './ListaEtapas'
import AgregarEtapa from './AgregarEtapa'

export default {
  name: 'Etapas',
  components: { Sticky, ListaEtapas, AgregarEtapa },
  directives: { elDragDialog },
  props: {
    editar: {
      type: Boolean,
      default: false
    },
    id: {
      type: String,
      default: ''
    },
    expediente: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      formAgregar: CONSTANTS.formAgregarEtapa,
      textEditarEtapa: 'Agregar',
      /* Si es o no visible el cuadro de dialogo de agregar o editar etapa */
      msgAgregarEtapaVisible: false,
      x: ''
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'idusuario', 'dependencia'])
  },
  async mounted() {
    this.x = window.matchMedia('(max-width: 800px)')
  },
  created() {
    this.initView()
  },
  methods: {
    async initView() {
    },
    btnClose() {
      if (this.x.matches) {
        return 'X'
      } else {
        return 'Cerrar'
      }
    },
    closeModalEtapa() {
      this.$emit('close-modal-etapas')
    },
    clickAgregarEtapa() {
      this.editarEtapa = false
      this.textEditarEtapa = 'Agregar'
      this.formAgregar = {}
      if (this.$refs['formAgregar']) {
        this.$refs['formAgregar'].resetFields()
      }
      this.msgAgregarEtapaVisible = true
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

<style lang="scss">
  // Pantallas superiores a 800px (PC)
  @media screen and (min-width: 800px) {
    .div-header {
      text-align: right;
    }
  }

  // Pantallas inferiores a 800px (mobile)
  @media screen and (max-width: 800px) {
    .div-header {
      text-align: center;
    }
  }
</style>
