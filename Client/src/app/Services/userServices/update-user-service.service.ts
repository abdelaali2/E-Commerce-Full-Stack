import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { httpOptions } from 'src/app/Models/http-options';
import { updatedUserProfile } from 'src/app/Models/user';

@Injectable({
  providedIn: 'root',
})
export class UpdateUserServiceService {
  constructor(private httpClient: HttpClient) {}

  updateUser(newUserProfile: updatedUserProfile) {
    const updateUserURL = 'http://localhost:8000/users/update-user/';

    const formData = new FormData();
    if (newUserProfile.firstName) {
      formData.append('first_name', newUserProfile.firstName);
    }
    if (newUserProfile.lastName) {
      formData.append('last_name', newUserProfile.lastName);
    }
    if (newUserProfile.username) {
      formData.append('username', newUserProfile.username);
    }
    if (newUserProfile.email) {
      formData.append('email', newUserProfile.email);
    }
    if (newUserProfile.profile_picture) {
      formData.append(
        'profile_picture',
        newUserProfile.profile_picture,
        newUserProfile.profile_picture.name
      );
    }
    return this.httpClient.put(updateUserURL, formData, httpOptions);
  }
}
