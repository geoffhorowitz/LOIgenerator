// QuestionDisplay.js

import React from 'react'
/*
async function get_question() {
  const response = await fetch('/api/question');
  const data = await response.json();
  return data.question;
}*/

function QuestionDisplay(props) {
  //return <h1>{props.question}</h1>
  return props.question
}

export default QuestionDisplay
