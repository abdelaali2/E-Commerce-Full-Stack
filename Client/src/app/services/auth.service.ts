import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpHeaders,
  HttpParams,
  HttpResponse,
} from '@angular/common/http';
import { map } from 'rxjs/operators';

interface response{
  'status': string;
  'token': string;
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  apiUrl = 'http://127.0.0.1:8000/accounts/login/';
  constructor(private http: HttpClient) {}

  login(username: string, password: string) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
    });

    const body = new HttpParams()
      .set('username', username)
      .set('password', password)
      .set('sameSite', 'None')
      .toString();

    const options = {
      headers: headers,
      withCredentials: true,
    };

    return this.http.post(this.apiUrl, body, options).pipe(
      map((response) => {
        const r = response as response
        console.log(r);

        return r.token;
      })
    );
  }

}
