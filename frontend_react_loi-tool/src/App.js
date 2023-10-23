// App.js

// System imports
import { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
//import ReactDOM from 'react-dom';
//import axios from 'axios';

// Local imports
import HomePage from './content/HomePage';
import AnswerForm from './content/AnswerForm';
import LOIGenerator from './content/Llm_plugin';
//import useFormStatus from './helpers/useFormStatus.js';

// style imports
import './styles/form.css'
//import './stles/App.css';


export default function App() {

    // main
    /*useEffect(() => {
        getQuestion();
        console.log('calling initial question retrieval api, result: '+question)
    }, [])*/
    /*const [form1Status, setForm1Status] = useState('');
    const [form2Status, setForm2Status] = useState('');
    const [form3Status, setForm3Status] = useState('');
    const [form4Status, setForm4Status] = useState('');*/

    //const {formStatus, setFormStatus} = useFormStatus();

    const form1 = 'org_questions'
    const form1_text = 'Organization Questions'
    const n_questions1 = 11;
    //const form1_obj = AnswerForm({endpoint_val: form1, n_questions: n_questions1, status: form1Status, setStatus: setForm1Status});
    //const form1_obj = AnswerForm({endpoint_val: form1, n_questions: n_questions1});

    const form2 = 'foundation_questions'
    const form2_text = 'Foundation Questions'
    const n_questions2 = 2;
    //const form2_obj = AnswerForm({endpoint_val: form2, n_questions: n_questions2});

    const form3 = 'project_questions'
    const form3_text = 'Project Questions'
    const n_questions3 = 7;
    //const form3_obj = AnswerForm({endpoint_val: form3, n_questions: n_questions3});

    const form4 = 'additional_questions'
    const form4_text = 'Additional Questions'
    const n_questions4 = 1;
    //const form4_obj = AnswerForm({endpoint_val: form4, n_questions: n_questions4});

    const form5 = 'loi_generator'
    const form5_text = 'LOI Generator'

    var current_object, current_form_text;
    //current_object = form1_obj;
    current_form_text = form1_text;
    
    /*for (const key in formStatus) {
      console.log(`${key}: ${formStatus[key]}`);
    }*/
    //console.log('form1: '+form1Status)
  

    /*if(form1_obj.status !== 'success'){
      current_object = form1_obj;
      current_form_text = form1_text;
    } else if (form2_obj.status !== 'success') {
      current_object = form2_obj;
      current_form_text = form2_text;
    } else if (form3_obj.status !== 'success') {
      current_object = form3_obj;
      current_form_text = form3_text;
    } else {
      current_object = form4_obj;
      current_form_text = form4_text;
    }*/

    return (
      <>
        <h1 className='center'>LOI Generation</h1>
        <BrowserRouter>
            <Routes>
            <Route path="/" element={
                <>
                  <div className='center'>
                    <HomePage />
                  </div>
                </>
              } />
              <Route path="/org_questions" element={
                <>
                  <h3 className='center'>{form1_text}</h3>
                  <div className='center'>
                    <AnswerForm endpoint_val={form1} n_questions={n_questions1}/>
                  </div>
                </>
              } />
              <Route path="/foundation_questions" element={
                <>
                  <h3 className='center'>{form2_text}</h3>
                  <div className='center'>
                    <AnswerForm endpoint_val={form2} n_questions={n_questions2}/>
                  </div>
                </>
              } />
              <Route path="/project_questions" element={
                <>
                  <h3 className='center'>{form3_text}</h3>
                  <div className='center'>
                    <AnswerForm endpoint_val={form3} n_questions={n_questions3}/>
                  </div>
                </>
              } />
              <Route path="/additional_questions" element={
                <>
                  <h3 className='center'>{form4_text}</h3>
                  <div className='center'>
                    <AnswerForm endpoint_val={form4} n_questions={n_questions4}/>
                  </div>
                </>
              } />
              <Route path="/loi_generator" element={
                <>
                  <div className='center'>
                    <LOIGenerator />
                  </div>
                </>
              } />
            </Routes>
          </BrowserRouter>
        <br />
        <br />
        <br />
      </>
    );

    //{<AnswerForm endpoint_val={form1} n_questions={n_questions1}/>}
    //<AnswerForm endpoint_val={form2} n_questions={n_questions2}/>
    //<AnswerForm endpoint_val={form3} n_questions={n_questions3}/>
    /*return (
        <>
            <h1 className='center'>LOI Generation</h1>
            <h3 className='center'>{current_form_text}</h3>
            <div className='center'>
              {current_object}
            </div>
            <br />
            <br />
            <br />
        </>
    );*/
}
/*
ReactDOM.render(
  <Router>
    <Route exact path="/">
      <App />
    </Route>
    <Route path="/question/:id">
      <QuestionPage />
    </Route>
  </Router>,
  document.getElementById('root')
);*/
