import { Component, OnInit, Input} from '@angular/core';
import { Player } from '../../models/player';

@Component({
  selector: 'app-player-item',
  templateUrl: './player-item.component.html',
  styleUrls: ['./player-item.component.scss']
})
export class PlayerItemComponent implements OnInit {
  @Input() player: Player;

  constructor() { }

  ngOnInit() {
  }
}