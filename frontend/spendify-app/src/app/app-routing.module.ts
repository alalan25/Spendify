import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DashComponent } from './dash/dash.component';
import { Dash2Component } from './dash2/dash2.component';
import { Dash3Component } from './dash3/dash3.component';

const routes: Routes = [
  { path: 'Account1', component: DashComponent },
  { path: 'Account2', component: Dash2Component },
  { path: 'Account3', component: Dash3Component }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
