import { EventEmitter, Injectable } from '@angular/core';
import { UserProfile, newUserProfile } from '../Models/user';
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
    return this.httpClient
      .get(this.getUserURL, httpOptions)
      .subscribe(({ ok, body }) => {
        if (ok) {
          this.loggedInUser.emit(body as UserProfile);
          this.loginFlag.emit(true);
        } else {
          this.loginFlag.emit(false);
        }
      });
  }
  resetUserProfile() {
    this.loggedInUser.emit(newUserProfile);
    this.loginFlag.emit(false);
  }
}
