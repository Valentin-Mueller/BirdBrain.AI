import './App.css';

function App() {
  function callApi() {
    fetch('http://localhost:8000/test', { method: 'GET' })
      .then((data) => data.json()) // Parsing the data into a JavaScript object
      .then((json) => alert(JSON.stringify(json))); // Displaying the stringified data in an alert popup
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>
          <button onClick={callApi}>Call API</button>
        </p>
      </header>
    </div>
  );
}

export default App;
