import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { GameService } from '../../services/game.service';

@Component({
  selector: 'app-game',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './game.html',
  styleUrls: ['./game.css']
})
export class GameComponent {

  user_id: number = 0;
  currentRow = 0;
  colors = ['r', 'b', 'g', 'y'];
  won = false;
  gameFinished = false;
  secretCode = '';

  board = Array(10).fill(null).map(() => ({
    guess: ['', '', '', ''],
    result: { black: 0, white: 0 }
  }));

  constructor(private gameService: GameService) {}

  ngOnInit() {
  const id = localStorage.getItem('user_id');

  if (!id) {
    alert('Usuário não logado!');
    return;
  }

    this.user_id = Number(id);
    this.startGame();
  }

  startGame() {
    this.gameService.startGame(this.user_id).subscribe({
      next: (res) => {
        console.log('Jogo iniciado', res);
      },
      error: (err) => {
        console.error('Erro ao iniciar jogo:', err);
      }
    });
  }

  selectColor(rowIndex: number, colIndex: number) {
    if (rowIndex !== this.currentRow || this.gameFinished) return;

    const current = this.board[rowIndex].guess[colIndex];
    const index = this.colors.indexOf(current);
    const next = (index + 1) % this.colors.length;

    this.board[rowIndex].guess[colIndex] = this.colors[next];
  }

  submitRow() {
  console.log('CLICOU ENVIAR');

  if (this.gameFinished) return;

  // 🚫 BLOQUEIO DE LIMITE
  if (this.currentRow >= this.board.length) {
    alert('Fim de jogo! Você usou todas as tentativas.');
    this.gameFinished = true;
    return;
  }

  const guess = this.board[this.currentRow].guess;

  if (guess.includes('')) {
    alert('Preencha todas as cores!');
    return;
  }

  const payload = {
    user_id: this.user_id,
    guess: guess.join('')
  };

  console.log('ENVIANDO:', payload);

  this.gameService.attempt(payload).subscribe({
    next: (res: any) => {
      console.log('RESPOSTA BACKEND:', res);

      this.board[this.currentRow].result.black = res.black;
      this.board[this.currentRow].result.white = res.white;

      if (res.finished) {
        this.gameFinished = true;
        this.secretCode = res.secret;
        this.won = res.won;
      }

      this.currentRow++;

      if (this.currentRow >= this.board.length) {
        this.gameFinished = true;
        alert('Fim de jogo! Você perdeu 😢');
      }
    },
    error: (err) => {
      console.error('ERRO NO BACKEND:', err);
      alert('Erro ao enviar tentativa');
    }
  });

  
}
}