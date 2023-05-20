import { Component } from '@angular/core';
import { LoginService } from '../Services/login.service';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { GetLoggedInUserService } from '../Services/get-logged-in-user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  username: string = 'ibrahim';
  password: string = 'P@ssw0rd11';

  constructor(
    private loginService: LoginService,
    private router: Router,
    private cookieService: CookieService,
    private getLoggedInUserService: GetLoggedInUserService
  ) {}

  // // TODO: handle wrong login credentials before redirection.

  onSubmit() {
    const user = { username: this.username, password: this.password };
    this.loginService
      .login(user)
      .subscribe(({ sessionid, csrftoken, success }) => {
        if (success) {
          this.cookieService.set('sessionid', sessionid);
          this.cookieService.set('csrftoken', csrftoken);
          this.router.navigate(['']);

          this.getLoggedInUserService
            .getUserBySessionId(this.cookieService.get('sessionid'))
            .subscribe((user) => {
              this.getLoggedInUserService.loggedInUser.emit(user);
              this.getLoggedInUserService.loginFlag.emit(true);
            });
        } else {
          // TODO: enhance UI
          alert('Invalid username or password');
        }
      });
  }
}
