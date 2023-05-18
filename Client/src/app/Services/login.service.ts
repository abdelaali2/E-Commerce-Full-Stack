import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { map } from 'rxjs/operators';
import { ResponseFromDjango } from '../Models/response-from-django';

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
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
    });

    const body = new HttpParams()
      .set('username', credentials.username)
      .set('password', credentials.password)
      .set('sameSite', 'None')
      .toString();

    const options = {
      headers: headers,
    };

    return this.httpClient.post(this.loginURL, body, options).pipe(
      map((response) => {
        const resp = response as ResponseFromDjango;
        console.log(resp);

        return resp.sessionid;
      })
    );
  }
}
