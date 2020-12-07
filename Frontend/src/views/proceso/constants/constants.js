/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    formTercero: {
        idtercero: '',
        persona: '',
        documento: '',
        nombre: '',
        direccion: '',
        email: ''
    },
    rulesFormTercero: {
        persona: [{
            required: true,
            message: 'Seleccione un tipo de persona',
            trigger: 'change'
        }],
        documento: [
            { required: true, message: 'Ingrese un documento' },
            { type: 'number', message: 'Este campo debe ser numérico' }
        ],
        nombre: [
            { required: true, message: 'Ingrese un nombre', trigger: 'blur' },
        ],
        direccion: [
            { required: true, message: 'Ingrese una dirección', trigger: 'blur' },
        ],
        email: [
            { type: "email", required: true, message: 'Ingrese un correo electrónico válido', trigger: 'blur' },
        ],
    },
    tableColumnsTerceros: [{
            label: 'Tipo',
            prop: 'persona',
            width: 125
        },
        {
            label: 'Documento',
            prop: 'documento',
            width: 125
        },
        {
            label: 'Nombre',
            prop: 'nombre',
            width: 170
        },
        {
            label: 'Dirección',
            prop: 'direccion',
            width: 200
        },
        {
            label: 'Email',
            prop: 'email',
            width: 230
        }
    ],
    dataPersona: [{
            idpersona: 1,
            nombre: 'Persona natural'
        },
        {
            idpersona: 2,
            nombre: 'Persona jurídica'
        }
    ]
};