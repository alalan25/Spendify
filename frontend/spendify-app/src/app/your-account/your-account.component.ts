import { Component, OnInit } from '@angular/core';
import { BankingService } from '../banking.service';

@Component({
  selector: 'app-your-account',
  templateUrl: './your-account.component.html',
  styleUrls: ['./your-account.component.css']
})
export class YourAccountComponent implements OnInit {
  hello: Object;

  constructor(private bankingService: BankingService) {
    this.getHello();
   }



  ngOnInit(): void {

  }

  getHello(){
    return this.bankingService.getHelloWorld()
    .subscribe(result=>{
      this.hello = result;
    })
  }
}
