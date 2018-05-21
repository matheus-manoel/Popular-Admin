import React, { Component } from 'react';
import styled from 'styled-components';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

import  bgImage from './images/bg.png';
import './App.css';
import LoginPage from './components/LoginPage';


const AppContent = styled.div`
  background-image: url(${bgImage});
  background-size: cover;
  position: absolute;
  width: 100% !important;
  height: 100% !important;
`;

const theme = createMuiTheme({
  palette: {
    primary: {
      light: '#f05545',
      main: '#b71c1c',
      dark: '#7f0000',
      contrastText: '#fff',
    },
    secondary: {
      light: '#ff7961',
      main: '#f44336',
      dark: '#ba000d',
      contrastText: '#000',
    },
  },
});

class App extends Component {
  render() {
    return (
      <MuiThemeProvider theme={theme}>
        <AppContent className="App">
          <LoginPage />
        </AppContent>
      </MuiThemeProvider>
    );
  }
}

export default App;
