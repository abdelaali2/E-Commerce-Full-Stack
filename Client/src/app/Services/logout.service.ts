import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { httpOptions } from '../Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class LogoutService {
  constructor(
    private httpClient: HttpClient,
    private cookieService: CookieService
  ) {}

  logoutURL: string = 'http://localhost:8000/users/logout/';

  logoutUser() {
    return this.httpClient.post(this.logoutURL, '', httpOptions);
  }
}
