import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import {BankingService} from '../banking.service'


@Component({
  selector: 'app-dash2',
  templateUrl: './dash2.component.html',
  styleUrls: ['./dash2.component.css']
})
export class Dash2Component implements OnInit {

  miniCardData=  <any>[];
  ngOnInit() {
    this.bankingService.getAccountSummary().subscribe(
     summaryData => {
       console.log(summaryData, "was the response")
        this.miniCardData = summaryData

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
