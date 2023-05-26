import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { httpOptions } from '../Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class ObtainCsrfService {
  constructor(private httpClient: HttpClient) {}

  obtainCSRFToken() {
    const csrf_URL = 'http://localhost:8000/users/csrf';
    this.httpClient.get(csrf_URL, httpOptions).subscribe();
  }
}
