// client/src/theme.ts
import { createTheme } from '@mui/material/styles';
import { PaletteMode } from '@mui/material';

const getDesignTokens = (mode: PaletteMode) => ({
  palette: {
    mode,
    ...(mode === 'light'
      ? {
          // Light mode colors
          primary: {
            main: '#5E81AC',
          },
          background: {
            default: '#f4f6f8',
            paper: '#ffffff',
          },
          text: {
            primary: '#1e1e1e',
          },
        }
      : {
          // Dark mode colors (Nord-ish)
          primary: {
            main: '#8FBCBB',
          },
          background: {
            default: '#2E3440',
            paper: '#3B4252',
          },
          text: {
            primary: '#ECEFF4',
          },
        }),
  },
});

export const darkTheme = createTheme(getDesignTokens('dark'));
export const lightTheme = createTheme(getDesignTokens('light'));

