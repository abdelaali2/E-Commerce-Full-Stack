import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { httpOptions } from 'src/app/Models/http-options';

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
    httpOptions.headers = httpOptions.headers.set(
      'X-CSRFToken',
      this.cookieService.get('csrftoken')
    );
    return this.httpClient.post(this.logoutURL, '', httpOptions);
  }
}
