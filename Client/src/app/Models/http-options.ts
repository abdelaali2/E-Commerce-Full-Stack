import { HttpHeaders } from '@angular/common/http';

export const httpOptions = {
  headers: new HttpHeaders(),
  withCredentials: true,
  observe: 'response' as 'response',
  reportProgress: true,
};
