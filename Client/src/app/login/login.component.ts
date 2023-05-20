import { Component } from '@angular/core';
import { LoginService } from '../Services/login.service';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

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
    private cookieService: CookieService
  ) {}

  // // TODO: handle wrong login credentials before redirection.

  onSubmit() {
    const user = { username: this.username, password: this.password };
    this.loginService
      .login(user)
      .subscribe(({ sessionid, csrftoken, success }) => {
        console.log('success', success);

        if (success) {
          // this.cookieService.set('sessionid', sessionid);
          // this.cookieService.set('csrftoken', csrftoken);
          this.router.navigate(['']);
        } else {
          // TODO: enhance UI
          alert('Invalid username or password!');
        }
      });
  }
}
