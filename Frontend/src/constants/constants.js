/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    tableColumns: [
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
    filters: [
        { text: 'Energía', value: 'Energía' },
        { text: 'Gas', value: 'Gas' },
        { text: 'GLP', value: 'GLP' },
    ],
    rulesFormProceso: {
        radicado: [
            { required: true, message: 'Ingrese un expediente', trigger: 'change' },
            {
                min: 14,
                max: 14,
                message: 'La longitud del expediente debe ser de 14 caracteres'
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
    },
    etapas: {
        etapas: [{
                nombreEtapa: 'Radicación',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2017-12-20',
                fechaFinEtapa: '2018-01-20',
                observacionEtapa: ''
            },
            {
                nombreEtapa: 'Memorando',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2018-01-20',
                fechaFinEtapa: '2018-01-30',
                observacionEtapa: ''
            },
            {
                nombreEtapa: 'Informe de Gestión',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2018-01-30',
                fechaFinEtapa: '2018-07-30',
                observacionEtapa: 'Se requrio explicación mediante radicado 2000XYX'
            },
            {
                nombreEtapa: 'Indagación Preeliminar - Auto',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2018-07-30',
                fechaFinEtapa: '2018-09-30',
                observacionEtapa: ''
            },
            {
                nombreEtapa: 'Probatoria - Auto de pruebas',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2018-09-30',
                fechaFinEtapa: '2018-12-02',
                observacionEtapa: ''
            },
            {
                nombreEtapa: 'Translado de alegatos - Auto',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2018-12-02',
                fechaFinEtapa: '2019-02-03',
                observacionEtapa: 'Se dio translado a todos por parte de gestión documental'
            },
            {
                nombreEtapa: 'Translado de alegatos - Alegatos',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2019-02-03',
                fechaFinEtapa: '2019-02-12',
                observacionEtapa: ''
            },
            {
                nombreEtapa: 'Pliego de cargos',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2019-02-12',
                fechaFinEtapa: '2019-04-15',
                observacionEtapa: ''
            },
            {
                nombreEtapa: 'Descargos',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2019-04-15',
                fechaFinEtapa: '2019-04-30',
                observacionEtapa: ''
            },
            {
                nombreEtapa: 'Sancion',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2019-04-30',
                fechaFinEtapa: '2019-06-01',
                observacionEtapa: 'Sanción por monto de $ 1.000.000'
            },
            {
                nombreEtapa: 'Recurso de reposición - Radicación',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2019-06-01',
                fechaFinEtapa: '2019-06-10',
                observacionEtapa: ''
            },
            {
                nombreEtapa: 'Resolución recurso',
                radicadoEtapa: '2000XXXXXX',
                fechaInicioEtapa: '2019-06-10',
                fechaFinEtapa: '2019-11-01',
                observacionEtapa: ''
            }
            // {
            //   nombreEtapa: 'Firmeza',
            //   radicadoEtapa: '2000XXXXXX',
            //   fechaInicioEtapa: '2019-11-01',
            //   fechaFinEtapa: '2019-12-18',
            //   observacionEtapa: 'En espera a tutela'
            // }
        ]
    }
};