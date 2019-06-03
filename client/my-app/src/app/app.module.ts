import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavComponent } from './nav/nav.component';
import { HomeComponent } from './home/home.component';
import { AddComponent } from './add/add.component';
import { PlayerItemComponent } from './player-item/player-item.component';
import { AddPlayerComponent } from './add-player/add-player.component';
import { GameItemComponent } from './game-item/game-item.component';
import { AddGameComponent } from './add-game/add-game.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from "./material.module";

@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    HomeComponent,
    AddComponent,
    PlayerItemComponent,
    AddPlayerComponent,
    GameItemComponent,
    AddGameComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule, 
    FormsModule, BrowserAnimationsModule, 
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
