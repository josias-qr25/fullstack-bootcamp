import React from 'react';

jest.mock('./services/todoService', () => ({
  getTodos: jest.fn().mockResolvedValue([]), // or mock data
  addTodo: jest.fn().mockResolvedValue({}),
  updateTodo: jest.fn().mockResolvedValue({}),
  deleteTodo: jest.fn().mockResolvedValue({}),
}));

import { render, screen, waitFor } from '@testing-library/react';
import App from './App';
import * as todoService from './services/todoService';

jest.mock('./services/todoService');

test('renders todo list title', async () => {
  // Mock getTodos to resolve with fake data
  (todoService.getTodos as jest.Mock).mockResolvedValue([]);

  render(<App />);

  await waitFor(() => {
    expect(screen.getByText('My Todo App')).toBeInTheDocument();
  });
});

