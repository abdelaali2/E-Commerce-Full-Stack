import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { httpOptions } from '../Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  constructor(
    private httpClient: HttpClient,
    private cookieService: CookieService
  ) {}

  loginURL: string = 'http://localhost:8000/users/login/';

  getAllTokens(): any {
    return this.cookieService.getAll();
  }

  login(credentials: any) {
    const body = new HttpParams()
      .set('username', credentials.username)
      .set('password', credentials.password)
      .set('sameSite', 'None')
      .toString();

    return this.httpClient.post(this.loginURL, body, httpOptions);
  }
}
