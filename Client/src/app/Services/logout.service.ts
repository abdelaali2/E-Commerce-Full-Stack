import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map } from 'rxjs';
import { ResponseFromDjango } from '../Models/response-from-django';
import { CookieService } from 'ngx-cookie-service';

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
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
    });

    const options = {
      headers: headers,
      Cookie: `csrftoken=${this.cookieService.get('csrftoken')};`,
    };

    return this.httpClient.post(this.logoutURL, '', options).pipe(
      map((response) => {
        console.log('response', response);

        return response;
      })
    );
  }
}
