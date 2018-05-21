import { createStore, compose } from 'redux';
import rootReducer from './reducers';
import { reduxFirebase } from 'react-redux-firebase';


const fbConfig = {
  apiKey: 'AIzaSyBw_NVMq8FfnTx5mKoAuaQSyVd7QCmm9eE',
  authDomain: 'lima-barreto-sanca.firebaseapp.com',
  databaseURL: 'https://lima-barreto-sanca.firebaseio.com',
}

export default function configureStore (initialState, history) {
  const createStoreWithMiddleware = compose(
    reduxFirebase(fbConfig, { userProfile: 'users' }),
    typeof window === 'object' && typeof window.devToolsExtension !== 'undefined' ? window.devToolsExtension() : f => f
  )(createStore);

  return createStoreWithMiddleware(rootReducer);
}
