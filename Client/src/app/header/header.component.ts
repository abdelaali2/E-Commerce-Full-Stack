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
      this.getLoggedInUserService.getUserProfile().subscribe((res: any) => {
        this.loggedInUser = res.body as UserProfile;
        this.loginFlag = true;
      });
    }
  }

  logout() {
    this.logoutService.logoutUser().subscribe(({ ok }) => {
      if (ok) {
        this.router.navigate(['']);

        this.getLoggedInUserService.getUserProfile().subscribe(() => {
          this.getLoggedInUserService.loggedInUser.emit(newUserProfile);
          this.getLoggedInUserService.loginFlag.emit(true);
        });
      } else {
        // TODO: handle wrong login credentials before redirection.
        // TODO: enhance UI
        alert(`couldn't log you out! Please try again`);
      }
    });
  }
}
