import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Player } from '../models/player';

const http_options = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class PlayerService {
  players_url:string = 'http://localhost:5000/players'

  constructor(private http:HttpClient) { }

  //Get Players
  getPlayers():Observable<Player[]> {
    return this.http.get<Player[]>(this.players_url);
  }

  //Add new Player
  addPlayer(player:Player):Observable<any> {
    return this.http.post<any>(this.players_url, player, http_options) 
  }
}
