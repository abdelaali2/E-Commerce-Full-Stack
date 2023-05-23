import { EventEmitter, Injectable } from '@angular/core';
import { UserProfile } from '../Models/user';
import { HttpClient } from '@angular/common/http';
import { httpOptions } from '../Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class GetLoggedInUserService {
  constructor(private httpClient: HttpClient) {}
  loggedInUser = new EventEmitter<UserProfile>();
  loginFlag = new EventEmitter<boolean>();

  getUserURL: string = 'http://localhost:8000/users/get-user/';

  getUserProfile(): any {
    return this.httpClient.get(this.getUserURL, httpOptions);
  }
}
