import { render, screen, fireEvent } from '@testing-library/react';
import AddTodoForm from './AddTodoForm';

test('submits entered todo title', () => {
  const handleAdd = jest.fn(); // mock function
  render(<AddTodoForm onAdd={handleAdd} />);

  const input = screen.getByLabelText(/enter new todo/i);
  const button = screen.getByRole('button', { name: /add/i });

  fireEvent.change(input, { target: { value: 'Test task' } });
  fireEvent.click(button);

  expect(handleAdd).toHaveBeenCalledWith('Test task');
});
