// System imports
import React from 'react'
import { useState, useEffect } from 'react';
import axios from 'axios';

// Local imports
import QuestionDisplay from './QuestionDisplay';

// proxy setting
var proxy_route = '';
console.log('env '+process.env.NODE_ENV);
if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
  // React is running in dev mode.
  proxy_route = 'http://localhost:5000'; //nothing likes proxy in package.json?
}


async function get_question(endpoint_val, question_ndx) {
    //console.log('requesting question from '+proxy_route+'/api/'+endpoint_val+' with question ndx: '+question_ndx);
    /*const response = await axios.get(proxy_route+'/api/'+endpoint_val, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body:JSON.stringify({question_ndx})
    });*/
    const response = await fetch(proxy_route + '/api/'+endpoint_val, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body:JSON.stringify({question_ndx})
    });
    
    //console.log(response);
    const data = await response.json();
    //console.log(data);
    return data.question;
}

async function submitAnswer(answer_dict){
    console.log('submitting answers to /api/submit_answer')
    //const response = await axios.get(proxy_route+'/api/question');
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
    //return data.next_route;
}

export default function QABlock(props){
    // get inputs
    const {question_ndx, endpoint_val, updateDict} = props;

    // set up variables
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');
    //console.log('question_ndx: '+question_ndx)

    // maybe don't need
    const [error, setError] = useState(null);
    const [status, setStatus] = useState('typing');

    // set up functions
    async function getQuestion(endpoint_val) {
        setStatus('submitting');
        try {
            setQuestion( await get_question(endpoint_val, question_ndx));
            setStatus('success');
        } catch (err) {
            setStatus('typing');
            setError(err);
        }
    }

    function handleTextareaChange(e) {
        setAnswer(e.target.value);
        updateDict(question_ndx, answer);
    }

    useEffect(() => {
        //console.log('getting the question '+question_ndx+' from the server')
        getQuestion(endpoint_val);
        //console.log('done. response: '+question)
    }, [])

    return (
        <div>
            <h4>
                <QuestionDisplay question={question} />
            </h4>
            <textarea
                style={{
                    height: '50px',
                    width: '800px',
                  }}
                value={answer}
                onChange={handleTextareaChange}
                disabled={status === 'submitting'}
            />
            <br />
        </div>
    )
}