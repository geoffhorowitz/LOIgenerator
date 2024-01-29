//import React from 'react'

import getConfigs from '../configs'
const { debug_flag } = getConfigs()

// proxy setting
export default function getProxyRoute() {
    var proxy_route = '';
    if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
        // React is running in dev mode.
        //proxy_route = 'http://localhost:5000'; //nothing likes proxy in package.json? 
        //proxy_route = 'http://127.0.0.1:5000';
        proxy_route = 'http://100.64.0.86:5000';
        //proxy_route = '/100.64.0.86:5000';
        //proxy_route = 'http://172.17.0.1:5000'; //docker
    }
    if (debug_flag) {
        console.log('env: '+process.env.NODE_ENV);
        console.log('route: '+proxy_route);
        }
    return proxy_route
}
