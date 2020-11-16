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
    rulesFormAgregar: {
        radicado: [
            { required: true, message: 'Ingrese un expediente' },
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
    }
};