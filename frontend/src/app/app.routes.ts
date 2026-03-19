import { Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login';
import { GameComponent } from './pages/game/game.component';
import { RankingComponent } from './pages/ranking/ranking';

export const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'game', component: GameComponent },
  { path: 'ranking', component: RankingComponent }
];