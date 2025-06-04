import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api/todos';

export const getTodos = async () => {
  const response = await axios.get(API_BASE_URL);
  return response.data;
}; 


export const addTodo = async (title: string) => {
  const response = await axios.post(API_BASE_URL, { title });
  return response.data;
};

export const updateTodo = async (id: number, updatedFields: object) => {
  const response = await axios.patch(`${API_BASE_URL}/${id}`, updatedFields);
  return response.data;
};

export const deleteTodo = async (id: number) => {
  await axios.delete(`${API_BASE_URL}/${id}`);
};
