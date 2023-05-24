import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ResponseFromDjango } from '../Models/response-from-django';
import { map } from 'rxjs';
import { User } from '../Models/user';
import { httpOptions } from '../Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class SignupService {
  constructor(private httpClient: HttpClient) {}

  signup(credentials: User) {
    const signupURL = 'http://localhost:8000/users/signup/';

    const body = new HttpParams()
      .set('username', credentials.username)
      .set('password1', credentials.password1)
      .set('password2', credentials.password2)
      .set('first_name', credentials.first_name)
      .set('last_name', credentials.last_name)
      .set('email', credentials.email)
      .set('is_dealer', credentials.is_dealer || false)
      .toString();

    return this.httpClient.post(signupURL, body, httpOptions);
  }
}
