import { Component } from '@angular/core';
import { LoginService } from '../Services/login.service';
import { Router } from '@angular/router';
import { GetLoggedInUserService } from '../Services/get-logged-in-user.service';
import { UserProfile } from '../Models/user';

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
    private getLoggedInUserService: GetLoggedInUserService
  ) {}

  onSubmit() {
    const user = { username: this.username, password: this.password };
    this.loginService.login(user).subscribe(({ ok, body }) => {
      if (ok) {
        this.router.navigate(['']);
        this.getLoggedInUserService.getUserProfile();
      } else {
        // TODO: handle wrong login credentials before redirection.
        // TODO: enhance UI
        alert('Invalid username or password');
      }
    });
  }
}
