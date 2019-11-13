import React, { Component } from 'react';
import './App.css';

class App extends Component {
  state = {
    todos: []
  }
  componentDidMount() {
    fetch('http://localhost:5000/teilnehmer')
    .then(res => res.json())
    .then((data) => {
      this.setState({ todos: data })
      console.log(this.state.todos)
    })
    .catch(console.log)
  }
  // [...]
  
  render() {

    return (
       <div className="container">
        <div className="col-xs-12">
        <h1>Meine Todos</h1>
        {this.state.todos.map((todo) => (
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">{todo.name}</h5>
			  <h5 className="card-title">{todo.yob}</h5>                                     
            </div>
          </div>
        ))}
        </div>
       </div>
    );
  }
  
}

export default App;
