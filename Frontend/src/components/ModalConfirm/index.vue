<template>
  <el-dialog
    v-el-drag-dialog
    :title="titulo"
    :visible.sync="modalvisible"
    :before-close="handleCancel"
    :width="x.matches ? '80%' : '40%'"
    center
    append-to-body
  >
    <center>
      <span v-html="mensaje" />
    </center>
    <span slot="footer" class="dialog-footer">
      <el-button @click="handleCancel()">Cancelar</el-button>
      <el-button
        type="primary"
        @click="handleConfirm()"
      >Confirmar</el-button>
    </span>
  </el-dialog>
</template>

<script>
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui

export default {
  name: 'ModalConfirm',
  directives: { elDragDialog },
  props: {
    titulo: {
      type: String,
      default: ''
    },
    mensaje: {
      type: String,
      default: ''
    },
    modalvisible: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      x: ''
    }
  },
  created() {
    this.x = window.matchMedia('(max-width: 800px)')
  },
  methods: {
    handleCancel() {
      this.$emit('confirmar', false)
    },
    handleConfirm() {
      this.$emit('confirmar', true)
    }
  }
}
</script>
