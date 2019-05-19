import { Component, OnInit, Input, Output, EventEmitter} from '@angular/core';
import { Player } from '../../models/player';

@Component({
  selector: 'app-player-item',
  templateUrl: './player-item.component.html',
  styleUrls: ['./player-item.component.scss']
})
export class PlayerItemComponent implements OnInit {
  @Input() player: Player;
  @Output() deletePlayer: EventEmitter<any> = new EventEmitter();

  is_shown:Boolean = false;

  constructor() { }

  ngOnInit() {
  }

  onDelete() {
    const player_id = {
      id: this.player.id,
    }
    this.deletePlayer.emit(player_id)
  }

  onPlayerClick() {
    this.is_shown = !this.is_shown
  }
}
