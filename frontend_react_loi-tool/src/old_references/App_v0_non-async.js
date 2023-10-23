// App.js

// functional imports
import { useState, useEffect } from 'react';
import QuestionDisplay from './content/QuestionDisplay';
import AnswerInput from './content/AnswerInput';
import SubmitButton from './content/SubmitButton';
//import { BrowserRouter as Router, Route } from 'react-router-dom';

// style imports
import './styles/form.css'

/*function get_question(){
  fetch('/api/question')
    .then(res => res.json())
    //.then(res => {console.log(res.question)})
    .then(res => {return res.question})
    //.then(data => setQuestion(data.question))
    //.then(data => {return data.question});
}*/

async function get_question() {
  const response = await fetch('/api/question');
  const data = await response.json();
  return data.question;
}

function submit_answer(answer) {
  //console.log('attempting to submit: '+answer)
  fetch('/api/submit_answer', {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json',
    },
    body: JSON.stringify({ answer }),
  })
  .then(res => res.json())
  //.then(get_question())
}

function submitForm(answer) {
  // Pretend it's hitting the network.
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      //let shouldError = answer.toLowerCase() !== 'lima'
      let shouldError = submit_answer(answer)
      if (shouldError) {
        reject(new Error('Good guess but a wrong answer. Try again!'));
      } else {
        resolve();
      }
    }, 1500);
  });
}

export default function App() {
  // set up variables
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  // maybe don't need
  const [error, setError] = useState(null);
  const [status, setStatus] = useState('typing');

  // set up functions
  async function getQuestion() {
    /*const bob = get_question();
    console.log('response1: '+bob)
    setQuestion(bob);*/
    setStatus('submitting');
    try {
      const bob = await get_question();
      setStatus('success');
      setQuestion(bob)
    } catch (err) {
      setStatus('typing');
      setError(err);
    }
  }

  /*const submit_answer = () => {
    fetch('/api/submit_answer', {
      method: 'POST',
      //body: JSON.stringify({ answer })
      body: JSON.stringify("Bob")
    })
    .then(res => res.json())
  }*/

  /*const handleSubmit = () => {
    console.log('attempting to handle submit')

    fetch('/api/submit_answer', {
      method: 'POST',
      //body: JSON.stringify({ answer })
      body: JSON.stringify("Bob")
    })
    .then(res => res.json())
    .then(data => {
      setQuestion(data.question);
      setAnswer('');
    })
    .then(console.log('handle submit complete'))
  }*/

  async function handleSubmit(e) {
    e.preventDefault();
    setStatus('submitting');
    try {
      await submitForm(answer);
      setStatus('success');
      getQuestion();
    } catch (err) {
      setStatus('typing');
      setError(err);
    }
  }

  function handleTextareaChange(e) {
    setAnswer(e.target.value);
  }

  // main
  useEffect(() => {
    getQuestion();
    //console.log('calling initial question retrieval api, result: '+question)
  }, [])

  return (
    <>
      <h1 className='center'>LOI Generation</h1>
      <div className='center'>
        <p>
          <QuestionDisplay question={question} />
        </p>
        <form onSubmit={handleSubmit}>
          <textarea
            value={answer}
            onChange={handleTextareaChange}
            disabled={status === 'submitting'}
          />
          <br />
          <button disabled={
            answer.length === 0 ||
            status === 'submitting'
          }>
            Submit
          </button>
          {error !== null &&
            <p className="Error">
              {error.message}
            </p>
          }
        </form>
      </div>
    </>
  );
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
