<template>
  <div class="createPost-container" style="background: #f7fbff;">
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

              <div class="demo-basic--circle" style="text-align: center; padding-bottom: 3%;">
                <div class="block" style="padding-bottom: 1%;"><el-avatar :size="150" :src="imageUrl" /></div>
                <label class="file-upload">
                  <input type="file" @change="previewFiles">
                  <span style="font-size: small; color: gray;">Cambiar foto</span>
                </label>
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
                  placeholder="Ingrese nombre de usuario"
                  clearable
                  class="control-modal"
                />
              </el-form-item>

              <el-form-item label="Género" prop="genero">
                <el-select v-model="formUsuario.genero" placeholder="Seleccione un genero" class="control-modal">
                  <el-option
                    v-for="item in dataGenero"
                    :key="item.idgenero"
                    :label="item.nombre"
                    :value="item.idgenero"
                  />
                </el-select>
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
                  <el-option
                    v-for="item in dataRoles"
                    :key="item.idrol"
                    :label="item.nombre"
                    :value="item.idrol"
                  />
                </el-select>
              </el-form-item>

              <el-form-item label="Descripción" prop="descripcion">
                <el-input
                  v-model="formUsuario.descripcion"
                  type="textarea"
                  class="control-modal"
                  rows="3"
                />
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
import { validUsername } from '@/utils/validate'
import { mapGetters } from 'vuex'
import { createUser } from '@/api/procesosDIEG/usuarios'
import { getListRol } from '@/api/procesosDIEG/usuarios'
import Sticky from '@/components/Sticky' // 粘性header组件
import { CONSTANTS } from '@/constants/constants'
import { DATA } from '@/data/ImgUser'
import md5 from 'md5'

export default {
  name: 'CreateUser',
  components: { Sticky },
  data() {
    return {
      formUsuario: CONSTANTS.formUser,
      rulesFormUser: CONSTANTS.rulesFormUser,
      loading: false,
      dataRoles: [],
      imageUrl: DATA.imageURL,
      dataGenero: CONSTANTS.dataGenero
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    this.initView()
  },
  methods: {
    async previewFiles(event) {
      const file = event.target.files[0]
      if (file) {
        // console.log('file -> ', file)
        this.imageUrl = await this.imgToBase64(file)
        this.formUsuario.avatar = this.imageUrl
        console.log(this.imageUrl)
      }
    },
    imgToBase64(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = () => resolve(reader.result)
        reader.onerror = error => reject(error)
      })
    },
    validateUsername(rule, value, callback) {
      const usernameLower = value.toLowerCase()
      if (validUsername(usernameLower)) {
        callback(new Error('Nombre de usuario ya esta en uso'))
      } else if (this.formUsuario.nickname === '') {
        callback(new Error('Ingrese nombre de usuario'))
      } else {
        callback()
      }
    },
    validatePassword(rule, value, callback) {
      if (value.length < 6) {
        callback(
          new Error('La contraseña no puede ser menor a seis caracteres')
        )
      } else {
        callback()
      }
    },
    async initView() {
      this.getDataRoles()
      this.formUsuario.avatar = DATA.imageURL
      this.rulesFormUser.nickname = [
        { required: true, trigger: 'blur', validator: this.validateUsername }
      ]
      this.rulesFormUser.contrasena = [
        { required: true, trigger: 'blur', validator: this.validatePassword }
      ]
    },
    async getDataRoles() {
      await getListRol().then((response) => {
        console.log(response)
        this.dataRoles = response
      })
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
            this.imageUrl = DATA.imageURL
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

<style>
.file-upload {
  cursor: pointer;
  border: 0px solid gray;
  border-radius: 3px;
  padding: 3px;
}

.file-upload input {
  overflow: hidden;
  width: 0;
}
</style>

