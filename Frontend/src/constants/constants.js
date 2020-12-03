/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    tableColumnsAdmin: [{
            label: '#',
            prop: 'idproceso'
        },
        {
            label: 'Expediente',
            prop: 'expediente'
        },
        {
            label: 'Empresa',
            prop: 'empresa'
        },
        // {
        //     label: 'Servicio',
        //     prop: 'servicio'
        // },
        {
            label: 'Estado',
            prop: 'estado'
        },
        {
            label: 'Caducidad',
            prop: 'caducidad'
        },
        {
            label: 'Abogado',
            prop: 'usuario'
        }
    ],
    tableColumnsAbogado: [{
            label: '#',
            prop: 'idproceso'
        },
        {
            label: 'Expediente',
            prop: 'expediente'
        },
        {
            label: 'Empresa',
            prop: 'empresa'
        },
        // {
        //     label: 'Servicio',
        //     prop: 'servicio'
        // },
        {
            label: 'Estado',
            prop: 'estado'
        },
        {
            label: 'Caducidad',
            prop: 'caducidad'
        }
    ],
    tableColumnsEtapas: [{
            label: '#',
            prop: 'idetapa'
        },
        {
            label: 'Radicado',
            prop: 'radicadoEtapa'
        },
        {
            label: 'Etapa',
            prop: 'nombreEtapa'
        },
        {
            label: 'Fecha de inicio',
            prop: 'fechaInicioEtapa'
        },
        {
            label: 'Fecha fin',
            prop: 'fechaFinEtapa'
        },
        {
            label: 'Observación',
            prop: 'observacionEtapa'
        }
    ],
    filters: [
        { text: 'Energía', value: 'Energía' },
        { text: 'Gas', value: 'Gas' },
        { text: 'GLP', value: 'GLP' },
    ],
    rulesFormProceso: {
        radicado: [
            { required: true, message: 'Ingrese un expediente', trigger: 'blur' },
            { min: 15, max: 15, message: 'La longitud del expediente debe ser de 15 caracteres', trigger: 'blur' }
        ],
        servicio: [{
            required: true,
            message: 'Seleccione un servicio',
            trigger: 'change'
        }],
        empresa: [{
            required: true,
            message: 'Seleccione una empresa',
            trigger: 'change'
        }],
        usuario: [{
            required: true,
            message: 'Seleccione un usuario',
            trigger: 'change'
        }],
        fecha_caducidad: [{
            type: 'date',
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }]
    },
    formAgregar: {
        radicado: '',
        servicio: '',
        empresa: '',
        usuario: '',
        fecha_caducidad: null
    },
    formUsuario: {
        usuario: '',
        expediente: ''
    },
    formDetalleProceso: {
        expediente: '',
        tipo_sancion: '',
        decision: '',
        sancion: '',
        descripcion: ''
    },
    rulesDetalleProceso: {
        expediente: [
            { required: true, message: 'Ingrese un expediente', trigger: 'blur' },
            { min: 15, max: 15, message: 'La longitud debe ser de 15 caracteres', trigger: 'blur' }
        ],
        empresa: [{
            required: true,
            message: 'Seleccione una empresa',
            trigger: 'change'
        }],
        tipo_sancion: [{
            required: false,
            message: 'Seleccione un tipo de sanción',
            trigger: 'change'
        }],
        sancion: [
            { required: false, message: 'Valor sanción requerido' },
            { type: 'number', message: 'La sanción debe ser un número' }
        ],
        decision: [{
            required: false,
            message: 'Seleccione una decision',
            trigger: 'change'
        }],
        causa: [{
            required: true,
            message: 'Seleccione una causal',
            trigger: 'change'
        }],
        fecha_hechos: [{
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
        caducidad: [{
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }]
    },
    formAgregarEtapa: {
        etapa: '',
        fechaInicioEtapa: null,
        fechaFinEtapa: null,
        observacionEtapa: ''
    },
    rulesFormEtapa: {
        etapa: [{
            required: true,
            message: 'Seleccione una etapa',
            trigger: 'change'
        }],
        fechaInicioEtapa: [{
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
        observacionEtapa: [{
            required: false,
            message: 'Ingrese una observación',
            trigger: 'blur'
        }]
    },
    formUser: {
        nombre: '',
        apellido: '',
        genero: '',
        nickname: '',
        contrasena: '',
        rol: '',
        descripcion: '',
        avatar: '',
        token: ''
    },
    rulesFormUser: {
        nombre: [
            { required: true, message: 'Ingrese nombre', trigger: 'blur' }
        ],
        apellido: [
            { required: true, message: 'Ingrese apellido', trigger: 'blur' }
        ],
        genero: [{
            required: true,
            message: 'Seleccione un género',
            trigger: 'change'
        }],
        rol: [{
            required: true,
            message: 'Seleccione un rol',
            trigger: 'change'
        }],
        descripcion: [{
            required: true,
            message: 'Ingrese una descripción del usuario',
            trigger: 'change'
        }],
    },
    dataGenero: [{
            idgenero: 1,
            nombre: 'Femenino'
        },
        {
            idgenero: 2,
            nombre: 'Masculino'
        }
    ]
};