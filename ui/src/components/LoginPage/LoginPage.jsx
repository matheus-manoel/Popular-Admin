import React, { Component } from 'react';
import styled from 'styled-components';
import {
  Paper,
  FormControl,
  Input,
  Button,
  InputAdornment,
  LinearProgress
} from '@material-ui/core';
import { Email, Lock } from '@material-ui/icons';
import { firebaseConnect } from 'react-redux-firebase';

import logo from '../../images/logo.jpg';


const FormContainer = styled(Paper)`
  width: 230px;
  height: 380px;
  padding: 40px;
  border-left: 5px solid red;
`;

const CustomLogo = styled.img`
  width: 150px;
  height: 200px;
  margin-bottom: 20px;
`;

const FormContainerWrapper = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  height: 100%;
`;

const CustomLinearProgress = styled(LinearProgress)`
  margin-top: 10px;
`;

class LoginPage extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: '',
      password: '',
      loading: false,
    };
  }

  _handleEmailChange = event => {
    this.setState({ email: event.target.value });
  }

  _handlePasswordChange = event => {
    this.setState({ password : event.target.value });
  }

  _handleLogin = () => {
    const { firebase } = this.props;
    const { email, password } = this.state;

    this.setState({ loading: true });
    firebase.login({ email, password })
      .then(a => {
        this.setState({ loading: false });
      })
      .catch(e => {
        this.setState({ loading: false });
      });
  }

  render() {
    const { email, password, loading } = this.state;
    console.log(loading);
    return (
        <FormContainerWrapper>
          <FormContainer>
            <CustomLogo src={logo} alt="CPLB" />
            <FormControl>
              <Input
                id="email-simple"
                placeholder="Email"
                value={email}
                onChange={this._handleEmailChange}
                style={{
                  marginBottom: '10px',
                }}
                startAdornment={
                  <InputAdornment position="start">
                    <Email />
                  </InputAdornment>
                }
              />
            </FormControl>
          <FormControl>
            <Input
              id="password-simple"
              placeholder="Senha"
              value={password}
              onChange={this._handlePasswordChange}
              type="password"
              style={{
                marginBottom: '40px',
              }}
              startAdornment={
                <InputAdornment position="start">
                  <Lock />
                </InputAdornment>
              }
            />
            {!loading ? ( 
              <Button
                variant="raised"
                color="primary"
                onClick={this._handleLogin}
              >
                Entrar
              </Button>
            ) : (
              <CustomLinearProgress />
            )}
          </FormControl>
        </FormContainer>
      </FormContainerWrapper>
    );
  }
}

export default firebaseConnect()(LoginPage);
