import { createStore, compose } from 'redux';
import rootReducer from './reducers';
import { reactReduxFirebase } from 'react-redux-firebase';
import firebase from 'firebase';


const fbConfig = {
  apiKey: 'AIzaSyBw_NVMq8FfnTx5mKoAuaQSyVd7QCmm9eE',
  authDomain: 'lima-barreto-sanca.firebaseapp.com',
  databaseURL: 'https://lima-barreto-sanca.firebaseio.com',
}

firebase.initializeApp(fbConfig);

const initialState = {};

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
export default createStore(
  rootReducer,
  initialState,
  composeEnhancers(
    reactReduxFirebase(firebase, {
      userProfile: 'users',
      enableLoggign: true,
    }),
  )
);
