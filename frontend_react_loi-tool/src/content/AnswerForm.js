// System imports
import React from 'react'
//import ReactDOM from 'react-dom';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

// Local imports
import QABlock from './QABlock';
//import useFormStatus from '../helpers/useFormStatus.js';
import submitForm from '../helpers/SubmitForm';


export default function AnswerForm({endpoint_val, n_questions}){
    // maybe don't need
    const [error, setError] = useState(null);
    const [status, setStatus] = useState('typing');
    //const {formStatus, setFormStatus} = useFormStatus();
    //setFormStatus(endpoint_val, status);

    //var n_questions = 0;
    var qaBlocks = [];
    const navigate = useNavigate();
    const submission_dict = {'endpoint': endpoint_val}
    const answer_dict = {}

    async function handleSubmit(e) {

        e.preventDefault();
        setStatus('submitting');
        //setFormStatus(endpoint_val, status);
        console.log('answer dict vals:')
        for (let i in answer_dict) {
            console.log(`${i}: ${answer_dict[i]}`);
        }
        //const fake_answer = {'endpoint': endpoint_val, 'question_ndx': 1, 'answer': 5}
        submission_dict['answer_dict'] = answer_dict;
        try {
            const next_route = await submitForm(submission_dict);
            //const next_route = '/'
            setStatus('success');
            //setFormStatus(endpoint_val, status);
            console.log('submission success, next route: '+next_route)
            navigate(next_route); 
            window.location.reload(); //without this, the form doesn't request the new questions....maybe better soln?
        } catch (err) {
            setStatus('typing');
            setError(err);
            console.log('submission failed')
        }
    }

    const handleTextChange = (q_ndx, val) => {
        answer_dict[q_ndx] = val;
        //console.log(answer_dict[q_ndx])
    }

    /*useEffect(() => {
        //console.log('getting the questions from the server')
        //jsx_questions = getNumQs(endpoint_val);
        //n_questions = 11;//getNumQs(endpoint_val);
        //console.log('n_questions: '+n_questions)
        console.log('n_questions: '+n_questions)
        for (let i = 0; i < n_questions; i++){
            const elem = <QABlock question_ndx={i} endpoint_val={endpoint_val} updateDictFcn={handleTextChange}/>;
            qaBlocks.push(<div key={i}>{elem}</div>);
        }
    }, [])*/

    //const n_questions = await get_num_questions(endpoint_val); //async but doesn't return n_questions appropriately since this function is not async
    console.log('n_questions: '+n_questions)
    for (let i = 0; i < n_questions; i++){
        const elem = <QABlock question_ndx={i} endpoint_val={endpoint_val} updateDictFcn={handleTextChange}/>;
        qaBlocks.push(<div key={i}>{elem}</div>);
    }
    

    return (
        <form onSubmit={handleSubmit}>
            <div>{qaBlocks}</div>
            <br />
            <button 
                className="large-centered-button"
                disabled={
                //answer.length === 0 ||
                status === 'submitting'
                }>
                Submit
            </button>
            {error &&
                <p className="Error">{error.message}</p>
            }
        </form>
    )
}

