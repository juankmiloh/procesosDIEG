/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getListProcesosEmpresa() {
    return request({
        url: '/procesos_empresa',
        method: 'get'
    });
}

export function getListProcesosCausal() {
    return request({
        url: '/procesos_causal',
        method: 'get'
    });
}

export function getListProcesosEstado() {
    return request({
        url: '/procesos_estado',
        method: 'get'
    });
}

export function getListCantidadProcesos() {
    return request({
        url: '/cantidad_procesos',
        method: 'get'
    });
}