import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  private API = 'http://127.0.0.1:5000/game';

  constructor(private http: HttpClient) {}

  startGame(user_id: number) {
    return this.http.post(`${this.API}/start`, { user_id });
  }

  attempt(data: { user_id: number, guess: string }) {
    return this.http.post(`${this.API}/attempt`, data);
  }

  getRanking() {
    return this.http.get(`${this.API}/ranking`);
  }
}