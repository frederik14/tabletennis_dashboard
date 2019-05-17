import { Component, OnInit } from '@angular/core';
import { Player } from '../../models/player';
import { PlayerService } from '../player.service'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  players:Player[]
  constructor(private player_service:PlayerService) { }

  ngOnInit() {
    this.player_service.GetPlayers().subscribe(players => {
      this.players = players
    });
  }

  addPlayer(player:Player) {
    //Add to server
    this.player_service.addPlayer(player).subscribe(response => {
      console.log(response)
      //Add to UI
      this.players.push(response.player)
    })
  }

}
