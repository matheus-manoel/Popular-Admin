import React, { Component } from 'react';
import styled from 'styled-components';
import {
  Paper,
  FormControl,
  Input,
  Button,
  InputAdornment
} from '@material-ui/core';
import { Email, Lock } from '@material-ui/icons';


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

class LoginPage extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: '',
      password: '',
    };
  }

  handleEmailChange = event => {
    this.setState({ email: event.target.value });
  }

  handlePasswordChange = event => {
    this.setState({ password : event.target.value });
  }

  render() {
    return (
        <FormContainerWrapper>
          <FormContainer>
            <CustomLogo src={logo} alt="CPLB" />
            <FormControl>
              <Input
                id="name-simple"
                placeholder="Email"
                value={this.state.email}
                onChange={this.handleEmailChange}
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
              id="name-simple"
              placeholder="Senha"
              value={this.state.password}
              onChange={this.handlePasswordChange}
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
            <Button variant="raised" color="primary">
              Entrar
            </Button>
          </FormControl>
        </FormContainer>
      </FormContainerWrapper>
    );
  }
}

export default LoginPage;
