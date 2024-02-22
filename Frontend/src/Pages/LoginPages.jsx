import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';

const LoginPage = () => {
  const { loginWithRedirect, logout, isAuthenticated, user } = useAuth0();

  return (
    <div>
      <h1>Página de Login</h1>

      {isAuthenticated ? (
        // Se o usuário estiver autenticado, mostra os dados do usuário e o botão de logout
        <>
          <p>Bem-vindo, {user.name}!</p>
          <button onClick={() => logout()}>Logout</button>
        </>
      ) : (
        // Se o usuário não estiver autenticado, mostra o botão de login
        <button onClick={() => loginWithRedirect()}>Login com Auth0</button>
      )}
    </div>
  );
};

export default LoginPage;













































/*import React from "react";
import { Auth0Provider, useAuth0 } from "@auth0/auth0-react";
import auth0 from 'auth0-js';

// Inicialização do Auth0
var webAuth = new auth0.WebAuth({
  domain: 'dev-flpjat1olkfrxgne.eu.auth0.com',
  clientID: 'YiH6Rz3NBCHV1hcPaE8nh2w7HzA8hWhU'
});

// Componente funcional para a página de login
const LoginPage = () => {
  const { loginWithRedirect, logout, isAuthenticated, user } = useAuth0();

  // Renderiza o formulário de login
  return (
    <div>
      <h1>Página de Login</h1>

      {isAuthenticated ? (
        // Se o usuário estiver autenticado, mostra os dados do usuário e o botão de logout
        <>
          <p>Bem-vindo, {user.name}!</p>
          <button onClick={() => logout()}>Logout</button>
        </>
      ) : (
        // Se o usuário não estiver autenticado, mostra o botão de login
        <button onClick={() => loginWithRedirect()}>Login com Auth0</button>
      )}
    </div>
  );
};

// Componente principal que envolve a aplicação com Auth0Provider
const AppWithAuth = () => {
  return (
    <Auth0Provider
      domain="dev-flpjat1olkfrxgne.eu.auth0.com"
      clientId="YiH6Rz3NBCHV1hcPaE8nh2w7HzA8hWhU"
      redirectUri={window.location.origin}
    >
      <LoginPage />
    </Auth0Provider>
  );
};

// Exporta o componente principal para uso em outros lugares
export default AppWithAuth;
*/