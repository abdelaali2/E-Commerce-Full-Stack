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

  private currentUser!: UserProfile;
  private is_loggedIn: boolean = false;

  getUserURL: string = 'http://localhost:8000/users/get-user/';

  getUserProfile(): any {
    return this.httpClient
      .get(this.getUserURL, httpOptions)
      .subscribe(({ ok, body }) => {
        if (ok) {
          this.currentUser = body as UserProfile;
          this.is_loggedIn = true;
          this.loggedInUser.emit(body as UserProfile);
          this.loginFlag.emit(true);
        } else {
          this.currentUser = newUserProfile;
          this.is_loggedIn = false;
          this.loggedInUser.emit(newUserProfile);
          this.loginFlag.emit(false);
        }
      });
  }
  resetUserProfile() {
    this.loggedInUser.emit(newUserProfile);
    this.loginFlag.emit(false);
  }
}
