import React from 'react';
import TodoList from './components/TodoList';
import ErrorBoundary from './components/ErrorBoundary';

const App: React.FC = () => {
  return (
    <ErrorBoundary>
      <div style={{ maxWidth: '600px', margin: '2rem auto', fontFamily: 'Arial, sans-serif' }}>
        <h1>My Todo App</h1>
        <TodoList />
      </div>
    </ErrorBoundary>
  );
};

export default App;

