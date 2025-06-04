import React, { useState, FormEvent } from 'react';
import { TextField, Button, Box } from '@mui/material';

interface AddTodoFormProps {
  onAdd: (title: string) => void;
}

const AddTodoForm: React.FC<AddTodoFormProps> = ({ onAdd }) => {
  const [title, setTitle] = useState('');
  const [error, setError] = useState(false);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();

    if (!title.trim()) {
      setError(true);
      return;
    }

    setError(false);
    onAdd(title.trim());
    setTitle('');
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', gap: 2, mb: 3 }}>
      <TextField
        label="Enter new todo"
        variant="outlined"
        fullWidth
        value={title}
        onChange={e => setTitle(e.target.value)}
      />
      <Button type="submit" variant="contained" color="primary">
        Add
      </Button>
    </Box>
  );
};

export default AddTodoForm;
