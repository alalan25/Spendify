import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import {Observable} from 'rxjs';
const baseUrl = 'http://127.0.0.1:5000';

@Injectable({
  providedIn: 'root'
})
export class BankingService {

  constructor(private http: HttpClient) {
  }

  getHelloWorld(): Observable<any>{
    console.log("Service method called on", baseUrl+"/p")
    return this.http.get(baseUrl+"/p");
   }

   getTransactions(inputId:string): Observable<any>{
    console.log("Service method called on", baseUrl+"/p")
    return this.http.get(baseUrl+"/api/transactions/?id="+inputId);
  }

  getAccountSummary(inputId:string){
    return this.http.get(baseUrl+"/api/account/summary/?id="+inputId)
  }
  getMonthlyTransactions(inputId:string){
    console.log(baseUrl+"/api/account/year/?id="+inputId, "is monthly the input")
    return this.http.get(baseUrl+"/api/account/year/?id="+inputId)
  }
  getCategoryTransactions(inputId:string){
    console.log(baseUrl+"/api/account/year/categories/?id="+inputId, "is the category input")
    return this.http.get(baseUrl+"/api/account/year/categories/?id="+inputId)
  }



}
