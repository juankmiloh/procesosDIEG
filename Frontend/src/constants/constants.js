/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    tableColumnsProceso: [
        // {
        //     label: 'ID Proceso',
        //     prop: 'idproceso'
        // },
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
    tableColumnsEtapas: [{
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
            { required: true, message: 'Ingrese un expediente', trigger: 'change' },
            {
                min: 15,
                max: 15,
                message: 'La longitud del expediente debe ser de 15 caracteres'
            }
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
    }
};