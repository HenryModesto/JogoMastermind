import { CanActivateFn, Router } from '@angular/router';

export const authGuard: CanActivateFn = () => {
  const isLogged = !!localStorage.getItem('token');

  if (!isLogged) {
    alert('Você precisa estar logado!');
    return false;
  }

  return true;
};