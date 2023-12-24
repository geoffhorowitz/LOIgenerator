// System imports
//import React from 'react'

// Local imports
import getProxyRoute from './ProxyRoute'

// // // SUBMIT BUTTON
/*function submit_answers(answer_dict) {
    //console.log('attempting to submit: '+answer_dict) 
    fetch(proxy_route+'/api/submit_answer', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answer_dict }),
    })
    .then(res => res.json())
    //.then(get_question())
}

function submitForm(answer_dict) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
        //let shouldError = answer.toLowerCase() !== 'lima'
        let shouldError = submit_answers(answer_dict)
        if (shouldError) {
            reject(new Error('There was an issue submitting this form. Please try again!'));
        } else {
            resolve();
        }
        }, 1500);
    });
}*/

export default async function submitForm(answer_dict){
    const proxy_route = getProxyRoute()
    console.log('proxy route: '+proxy_route)
    console.log('submitting answers to '+proxy_route+'/api/submit_answer')
    console.log(answer_dict)
    const response = await fetch(proxy_route + '/api/submit_answer', {
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body:JSON.stringify(answer_dict)
        }
    );
    //console.log(response);
    const data = await response.json();
    //console.log(data);
    console.log('next route'+data.next_route);
    return data.next_route;
}
