import React, { useState, useEffect } from 'react';
import TodoItem from './TodoItem';
import AddTodoForm from './AddTodoForm';
import { getTodos, addTodo, updateTodo, deleteTodo as deleteTodoApi} from '../services/todoService';

interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

const TodoList: React.FC = () => {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

useEffect(() => {
  const fetchData = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getTodos();
      setTodos(data);
    } catch (err) {
      console.error('Failed to fetch todos:', err);
      setError('Failed to load todos. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  fetchData();
}, []);


  const toggleTodo = async (id: number, completed: boolean) => {
  try {
    const updated = await updateTodo(id, { completed });
    setTodos(prev =>
      prev.map(todo =>
        todo.id === id ? updated : todo
      )
    );
  } catch (err) {
    console.error('Failed to update todo:', err);
  }
};


const deleteTodo = async (id: number) => {
  try {
    await deleteTodoApi(id);
    setTodos(prev => prev.filter(todo => todo.id !== id));
  } catch (err) {
    console.error('Failed to delete todo:', err);
  }
};

const handleAddTodo = async (title: string) => {
  try {
    const newTodo = await addTodo(title);
    setTodos(prev => [newTodo, ...prev]); // ← TypeScript error
  } catch (err) {
    console.error('Failed to add todo:', err);
  }
};

  return (
    <div>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {!loading && (
        <>
          <h2>Todo List</h2>

          <AddTodoForm onAdd={handleAddTodo} />

          {todos.map(todo => (
            <TodoItem
              key={todo.id}
              todo={todo}
              onToggle={toggleTodo}
              onDelete={deleteTodo}
            />
          ))}
        </>
      )}
    </div>
  );
};

export default TodoList;