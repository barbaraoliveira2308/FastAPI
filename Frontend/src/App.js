import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './Pages/LoginPages';
import { Auth0Provider, useAuth0 } from '@auth0/auth0-react';

function App() {
  const {
    loginWithPopup,
    loginWithRedirect,
    logout,
    user,
    isAuthenticated,
  } = useAuth0();

  return (
    <div>
      <Router>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          {/* Outras rotas da sua aplicação */}
        </Routes>
      </Router>

      <div>
        <ul>
          <li>
            <button onClick={loginWithPopup}>Login with Popup</button>
            <button onClick={loginWithRedirect}>Login with Redirect</button>
            <button onClick={logout}>Logout</button>
          </li>
        </ul>
        <h3>O usuário está {isAuthenticated ? 'logged in' : 'Not logged in'}</h3>
        {isAuthenticated && (
          <pre style={{ textAlign: 'start' }}>{JSON.stringify(user, null, 2)}</pre>
        )}
      </div>
    </div>
  );
}

function AppWithAuth() {
  return (
    <Auth0Provider
      domain="dev-flpjat1olkfrxgne.eu.auth0.com"
      clientId="wMGvU0ZhMRKOUj4ThJ6sFpAHIWQdMNjn"
      redirectUri={window.location.origin}
    
    >
      <App />
    </Auth0Provider>
  );
}

export default AppWithAuth;






















/*import React from 'react';
import { BrowserRouter as Router, Route, Redirect, Routes } from 'react-router-dom';
import LoginPage from './Pages/LoginPages'
import { useAuth0 } from '@auth0/auth0-react';


function App (){

 const {
   loginWithpopup,
   loginWithRedirect, 
   logout,
   user, 
   isAuthenticated,
   } = useAuth0()

 
 
  return (
  <div>
      <Router>
    <Routes>
      <Route path="/login" element={<LoginPage />} />
     
     


    </Routes>
  </Router>

  <div>
    <ul><li>
      <button onClick={loginWithpopup}>
       Login with Popup
      </button>
      <button onClick={loginWithRedirect}>
       Login with Redirect
      </button>
      <button onClick={logout}>
       logout
      </button>
    </li>
      </ul>
    <h3> O usuario esta {isAuthenticated? "logged in": "Not logged in"}</h3>
    {isAuthenticated && (
      <pre style={{textAling: 'start'}}> {JSON.stringify[user, null, 2]} </pre>
    )}
  </div>
  </div>

  
  )
}
 

export default App;
*/
/*

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './pages/login/LoginPages';
// Importe seus componentes de página


// Função para verificar a autenticação
const checkAuthentication = () => {
  const token = localStorage.getItem('authToken');
  return !!token;
};



const App = () => (
  <Router>
    <Routes>
      <Route path="/login" element={<LoginPage/>} />
      <ProtectedRoute path="/dashboard" element={<DashboardPage />} />
   
    </Routes>
  </Router>
);

ReactDOM.render(<App/>, document.getElementById('root'));
export default App;
*/