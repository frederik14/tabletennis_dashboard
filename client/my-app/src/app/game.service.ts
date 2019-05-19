import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Game } from '../models/game';

const http_options = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  })
}

@Injectable({
  providedIn: 'root'
})
export class GameService {
  url:string = 'http://localhost:5000/games'

  constructor(private http:HttpClient) { }

  //Get Games
  getGames():Observable<Game[]> {
    return this.http.get<Game[]>(this.url);
  }

  //Add new Game
  addGame(game:Game):Observable<any> {
    return this.http.post<any>(this.url, game, http_options) 
  }

  //Delete Game
  deleteGame(game:Game):Observable<any> {
    return this.http.delete<any>(this.url+'/'+game.id, http_options) 
  }
  

  //Set game result
  setGameResult(game:Game):Observable<any> {
    console.log(game)
    return this.http.put<any>(this.url, game, http_options) 
  }
}