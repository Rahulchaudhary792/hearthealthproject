import { useState } from 'react'
import Modal from 'react-modal'
import './App.css'
function App() {
  const [age, setAge] = useState(0);
  const [bp, setBp] = useState(0);
  const [chol, setChol] = useState(0);
  const [sugarTest, setSugarTest] = useState(false);
  const [hr, setHr] = useState(0);
  const [ca, setCa] = useState(0);
  const [chestPain, setChestPain] = useState('normal');
  const [data, setData] = useState(false);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const openModal = () => {
   setModalIsOpen(true);
  };
  const closeModal = () => {
   setModalIsOpen(false);
  };
  const handleSubmit = async (e) => {
     e.preventDefault();
     const response = await fetch('http://127.0.0.1:5000/submit', {method:'POST',
            body: JSON.stringify({
            'age': age,
            'bp': bp,
            'chol': chol,
            'sugarTest': sugarTest,
            'hr': hr,
            'ca': ca,
            'chestPain': chestPain          
            }),
            headers: {
               'Content-Type': 'application/json'
            }
         });
         const dat = await response.json();
         setData(dat)
         openModal();
  }
  return (
    <>
       <div>
           <div className="heading">
              <h2>Heart Health Predictor</h2>
           </div>
           <form className="form-div">
              <div>
                   <label className="label-item">Enter your age</label>
                <div className="input-div">
                   <input type="text" name="age" onChange={(e) => setAge(e.target.value)}/>
                </div>
              </div>
              <div>
                <label className="label-item">Enter your blood pressure (BP)</label>
                <div className="input-div">
                   <input type="text" name="bp" onChange={(e) => setBp(e.target.value)}/>
                </div>
              </div>
              <div>
                <label className="label-item">Enter your cholestrol level</label>
                <div className="input-div">
                   <input type="text" name="chol" onChange={(e) => setChol(e.target.value)}/>
                </div>
              </div>
              <div>
                <label className="label-item">Have the doctor conducted fasting blood sugar test?</label>
                <div className="input-div">
                   <select name="sugearTest" onChange={(e) => setSugarTest(e.target.value)}>
                       <option defaultChecked>select</option>
                       <option>Yes</option>
                       <option>No</option>
                   </select>
                </div>
              </div>
              <div>
                <label className="label-item">Enter your maximum heart rate</label>
                <div className="input-div">
                   <input type="text" name="hr" onChange={(e) => setHr(e.target.value)}/>
                </div>
              </div>
              <div>
                <label className="label-item">Enter the amount of calcium in your body</label>
                <div className="input-div">
                   <input type="text" name="ca" onChange={(e) => setCa(e.target.value)}/>
                </div>
              </div>
              <div>
                <label className="label-item">What type of chest pain you have?</label>
                <div className="input-div">
                   <select name="chestPain" onChange={(e) => setChestPain(e.target.value)}>
                       <option defaultChecked>select</option>
                       <option>typical</option>
                       <option>asymptomatic</option>
                       <option>nonanginal</option>
                       <option>nontypical</option>
                       <option>fixed</option>
                       <option>normal</option>
                       <option>reversable</option>
                   </select>
                </div>
              </div>
              <div className="submit-button">
                <button className="button-item" onClick={handleSubmit}>submit</button>
              </div>
           </form>
           <Modal isOpen={modalIsOpen} 
            onRequestClose={closeModal}
            contentLabel="Example Modal">
               <h2>{data.result ? 'true' : 'false'}</h2>
               <button onClick={closeModal}>Close Modal</button>
            </Modal>
       </div>
    </>
  )
}

export default App
