import { Component, SimpleChanges } from '@angular/core';
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

  loggedInUser!: UserProfile;

  ngOnInit(): void {
    // logged before
    this.getUser();
    // first time login
    this.getLoggedInUserService.loggedInUser.subscribe(
      (user) => (this.loggedInUser = user)
    );
    this.getLoggedInUserService.loginFlag.subscribe((flag) => {
      this.loginFlag = flag;
    });
  }

  getUser(): void {
    // after the header is loaded we should check if the user is logged in
    const sessionid = this.cookieService.get('sessionid');
    if (sessionid) {
      this.getLoggedInUserService
        .getUserBySessionId(sessionid)
        .subscribe((res) => {
          this.loggedInUser = res;
          this.loginFlag = true;
        });
    }
  }

  logout() {
    this.logoutService.logoutUser().subscribe((response) => {
      console.log('response', response);
    });
  }
}
