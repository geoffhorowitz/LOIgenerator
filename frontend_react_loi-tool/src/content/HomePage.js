// System imports
import React from 'react'
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

// Local imports
import submitForm from '../helpers/SubmitForm';


export default function HomePage({endpoint_val}){
    const [error, setError] = useState(null);
    const [status, setStatus] = useState('typing');
    const navigate = useNavigate();

    /*async function get_num_questions(endpoint) {
        console.log('requesting question from /api/num_questions')
        //const response = await axios.get(proxy_route+'/api/question');
        const response = await fetch(proxy_route + '/api/num_questions', {
                method:'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body:JSON.stringify({ endpoint })
            }
        );
        //console.log(response);
        const data = await response.json();
        //console.log(data);
        return (data.n_questions, data.next_route);
    }*/
    

    async function handleSubmit(e) {

        e.preventDefault();
        setStatus('submitting');
        try {
            const next_route = await submitForm({"endpoint": endpoint_val});
            setStatus('success');
            console.log('submission success, next route: '+next_route)
            navigate(next_route); 
            //window.location.reload(); //without this, the form doesn't request the new questions....maybe better soln?
        } catch (err) {
            setStatus('typing');
            setError(err);
            console.log('submission failed')
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <h2>Ready to begin the LOI generator?</h2>
            <br />
            <button 
                className="large-centered-button">
                Start Generating
            </button>
            {error &&
                <p className="Error">{error.message}</p>
            }
        </form>
    )
}

