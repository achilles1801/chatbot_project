import React, {useState} from 'react';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState(null);

  const handleClick = () => {
    fetch('http://127.0.0.1:5000/chat',{
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        message: input
      })
    })
    .then(response => {
      if (response.headers.get('content-type').includes('application/json')) {
        return response.json();
      } else {
        throw new Error('Server response was not in JSON format');
      }
    })
      .then(data => {
        setResponse(data.reply);
      });
  };

  return (

  
    <div className="App">
      <header className="App-header">
      <input type="text" value={input} onChange={e => setInput(e.target.value)} />
        <button onClick={handleClick}>Send</button>
        {response && <p>{response}</p>}
      </header>
    </div>
  );
}
export default App;
