import React from 'react';
import { IconButton, Typography } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';

interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

interface TodoItemProps {
  todo: {
    id: number;
    title: string;
    completed: boolean;
  };
  onToggle: (id: number, completed: boolean) => void;
  onDelete: (id: number) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onDelete }) => {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: '0.5rem 0',
      borderBottom: '1px solid #ccc'
    }}>
      <Typography
        onClick={() => onToggle(todo.id, !todo.completed)}
        style={{
          textDecoration: todo.completed ? 'line-through' : 'none',
          cursor: 'pointer',
          flexGrow: 1
        }}
      >
        {todo.title}
      </Typography>
      <IconButton
        aria-label="delete"
        color="error"
        onClick={() => onDelete(todo.id)}
      >
        <DeleteIcon />
      </IconButton>
    </div>
  );
};

export default TodoItem;

