import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Player } from '../models/player';

const http_options = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    "Access-Control-Allow-Methods": "DELETE, POST, GET, OPTIONS"
  })
}

@Injectable({
  providedIn: 'root'
})
export class PlayerService {
  player_url:string = 'http://localhost:5000/players'

  constructor(private http:HttpClient) { }

  //Get Players
  getPlayers():Observable<Player[]> {
    return this.http.get<Player[]>(this.player_url);
  }

  //Add new Player
  addPlayer(player:Player):Observable<any> {
    return this.http.post<any>(this.player_url, player, http_options) 
  }

  //Delete Game
  deletePlayer(player:Player):Observable<any> {
    return this.http.delete<any>(this.player_url+'/'+player.id, http_options) 
  }
}
