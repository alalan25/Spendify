import { Component, OnInit, Input } from '@angular/core';
import { ChartDataSets, ChartOptions, ChartType } from 'chart.js';
import { Label } from 'ng2-charts';
import {BankingService} from "../../banking.service";

@Component({
  selector: 'app-store-sessions-chart',
  templateUrl: './store-sessions-chart.component.html',
  styleUrls: ['./store-sessions-chart.component.css']
})
export class StoreSessionsChartComponent implements OnInit {

  @Input() dashId:string;
  public barChartOptions: ChartOptions = {
    responsive: true,
  };
  public barChartLabels: Label[] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  public barChartType: ChartType = 'bar';
  public barChartLegend = true;
  public barChartPlugins = [];

  public barChartData: ChartDataSets[] = [
    { data: [], label: 'Low Scenario' },
    { data: [], label: 'Average Scenario' },
    { data: [], label: 'High Scenario' }
  ];

  constructor(private bankingService:BankingService) { }

  getData(){
    this.bankingService.getAccountPrediction(this.dashId).subscribe(
      element =>{
        for (const [key, value] of Object.entries(element["yhat_lower"])) {
          this.barChartData[0].data[key] = value
        }

        for (const [key, value] of Object.entries(element["yhat"])) {
          this.barChartData[1].data[key] = value
        }
        for (const [key, value] of Object.entries(element["yhat_upper"])) {
          this.barChartData[2].data[key] = value
        }
      }
    )
  }

  ngOnInit() {
    this.getData();
  }

}
