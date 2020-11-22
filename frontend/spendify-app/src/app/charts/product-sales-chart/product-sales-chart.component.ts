import { Component, OnInit, Input } from '@angular/core';
import { ChartDataSets, ChartOptions, ChartType } from 'chart.js';
import { Label } from 'ng2-charts';
import {BankingService} from '../../banking.service'

@Component({
  selector: 'app-product-sales-chart',
  templateUrl: './product-sales-chart.component.html',
  styleUrls: ['./product-sales-chart.component.css']
})
export class ProductSalesChartComponent implements OnInit {
  @Input() dashId;

  public radarChartOptions: ChartOptions = {
    responsive: true,
  };
  public radarChartLabels: Label[] = ['Fast food', 'Health', 'Personal Care', 'Entertainment', 'Cable/Phone', 'Rideshare'];



  getSpending(){
    this.bankingService.getCategoryTransactions(this.dashId).subscribe(
      element =>{
        console.log(this.radarChartData[0].data[1], "is the datA")
          this.radarChartData[0].data[0] = element["fastfood"]
          this.radarChartData[0].data[1] = element["online_retail"]
          this.radarChartData[0].data[2] = element["personal care"]
          this.radarChartData[0].data[3] = element["entertainment"]
          this.radarChartData[0].data[4] = element["cable/phone"]
          this.radarChartData[0].data[5] = element["reideshare"]

        console.log(element["food"], "was the rfgfesponse")
      }
    )
    this.bankingService.getSegmentPrediction(this.dashId).subscribe(
      element =>{
        console.log(this.radarChartData[0].data[1], "is the datA")
          this.radarChartData[0].data[0] = element["fastfood"]
          this.radarChartData[0].data[1] = element["online_retail"]
          this.radarChartData[0].data[2] = element["personal care"]
          this.radarChartData[0].data[3] = element["entertainment"]
          this.radarChartData[0].data[4] = element["cable/phone"]
          this.radarChartData[0].data[5] = element["reideshare"]

        
      }
    )
  }

  public radarChartData: any[] = [
    { data: [], label: '% Spending this Year' },
    { data: [], label: '% Predicted next Year' }
  ];
  public radarChartType: ChartType = 'radar';
  constructor(private bankingService: BankingService) { }

  ngOnInit() {

      console.log("calling the init")
      this.getSpending();
  }

}
