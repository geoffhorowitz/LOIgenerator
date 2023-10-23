// System imports
import React from 'react'
import { useState, useEffect } from 'react';

// proxy setting
var proxy_route = '';
//console.log('env '+process.env.NODE_ENV);
if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
  // React is running in dev mode.
  proxy_route = 'http://localhost:5000'; //nothing likes proxy in package.json?
}

async function get_prompt(){
    const response = await fetch(proxy_route + '/api/loi_generator', {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body:JSON.stringify({ 'placeholder': 'also_placeholder' })
    });
    
    //console.log(response);
    const data = await response.json();
    //console.log(data);
    return data;
}

export default function LOIGenerator(props){
    const [prompt, setPrompt] = useState(null);

    async function handleSubmit(e) {
        return
    }

    async function get_prompt_wrapper() {
        return await get_prompt()
    }

    function get_prompt_wrapper(){
        fetch(proxy_route + '/api/loi_generator', {
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body:JSON.stringify({ 'placeholder': 'also_placeholder' })
        })
        .then(response => response.json())
        .then(text => {setPrompt(text.prompt); console.log(text.prompt)});
    }

    /*useEffect(() => {
        const prompt = get_prompt_wrapper()
        //const prompt = get_prompt();
        console.log(prompt);
        const bob = 'bob'
    }, []);*/

    /*const prompt = get_prompt_wrapper()
    //const prompt = get_prompt();
    console.log(prompt);
    */
    useEffect(() => {
        get_prompt_wrapper()
    }, []);
    const bob = 'bob';

    return (
        <>
            <div className='text-container'>
                <h2>You're reached....a placeholder</h2>
                <h4>
                    I'm your friendly LOI generator that will one day become a real boy....I mean have an LLM connected through an API and have a really good prompt that will get you the LOI you want!
                </h4>  
                <p>
                    In the meantime, I can tell you about some of the answers that I have access to from your input. These answers can be used in our prompt to provide you an awesome LOI!
                </p>
                <p>
                    {prompt}
                </p>
                <p>
                    One more thing we'll want to consider is how the formatting from the API will look....probably no formatting (as you can see even from sending the prompt above). How do we work with that?
                </p>
            </div>
        </>
    )
}