import React from 'react';
import TodoList from './components/TodoList';
import ErrorBoundary from './components/ErrorBoundary';
import { Container, IconButton, Typography } from '@mui/material';
import { Brightness4, Brightness7 } from '@mui/icons-material';

interface AppProps {
  darkMode: boolean;
  toggleTheme: () => void;
}

const App: React.FC<AppProps> = ({ darkMode, toggleTheme }) => {
  return (
    <ErrorBoundary>
      <div 
	style={{ 
	  maxWidth: '600px', 
	  margin: '2rem auto', 
	  fontFamily: 'Arial, sans-serif' }}>

	<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h1>My Todo App</h1>
	  <IconButton onClick={toggleTheme} color="inherit">
	    {darkMode ? <Brightness7 /> : <Brightness4 />}
	  </IconButton>
	</div>
        <TodoList />
      </div>
    </ErrorBoundary>
  );
};

export default App;

