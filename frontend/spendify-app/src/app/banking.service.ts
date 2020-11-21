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

  getAccountSummary(){
    return this.http.get(baseUrl+"/api/account/summary/")
  }
}
