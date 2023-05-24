import { Component } from '@angular/core';
import { User, UserProfile } from '../Models/user';
import { SignupService } from '../Services/signup.service';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { GetLoggedInUserService } from '../Services/get-logged-in-user.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss'],
})
export class SignupComponent {
  constructor(
    private signupService: SignupService,
    private router: Router,
    private getLoggedInUserService: GetLoggedInUserService
  ) {}

  user: User = {
    first_name: 'ibrahim',
    last_name: 'badr',
    email: 'ibrahim@email.com',
    username: 'ibrahim',
    password1: 'P@ssw0rd11',
    password2: 'P@ssw0rd11',
    is_dealer: false,
    photo: undefined,
  };

  // TODO: handle password confirmation criteria.
  // TODO: handle username exists already error message.

  onSubmit() {
    if (this.user.password1 !== this.user.password2) {
      alert('Passwords do not match');
      return;
    }

    this.signupService.signup(this.user)?.subscribe(({ ok }) => {
      if (ok) {
        this.getLoggedInUserService.getUserProfile();
        this.router.navigate(['']);
      } else {
        // TODO: handle wrong login credentials before redirection.
        // TODO: enhance UI
        alert('Invalid username or password');
      }
    });
  }

  onFileSelected(event: any) {
    this.user.photo = event.target.files[0];
    console.log('this.user.photo', this.user.photo);

    // const file = event.target.files[0];
    // const reader = new FileReader();
    // reader.readAsDataURL(file);
    // reader.onload = () => {
    //   const base64 = reader.result.toString().split(',')[1];
    //   const formData = new FormData();
    //   formData.append('file', base64);
    //   this.http.post('/api/upload', formData).subscribe((response) => {
    //     console.log(response);
    //   });
    // };
  }
}
