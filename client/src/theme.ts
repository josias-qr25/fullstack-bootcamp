// client/src/theme.ts
import { createTheme } from '@mui/material/styles';
import { PaletteMode } from '@mui/material';

const getDesignTokens = (mode: PaletteMode) => ({
  palette: {
    mode,
    ...(mode === 'dark'
      ? {
          primary: {
            main: '#88C0D0', // Nord Frost — soft blue
          },
          background: {
            default: '#2E3440', // Polar Night
            paper: '#3B4252',   // Slightly lighter for cards
          },
          text: {
            primary: '#ECEFF4', // Snow Storm
          },
          secondary: {
            main: '#B48EAD', // Nord Aurora (purple)
          },
        }
      : {
          primary: {
            main: '#5E81AC', // Slightly darker for light mode
          },
          background: {
            default: '#f4f6f8',
            paper: '#ffffff',
          },
          text: {
            primary: '#1e1e1e',
          },
        }),
  },
});

export const darkTheme = createTheme(getDesignTokens('dark'));
export const lightTheme = createTheme(getDesignTokens('light'));

