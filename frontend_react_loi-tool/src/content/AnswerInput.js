// AnswerInput.js

const AnswerInput = ({answer, setAnswer}) => {

  const onChange = (e) => {
    setAnswer(e.target.value);
  }

  return (
    <input value={answer} onChange={onChange} />
  )

}

export default AnswerInput
