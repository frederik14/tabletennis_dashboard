import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-add-game',
  templateUrl: './add-game.component.html',
  styleUrls: ['./add-game.component.scss']
})
export class AddGameComponent implements OnInit {
  @Output() addGame: EventEmitter<any> = new EventEmitter();

  home_player:string;
  out_player:string;

  constructor() { }

  ngOnInit() {
  }

  onSubmit() {
    const game = {
      home_player: this.home_player,
      out_player: this.out_player,
    }

    this.addGame.emit(game)
  }
}