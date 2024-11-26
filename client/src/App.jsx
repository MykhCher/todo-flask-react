import { useEffect, useState } from 'react';
// =====
import api from './api';
import './App.css'

function App() {

  const [ todoList, setTodoList ] = useState([]);
  const [ formTitle, setFormTitle ] = useState('');

  useEffect(() => {
    api.get('/todo')
      .then(({ data }) => {
        if(data[0]) {
          setTodoList(data);
        }
      })
      .catch(err => console.log(err))
  }, [])

  const createTodo = (title) => {
    if (title) {
      api.post('/todo', { title }, { headers: {'Content-Type': 'application/json'} })
        .then(({ data: { id, title } }) => {
          setTodoList(prevState => [...prevState, { id, title }]);
        })
        .catch(err => console.log(err))
      setFormTitle('');
    }
  }

  const deleteTodo = (id) => {
    api.delete(`/todo/${id}`)
      .then(({ data }) => {
        if (data) {
          const newList = todoList.filter(todo => todo.id !== id);
          setTodoList(newList);
        }
      })
      .catch(err => console.log(err))
  }

  const deleteAllTodo = (e) => {
    e.preventDefault();
    setTodoList([]);
  }

  return (
    <>
      <h1>Todo List</h1>
      <div className="card">
        <ul>
          {todoList.map(({ title, id }) => (
            <li key={id}>
              {title} 
              <span onClick={() => {deleteTodo(id)}}>
                X
              </span>
            </li>))}
        </ul>
        <form>
          <input 
            type="text" 
            name='title' 
            value={formTitle}
            onChange={e => {
              setFormTitle(e.target.value)
            }}
          />
          <button 
            type='submit' 
            onClick={e => {
              e.preventDefault();
              createTodo(formTitle)
            }}
          >
            Submit
          </button>
          <button onClick={deleteAllTodo}>
            Clear all
          </button>
        </form>
      </div>
    </>
  )
}

export default App;
