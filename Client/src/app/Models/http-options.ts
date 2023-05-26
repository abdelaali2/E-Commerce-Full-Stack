import { HttpHeaders } from '@angular/common/http';

export const httpOptions = {
  headers: new HttpHeaders(),
  // headers: new HttpHeaders({
  //   'Content-Type': 'undefined',
  // }),
  withCredentials: true,
  observe: 'response' as 'response',
  reportProgress: true,
};
