import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-add-player',
  templateUrl: './add-player.component.html',
  styleUrls: ['./add-player.component.scss']
})
export class AddPlayerComponent implements OnInit {
  @Output() addPlayer: EventEmitter<any> = new EventEmitter();

  name:string;

  constructor() { }

  ngOnInit() {
  }

  onSubmit() {
    const player = {
      name: this.name
    }

    this.addPlayer.emit(player)
  }
}
