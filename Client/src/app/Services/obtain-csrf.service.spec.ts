import { TestBed } from '@angular/core/testing';

import { ObtainCsrfService } from './obtain-csrf.service';

describe('ObtainCsrfService', () => {
  let service: ObtainCsrfService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ObtainCsrfService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
