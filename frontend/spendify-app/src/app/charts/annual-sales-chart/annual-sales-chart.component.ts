import { Component, OnInit, Input } from '@angular/core';
import { ChartDataSets, ChartOptions, ChartType } from 'chart.js';
import { Color, Label } from 'ng2-charts';
import {BankingService} from '../../banking.service';

@Component({
  selector: 'app-annual-sales-chart',
  templateUrl: './annual-sales-chart.component.html',
  styleUrls: ['./annual-sales-chart.component.css']
})
export class AnnualSalesChartComponent implements OnInit {
  constructor(private bankingService: BankingService) {}
  currentBankingInfo = <any>[];
  currentRiskInfo = <any>[];
  public lineChartData: ChartDataSets[] = [
    { data: [65, 59, 80, 81, 56, 55, 40], label: 'Monthly Spending' },
    { data: [100,100,100,100,100,100,100,100,100,100,100,100], label: 'Max Risk ' },
    { data: [], label: 'Risk ' }
  ];


  options: {
    responsive: true,
    elements: {
        line :{
            fill: false
        }
    },
    title: {
        display: true,
        position: 'bottom',
        text: 'Commissions Paid',
        fontSize: 14
    },
    //scales: [{
    scales: { // Shouldn't be an array.
       yAxes: [{
           display: true,
           position: 'left',
           type: "linear",
            scaleLabel: {
                display: true,
                labelString: 'USD',
                beginAtZero: true,
            },
           //yAxisID: "id1"
           id: "id1" // incorrect property name.
        },{
           scaleLabel: {
                display: true,
                labelString: 'Commissions',
                beginAtZero: false,
            },
           //display: false,
           display: true, // Hopefully don't have to explain this one.
           type: "linear",
           position:"right",
           ticks: {
            max: 1,
            min: 0,
            stepSize: 4
          },
           gridLines: {
               display: false
           },
           //yAxisID: "id2"
           id: "id2" // incorrect property name.
        }]
    //}]
    } // Shouldn't be an arra
  }











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

  @Input() dashId;

  ngOnInit() {
    this.loadData();

  }


  loadData(){
    this.lineChartData[0].data = [0,0,0,0,0,0,0,0,0,0,0,0]

    this.bankingService.getMonthlyTransactions(this.dashId).subscribe(
      summaryData => {
        this.currentBankingInfo  = summaryData

        for (const [key, value] of Object.entries(summaryData)) {
          this.lineChartData[0].data[key] = value;
        }

      })
      this.bankingService.getRiskPrediction(this.dashId).subscribe(
        summaryData => {
          this.currentRiskInfo  = summaryData
          console.log(summaryData, "is the risk data")

          this.currentRiskInfo.forEach(element=>{
            console.log(this.lineChartData[2].data, "is the current data")
            console.log(element["ratioCount"], "is the current risk percent")
            this.lineChartData[2].data.push(element["ratioCount"].substring(0, element["ratioCount"].length-1))
          })


        })
       }



}
