// System imports
import React, {useRef} from 'react'
import { useState, useEffect } from 'react';
import Image from 'react-image';


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
        body:JSON.stringify({ 'placeholder': 'also_placeholder' }) //in JS, the dictionary key may not need to be a string?? but it shows up at string on the other end??
    });
    
    //console.log(response);
    const data = await response.json();
    //console.log(data);
    return data;
}

export default function LOIGenerator(props){
    const [prompt, setPrompt] = useState(null);
    const [image, setImage] = useState(null);
    const [im_w, setIm_w] = useState(null);
    const [im_h, setIm_h] = useState(null);

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
            body:JSON.stringify({ placeholder: 'also_placeholder' })
        })
        .then(response => response.json())
        .then(text => {
            setPrompt(text.prompt);

            // Extract bytes and metadata
            //const {bytes, size, mode} = text.image; 
            //const bytes = text.image;
            // Convert bytes to Uint8Array
            //const buffer = new Uint8Array(bytes); 

            
            //const img = document.getElementById( 'img' );
            //img.src = url;
            // in case you don't need the blob anymore
            //img.onload = e => URL.revokeObjectURL( url );

            //const base64data = Buffer.from(buffer).toString('base64')
            //const img = `data:${blob.type};blob,${blob}`

            //setImage(text.image.data);
            //setIm_w(size[0]); 
            //setIm_h(size[1]);
            console.log(text.prompt)});
            //console.log(image)
    }

    function get_image(){
        fetch(proxy_route + '/api/get_generated_image',{
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body:JSON.stringify({ placeholder: 'also_placeholder' })
        })
        .then(response => {
            console.log('image stuff:')
            //console.log(response);
            //const bytes = response.text();
            //const buffer = new Uint8Array(bytes)
            //console.log(buffer)
            // Create image blob
            //const blob = new Blob([buffer], {type: 'image/png'});
            const blob = response.blob();
            const url = URL.createObjectURL(blob);
            console.log(url)

            //const blob = response.blob();
            //const img = URL.createObjectURL(blob);
            //setImage(img)

            setImage(url);

        })
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
        get_prompt_wrapper();
        //get_image();
    }, []);
    
    /*         {image && <img src={image} width={im_w} height={im_h}/>}
                */

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
                <br />
                <h4>To simulate a call to an LLM, lets use the provided mission statement to generate a image!</h4>
                {image && <img src={image}/>}
            </div>
        </>
    )
}