import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { GameService } from '../../services/game.service';

@Component({
  selector: 'app-ranking',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './ranking.html'
})
export class RankingComponent {

  ranking: any[] = [];

  constructor(private gameService: GameService) {}

  ngOnInit() {
    this.gameService.getRanking().subscribe((res: any) => {
      this.ranking = res;
    });
  }
}