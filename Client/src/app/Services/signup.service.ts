import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../Models/user';
import { httpOptions } from '../Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class SignupService {
  constructor(private httpClient: HttpClient) {}

  signup(credentials: User) {
    const signupURL = 'http://localhost:8000/users/signup/';

    const formData = new FormData();
    formData.append('username', credentials.username);
    formData.append('password1', credentials.password1);
    formData.append('password2', credentials.password2);
    formData.append('first_name', credentials.first_name);
    formData.append('last_name', credentials.last_name);
    formData.append('email', credentials.email);
    formData.append('is_dealer', (credentials.is_dealer || false).toString());
    if (credentials.profilePicture) {
      formData.append(
        'profile_picture',
        credentials.profilePicture,
        credentials.profilePicture.name
      );
    }
    return this.httpClient.post(signupURL, formData, httpOptions);
  }
}
