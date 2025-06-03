import React from 'react';
import TodoList from './components/TodoList';

const App: React.FC = () => {
  return (
    <div style={{ maxWidth: '600px', margin: '2rem auto', fontFamily: 'Arial, sans-serif' }}>
      <h1>My Todo App</h1>
      <TodoList />
    </div>
  );
};

export default App;

