<template>
  <div class="createPost-container" style="background: #f7fbff; height: 89vh;">
    <sticky class-name="sub-navbar">
      <div style="border: 0px solid red">
        <span />
      </div>
    </sticky>

    <!-- Formulario donde se cargan los datos del proceso -->

    <div v-loading="loading" class="app-container">
      <el-row :gutter="10">
        <!-- Card datos proceso -->
        <el-form
          ref="formUsuario"
          :rules="rulesFormUser"
          :model="formUsuario"
          label-width="120px"
          class="demo-ruleForm"
        >
          <el-col :md="24" style="border: 0px solid blue; padding-left: 25%; padding-right: 25%;">
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>Crear usuario</span>
              </div>

              <el-form-item label="Nombre" prop="nombre">
                <el-input
                  v-model="formUsuario.nombre"
                  autocomplete="off"
                  placeholder="Ingrese nombre"
                  clearable
                  class="control-modal"
                />
              </el-form-item>

              <el-form-item label="Apellido" prop="apellido">
                <el-input
                  v-model="formUsuario.apellido"
                  autocomplete="off"
                  placeholder="Ingrese apellido"
                  clearable
                  class="control-modal"
                />
              </el-form-item>

              <el-form-item label="Usuario" prop="nickname">
                <el-input
                  v-model="formUsuario.nickname"
                  autocomplete="off"
                  placeholder="Ingrese nickname"
                  clearable
                  class="control-modal"
                />
              </el-form-item>

              <el-form-item label="Contraseña" prop="contrasena">
                <el-input
                  v-model="formUsuario.contrasena"
                  type="password"
                  autocomplete="off"
                  placeholder="Ingrese contrasena"
                  clearable
                  class="control-modal"
                />
              </el-form-item>

              <el-form-item label="Tipo usuario" prop="rol">
                <el-select v-model="formUsuario.rol" placeholder="Seleccione un rol" class="control-modal">
                  <el-option label="Administrador" value="1" />
                  <el-option label="Abogado" value="2" />
                </el-select>
              </el-form-item>

              <el-form-item>
                <el-button
                  style="width: 10em"
                  type="success"
                  @click="submitForm('formUsuario')"
                >Guardar</el-button>
              </el-form-item>
            </el-card>
          </el-col>
        </el-form>
      </el-row>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { createUser } from '@/api/procesosDIEG/usuarios'
import Sticky from '@/components/Sticky' // 粘性header组件
import { CONSTANTS } from '@/constants/constants'
import md5 from 'md5'

export default {
  name: 'CreateUser',
  components: { Sticky },
  data() {
    return {
      formUsuario: {
        nombre: '',
        apellido: '',
        nickname: '',
        contrasena: '',
        rol: '',
        descripcion: '',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        token: ''
      },
      rulesFormUser: CONSTANTS.rulesFormUser,
      loading: false
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    this.initView()
  },
  methods: {
    async initView() {

    },
    submitForm(formName) {
      this.$refs[formName].validate(async(valid) => {
        if (valid) {
          this.formUsuario.token = `${this.formUsuario.nickname}-token`
          this.formUsuario.rol = Number(this.formUsuario.rol)
          this.formUsuario.contrasena = md5(this.formUsuario.contrasena)
          console.log(this.formUsuario)
          await createUser(this.formUsuario).then(async(response) => {
            this.$notify({
              title: 'Bien hecho!',
              message: 'Usuario creado con éxito',
              position: 'top-right',
              type: 'success',
              duration: 2000
            })
            this.$refs[formName].resetFields()
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.control-modal {
  width: 100%;
}
</style>
