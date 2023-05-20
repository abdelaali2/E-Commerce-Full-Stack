import { Injectable } from '@angular/core';
import { UserProfile } from '../Models/user';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class GetLoggedInUserService {
  constructor(private httpClient: HttpClient) {}

  getUserURL: string = 'http://localhost:8000/users/get-user/';

  getUserBySessionId(sessionId: string): Observable<UserProfile> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
    });

    const params = {
      sessionid: sessionId,
      sameSite: 'None',
    };

    return this.httpClient.get<UserProfile>(this.getUserURL, {
      headers,
      params,
    });
  }
}
