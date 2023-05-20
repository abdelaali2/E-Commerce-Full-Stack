import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ResponseFromDjango } from '../Models/response-from-django';

@Injectable({
  providedIn: 'root',
})
export class LogoutService {
  constructor(private httpClient: HttpClient) {}

  logoutURL: string = 'http://localhost:8000/users/logout/';

  // logutUser():Observable<ResponseFromDjango>{

    
  //   return null;
  // }
}
