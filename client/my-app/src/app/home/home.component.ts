import { Component, OnInit } from '@angular/core';
import { Player } from '../../models/player';
import { PlayerService } from '../player.service'
import { Game } from '../../models/game';
import { GameService } from '../game.service'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  players:Player[]
  games:Game[]
  constructor(private player_service:PlayerService, private game_service:GameService) { }

  ngOnInit() {
    this.player_service.getPlayers().subscribe(players => {
      console.log(players)
      this.players = players
    });
    this.game_service.getGames().subscribe(games => {
      console.log(games)
      this.games = games
    });
  }

  addPlayer(player:Player) {
    //Add to server
    this.player_service.addPlayer(player).subscribe(response => {
      console.log(response)
      //Add to UI
      this.players.push(response.data)
    });
  }

  addGame(game:Game) {
    //Add to server
    this.game_service.addGame(game).subscribe(response => {
      console.log(response)
      //Add to UI
      this.games.push(response.data)
    });
  }

  setGameResult(game:Game) {
    //Add to server
    this.game_service.setGameResult(game).subscribe(response => {
      console.log(response)
      //Add to UI
      this.games[this.games.findIndex(game => game.id === response.data.id)] = response.data
    });
  }
}
