import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import {BankingService} from '../banking.service'


@Component({
  selector: 'app-dash',
  templateUrl: './dash.component.html',
  styleUrls: ['./dash.component.css']
})
export class DashComponent implements OnInit {

  miniCardData: any[];
  ngOnInit() {
    this.bankingService.getAccountSummary().subscribe(
     summaryData => {
       console.log(summaryData, "was the response")
        this.miniCardData = summaryData
        console.log(this.miniCardData.length)
      }
    );
  }

  cardLayout = this.breakpointObserver.observe(Breakpoints.Handset).pipe(
    map(({ matches }) => {
      if (matches) {
        return {
          columns: 1,
          miniCard: { cols: 1, rows: 1 },
          chart: { cols: 1, rows: 2 },
          table: { cols: 1, rows: 4 },
        };
      }

     return {
        columns: 4,
        miniCard: { cols: 1, rows: 1 },
        chart: { cols: 2, rows: 2 },
        table: { cols: 4, rows: 4 },
      };
    })
  );



  constructor(private breakpointObserver: BreakpointObserver, private bankingService: BankingService) {}
}
