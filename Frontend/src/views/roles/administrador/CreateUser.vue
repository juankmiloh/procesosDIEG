<template>
  <div class="createPost-container" style="background: #f7fbff;">
    <div class="app-container">
      <div>
        <el-row :gutter="20">

          <el-col :span="10" :xs="24">
            <lista-users :data="viewRefresh" @handleSetUser="handleSetUser" />
          </el-col>

          <el-col :span="14" :xs="24">
            <el-card :class="x.matches ? '' : 'create-user'">
              <div slot="header" class="clearfix">
                <span>Crear usuario</span>
              </div>
              <!-- Formulario donde se cargan los datos del usuario -->
              <el-form
                ref="formUsuario"
                :rules="rulesFormUser"
                :model="formUsuario"
                label-width="120px"
                :inline="false"
                class="form-user"
              >
                <div>
                  <avatar :img="imageUrl" @preview-files="previewFiles" />
                </div>

                <el-row :gutter="10" style="border: 0px solid red; padding-left: 15%; padding-right: 15%;">
                  <el-col :span="24" :xs="24" style="border: 0px solid red; text-align: center;">
                    <el-form-item label="" prop="genero" class="item-genero">
                      <el-radio-group v-model="formUsuario.genero">
                        <el-radio-button
                          v-for="item in dataGenero"
                          :key="item.idgenero"
                          :label="item.nombre"
                        />
                      </el-radio-group>
                    </el-form-item>
                  </el-col>
                  <el-col :span="12" :xs="24" style="border: 0px solid red;">
                    <el-form-item label="" prop="nombre">
                      <el-input
                        v-model="formUsuario.nombre"
                        autocomplete="off"
                        placeholder="Nombre"
                        clearable
                        class="control-modal"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="12" :xs="24" style="border: 0px solid red;">
                    <el-form-item label="" prop="apellido">
                      <el-input
                        v-model="formUsuario.apellido"
                        autocomplete="off"
                        placeholder="Apellido"
                        clearable
                        class="control-modal"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="12" :xs="24" style="border: 0px solid red;">
                    <el-form-item label="" prop="nickname">
                      <el-input
                        v-model="formUsuario.nickname"
                        autocomplete="off"
                        placeholder="Usuario"
                        clearable
                        class="control-modal"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="12" :xs="24" style="border: 0px solid red;">
                    <el-form-item label="" prop="contrasena">
                      <el-input
                        v-model="formUsuario.contrasena"
                        type="password"
                        autocomplete="off"
                        placeholder="Contraseña"
                        clearable
                        class="control-modal"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="12" :xs="24" style="border: 0px solid red;">
                    <el-form-item label="" prop="rol">
                      <el-select v-model="formUsuario.rol" placeholder="Tipo de usuario" class="control-modal">
                        <el-option
                          v-for="item in dataRoles"
                          :key="item.idrol"
                          :label="item.nombre"
                          :value="item.idrol"
                        />
                      </el-select>
                    </el-form-item>
                  </el-col>
                  <el-col :span="12" :xs="24" style="border: 0px solid red;">
                    <el-form-item label="" prop="email">
                      <el-input
                        v-model="formUsuario.email"
                        autocomplete="off"
                        placeholder="Correo electrónico"
                        clearable
                        class="control-modal"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="24" :xs="24" style="border: 0px solid red;">
                    <el-form-item label="" prop="descripcion">
                      <el-input
                        v-model="formUsuario.descripcion"
                        type="textarea"
                        class="control-modal"
                        rows="3"
                        placeholder="Descripción"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="12" :xs="24" style="border: 0px solid red; text-align: right;">
                    <el-form-item>
                      <el-button :class="x.matches ? 'btn-create-sm' : 'btn-create-md'" @click="resetForm('formUsuario')">Limpiar</el-button>
                    </el-form-item>
                  </el-col>
                  <el-col :span="12" :xs="24" style="border: 0px solid red; text-align: left;">
                    <el-form-item>
                      <el-button
                        :class="x.matches ? 'btn-create-sm' : 'btn-create-md'"
                        type="success"
                        @click="submitForm('formUsuario')"
                      >{{ textButton }}</el-button>
                    </el-form-item>
                  </el-col>
                </el-row>
              </el-form>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
import { validUsername } from '@/utils/validate'
import { mapGetters } from 'vuex'
import { createUser } from '@/api/procesosDIEG/usuarios'
import { updateUsuario } from '@/api/procesosDIEG/usuarios'
import { getListRol } from '@/api/procesosDIEG/usuarios'
import { CONSTANTS } from '@/constants/constants'
import { DATA } from '@/data/ImgUser'
import md5 from 'md5'
import ListaUsers from './components/user/ListaUsers'
import Avatar from './components/user/Avatar'

export default {
  name: 'CreateUser',
  components: {
    Avatar, ListaUsers
  },
  data() {
    return {
      formUsuario: CONSTANTS.formUser,
      rulesFormUser: CONSTANTS.rulesFormUser,
      loading: false,
      dataRoles: [],
      imageUrl: DATA.imageURL,
      dataGenero: CONSTANTS.dataGenero,
      viewRefresh: { action: false },
      textButton: 'Guardar',
      updateUSer: false,
      nicknameold: '',
      x: ''
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'dependencia'])
  },
  created() {
    this.initView()
    this.x = window.matchMedia('(max-width: 800px)')
  },
  methods: {
    handleSetUser(param) {
      // console.log('handleSetUser -> ', param)
      if (param.hasOwnProperty('updateView')) {
        this.rulesFormUser.contrasena[0].required = true
        this.updateUSer = false
        this.textButton = 'Guardar'
        this.viewRefresh.action = param.updateView
      } else {
        this.rulesFormUser.contrasena[0].required = false
        this.updateUSer = true
        this.textButton = 'Actualizar'
        this.formUsuario = param
        this.imageUrl = param.avatar
        this.nicknameold = param.nickname
        window.localStorage.setItem('userUpdate', param.nickname)
      }
    },
    async previewFiles(event) {
      if (event) {
        // console.log('file -> ', event)
        this.formUsuario.avatar = event
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
        if (this.updateUSer) {
          if (usernameLower === window.localStorage.getItem('userUpdate')) {
            callback()
          } else {
            callback(new Error('Nombre de usuario ya esta en uso'))
          }
        } else {
          callback(new Error('Nombre de usuario ya esta en uso'))
        }
      } else if (this.formUsuario.nickname === '') {
        callback(new Error('Ingrese nombre de usuario'))
      } else {
        callback()
      }
    },
    validatePassword(rule, value, callback) {
      if (!this.updateUSer) { // Si no actualiza usuario
        if (value.length < 6) {
          callback(
            new Error('No puede ser menor a seis caracteres')
          )
        } else {
          callback()
        }
      } else { // Si se actualiza usuario
        if (this.formUsuario.contrasena !== '') {
          this.rulesFormUser.contrasena[0].required = true
          if (value.length < 6) {
            callback(
              new Error('No puede ser menor a seis caracteres')
            )
          } else {
            callback()
          }
        } else {
          this.rulesFormUser.contrasena[0].required = false
          callback()
        }
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
        // console.log(response)
        this.dataRoles = response
      })
    },
    submitForm(formName) {
      this.$refs[formName].validate(async(valid) => {
        if (!this.updateUSer) { // Si no actualiza usuario
          if (valid) {
            const modelUser = this.formUsuario
            modelUser.token = `${modelUser.nickname}-token`
            modelUser.rol = Number(modelUser.rol)
            modelUser.contrasena = md5(modelUser.contrasena)
            modelUser.genero = this.dataGenero.find((genero) => genero.nombre === modelUser.genero).idgenero
            modelUser.dependencia = this.dependencia
            console.log('Guardar modelUser -> ', modelUser)
            await createUser(modelUser).then(async(response) => {
              this.$notify({
                title: 'Bien hecho!',
                message: 'Usuario creado con éxito',
                position: 'top-right',
                type: 'success',
                duration: 2000
              })
              this.imageUrl = ''
            })
            this.resetForm('formUsuario')
          } else {
            // console.log('error submit!!')
            return false
          }
        } else { // Si se actualiza usuario
          if (valid) {
            const modelUser = this.formUsuario
            modelUser.token = `${modelUser.nickname}-token`
            modelUser.genero = this.dataGenero.find((genero) => genero.nombre === modelUser.genero).idgenero
            modelUser.nicknameold = this.nicknameold
            if (modelUser.contrasena !== '') {
              modelUser.contrasena = md5(modelUser.contrasena)
            }
            // console.log('actualizar modelUser -> ', modelUser)
            await updateUsuario(modelUser).then(async(response) => {
              this.$notify({
                title: 'Bien hecho!',
                message: 'Usuario actualizado con éxito',
                position: 'top-right',
                type: 'success',
                duration: 2000
              })
              this.$refs[formName].resetFields()
              this.viewRefresh = { idusuario: modelUser.idusuario, action: true }
            })
          }
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
      this.formUsuario = CONSTANTS.formUser
      this.formUsuario.avatar = DATA.imageURL
      this.imageUrl = DATA.imageURL
      this.viewRefresh = { action: true }
    }
  }
}
</script>

<style lang="scss" scoped>
.control-modal {
  width: 100%;
}

.create-user {
  position: fixed;
  margin-right: 13px;
}

.btn-create-sm {
  width: 100%;
}

.btn-create-md {
  width: 13em;
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
.form-user .el-form-item .el-form-item__content {
  margin-left: 0% !important;
}
.item-genero .el-form-item__error {
  padding-left: 12.5vw;
}
</style>
