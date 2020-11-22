import { Component, OnInit } from '@angular/core';
import { ChartDataSets, ChartOptions, ChartType } from 'chart.js';
import { Color, Label } from 'ng2-charts';
import {BankingService} from '../../banking.service';

@Component({
  selector: 'app-annual-sales-chart',
  templateUrl: './annual-sales-chart.component.html',
  styleUrls: ['./annual-sales-chart.component.css']
})
export class AnnualSalesChartComponent implements OnInit {
  currentBankingInfo = <any>[];

  public lineChartData: ChartDataSets[] = [
    { data: [65, 59, 80, 81, 56, 55, 40], label: 'Monthly Spending' },
  ];
  public lineChartLabels: Label[] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  public lineChartOptions: ChartOptions = {
    responsive: true,
  };
  public lineChartColors: Color[] = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,0,0,0.3)',
    },
  ];
  public lineChartLegend = true;
  public lineChartType: ChartType = 'line';
  public lineChartPlugins = [];



  ngOnInit() {
    this.loadData();
  }
  loadData(){
    this.lineChartData[0].data = [0,0,0,0,0,0,0,0,0,0,0,0]
    this.bankingService.getMonthlyTransactions().subscribe(
      summaryData => {
        this.currentBankingInfo  = summaryData

        for (const [key, value] of Object.entries(summaryData)) {
          this.lineChartData[0].data[key] = value;
        }

      })
       }


  constructor(private bankingService: BankingService) {}
}
