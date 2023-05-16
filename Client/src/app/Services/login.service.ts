import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  constructor(private httpClient: HttpClient) {}

  loginURL: string = 'http://localhost:8000/users/login/';

  login(credentials: any) {
    return this.httpClient.post(this.loginURL, credentials);
  }
}
