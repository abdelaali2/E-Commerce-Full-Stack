import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ReviewsService {
  apiUrl = 'http://localhost:8000/reviews/';

  constructor(private httpClient: HttpClient) {}

  // get review by review id
  getReview(id: number) {
    // payload: {id: 1, title: "Expensive", content: "Over priced", rating: 1, product: 2, user: 1}
    return this.httpClient.get(`${this.apiUrl}details/${id}/`);
  }

  // get reviews by user id
  getReviewsByUserId(userId: number) {
    return this.httpClient.get(`${this.apiUrl}user/${userId}/`);
  }
}
