import { Component } from '@angular/core';
import { GetLoggedInUserService } from '../Services/userServices/get-logged-in-user.service';
import { CookieService } from 'ngx-cookie-service';
import { UserProfile } from '../Models/user';
import { LogoutService } from '../Services/userServices/logout.service';
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
  showLogoutErrorWarning: boolean = false;

  ngOnInit(): void {
    // this.getLoggedInUserService.loggedInUser.subscribe((user) => {
    //   this.loggedInUser = user;
    // });
    // this.getLoggedInUserService.loginFlag.subscribe((flag) => {
    //   this.loginFlag = flag;
    // });
    // this.getUser();
  }

  getUser(): void {
    const sessionid = this.cookieService.get('sessionid');
    if (sessionid) {
      this.getLoggedInUserService.getUserProfile();
    }
  }

  logout() {
    this.logoutService.logoutUser().subscribe({
      next: () => {
        this.router.navigate(['']);
        this.getLoggedInUserService.resetUserProfile();
      },
      error: (err) => {
        console.log("err", err);
        this.showLogoutErrorWarning = true;
      },
    });
  }
}
