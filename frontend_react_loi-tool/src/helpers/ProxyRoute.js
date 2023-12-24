//import React from 'react'

// proxy setting
export default function getProxyRoute() {
    var proxy_route = '';
    console.log('env '+process.env.NODE_ENV);
    if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
        // React is running in dev mode.
        //proxy_route = 'http://localhost:5000'; //nothing likes proxy in package.json?
        proxy_route = 'http://127.0.0.1:5000';
    }
    return proxy_route
}
