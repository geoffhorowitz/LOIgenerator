// System imports
import React, {useRef} from 'react'
import { useState, useEffect } from 'react';
import '../styles/loi.css'


// proxy setting
var proxy_route = '';
//console.log('env '+process.env.NODE_ENV);
if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
  // React is running in dev mode.
  proxy_route = 'http://localhost:5000'; //nothing likes proxy in package.json?
}

//assets folder reference
const ASSETS = '../../../assets/' //useless since doesn't like anything outside of src folder

async function get_prompt(){
    const response = await fetch(proxy_route + '/api/loi_generator', {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body:JSON.stringify({ 'placeholder': 'also_placeholder' }) //in JS, the dictionary key may not need to be a string?? but it shows up at string on the other end??
    });
    
    //console.log(response);
    const data = await response.json();
    //console.log(data);
    return data;
}

export default function LOIGenerator(props){
    const [loi_data, set_loi_data] = useState(null);

    async function handleSubmit(e) {
        return
    }
    /*
    async function get_prompt_wrapper() {
        return await get_prompt()
    }*/

    function get_prompt_wrapper(){
        fetch(proxy_route + '/api/loi_generator', {
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body:JSON.stringify({ placeholder: 'also_placeholder' })
        })
        .then(response => response.json())
        .then(text => {
            set_loi_data(text.loi_data);
            console.log(text.loi_data)});
    }

    useEffect(() => {
        get_prompt_wrapper();
    }, []);
    
    return (
        <>
            <div>
                <h2 className='center'>Congratulations! You've produced an LOI!</h2>
                <h4 className='center'>
                    Please see the LOI below. You can take this result and modify it for your own purposes or to use your own voice.
                    <br></br>
                    Like what you see? Generosity Genius can help optimize your grant management process using AI solutions that fit your organization.
                    <br></br>Contact us at generositygenius.org!
                </h4>
                <p className="preserve-line-breaks text-container">
                    {loi_data}
                </p>
            </div>
        </>
    )
}