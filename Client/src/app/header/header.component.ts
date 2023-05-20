import { Component } from '@angular/core';
import { GetLoggedInUserService } from '../Services/get-logged-in-user.service';
import { CookieService } from 'ngx-cookie-service';
import { UserProfile } from '../Models/user';
import { LogoutService } from '../Services/logout.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent {
  constructor(
    private getLoggedInUserService: GetLoggedInUserService,
    private cookieService: CookieService,
    private logoutService: LogoutService
  ) {}

  loginFlag: boolean = false;

  loggedInUser: UserProfile = {
    username: '',
    first_name: '',
    last_name: '',
    email: '',
    is_dealer: false,
  };

  ngOnInit(): void {
    this.loginFlag = Boolean(this.cookieService.get('sessionid') || false);
    if (this.loginFlag) {
      this.getUser();
    }
  }

  getUser(): void {
    // after the header is loaded we should check if the user is logged in
    const sessionid = this.cookieService.get('sessionid');
    this.getLoggedInUserService
      .getUserBySessionId(sessionid)
      .subscribe((res) => {
        this.loggedInUser = res;
        // console.log('loggedInUser', this.loggedInUser);
      });
  }

  logout() {
    this.logoutService.logoutUser().subscribe((response) => {
      console.log('response', response);
    });
  }
}
