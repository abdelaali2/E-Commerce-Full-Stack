import { Router } from '@angular/router';
import { Component } from '@angular/core';
import { LoginService } from '../Services/userServices/login.service';
import { GetLoggedInUserService } from '../Services/userServices/get-logged-in-user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  username: string = 'ibrahim';
  password: string = 'P@ssw0rd11';
  showPasswordOnPress: boolean = false;
  showInvalidInputWarning: boolean = false;
  responseError!: string;

  constructor(
    private loginService: LoginService,
    private router: Router,
    private getLoggedInUserService: GetLoggedInUserService
  ) {}

  onSubmit() {
    const user = { username: this.username, password: this.password };
    if (!user.username || !user.password) {
      this.showInvalidInputWarning = true;
      return;
    }
    this.loginService.login(user).subscribe({
      next: () => {
        this.getLoggedInUserService.getUserProfile();
        this.router.navigate(['']);
      },
      error: (err) => {
        this.responseError = err.error.error.__all__[0];
      },
    });
  }
}
