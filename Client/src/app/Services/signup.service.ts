import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ResponseFromDjango } from '../Models/response-from-django';
import { map } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SignupService {
  constructor(private httpClient: HttpClient) {}

  signupURL: string = 'http://localhost:8000/users/signup/';

  signup(credentials: any) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
    });

    const body = new HttpParams()
      .set('username', credentials.username)
      .set('password1', credentials.password1)
      .set('password2', credentials.password2)
      .set('first_name', credentials.first_name)
      .set('last_name', credentials.last_name)
      .set('email', credentials.email)
      // .set('is_dealer', credentials.is_dealer || false)
      .set('sameSite', 'None')
      .toString();

    const options = {
      headers: headers,
    };

    return this.httpClient.post(this.signupURL, body, options).pipe(
      map((response) => {
        const resp = response as ResponseFromDjango;
        console.log(resp);

        return resp.sessionid;
      })
    );
  }
}
