import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Game } from '../../models/game';

@Component({
  selector: 'app-game-item',
  templateUrl: './game-item.component.html',
  styleUrls: ['./game-item.component.scss']
})
export class GameItemComponent implements OnInit {
  @Input() game: Game;
  @Output() setGameResult: EventEmitter<any> = new EventEmitter();
  @Output() deleteGame:EventEmitter<any> = new EventEmitter();

  home_sets:Number = 0;
  out_sets:Number = 0;
  is_shown:Boolean = false;

  constructor() { }

  ngOnInit() {
  }

  onSubmit() {
    const game_result = {
      id: this.game.id,
      home_sets: this.home_sets,
      out_sets: this.out_sets,
    }
    this.setGameResult.emit(game_result)
  }

  onDelete() {
    const game_id = {
      id: this.game.id,
    }
    this.deleteGame.emit(game_id)
  }

  onGameClick() {
    this.is_shown = !this.is_shown
  }
}
