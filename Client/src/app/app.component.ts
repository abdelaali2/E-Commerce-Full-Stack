import { Component } from '@angular/core';
import { ObtainCsrfService } from './Services/userServices/obtain-csrf.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'Client';
  constructor(private csrfService: ObtainCsrfService) {}
  ngOnInit(): void {
    this.csrfService.obtainCSRFToken();
  }
}
