import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { httpOptions } from 'src/app/Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  constructor(private httpClient: HttpClient) {}

  loginURL: string = 'http://localhost:8000/users/login/';

  login(credentials: any) {
    const body = new HttpParams()
      .set('username', credentials.username)
      .set('password', credentials.password)
      .set('sameSite', 'None')
      .toString();
    const modifiedOptions = { ...httpOptions };
    modifiedOptions.headers = modifiedOptions.headers.set(
      'Content-Type',
      'application/x-www-form-urlencoded'
    );

    return this.httpClient.post(this.loginURL, body, modifiedOptions);
  }
}
