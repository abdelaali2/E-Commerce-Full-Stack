import { Component, SimpleChanges } from '@angular/core';
import { GetLoggedInUserService } from '../Services/get-logged-in-user.service';
import { CookieService } from 'ngx-cookie-service';
import { UserProfile, newUserProfile } from '../Models/user';
import { LogoutService } from '../Services/logout.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent {
  constructor(
    private router: Router,
    private cookieService: CookieService,
    private logoutService: LogoutService,
    private getLoggedInUserService: GetLoggedInUserService
  ) {}

  loginFlag: boolean = false;

  loggedInUser!: UserProfile;

  ngOnInit(): void {
    // first time login
    this.getLoggedInUserService.loggedInUser.subscribe(
      (user) => (this.loggedInUser = user)
    );
    this.getLoggedInUserService.loginFlag.subscribe((flag) => {
      this.loginFlag = flag;
    });
    // logged before
    this.getUser();
  }

  getUser(): void {
    // after the header is loaded we should check if the user is logged in
    const sessionid = this.cookieService.get('sessionid');
    if (sessionid) {
      this.getLoggedInUserService.getUserProfile();
    }
  }

  logout() {
    this.logoutService.logoutUser().subscribe(({ ok }) => {
      if (ok) {
        this.router.navigate(['']);
        this.getLoggedInUserService.resetUserProfile();
      } else {
        // TODO: handle wrong login credentials before redirection.
        // TODO: enhance UI
        alert(`couldn't log you out! Please try again`);
      }
    });
  }
}
