import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { httpOptions } from '../Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class LogoutService {
  constructor(private httpClient: HttpClient) {}

  logoutURL: string = 'http://localhost:8000/users/logout/';

  logoutUser() {
    return this.httpClient.post(this.logoutURL, '', httpOptions);
  }
}
