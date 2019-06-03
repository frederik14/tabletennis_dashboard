import {MatInputModule, MatFormFieldModule} from '@angular/material';
import { NgModule } from '@angular/core';

@NgModule({
  imports: [MatInputModule, MatFormFieldModule],
  exports: [MatInputModule, MatFormFieldModule],
})
export class MaterialModule { }