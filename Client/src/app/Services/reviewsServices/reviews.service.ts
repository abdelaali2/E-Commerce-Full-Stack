import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { httpOptions } from 'src/app/Models/http-options';

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

  // get reviews by product id
  getReviewsByProductId(productId: number) {
    return this.httpClient.get(`${this.apiUrl}product/${productId}/`);
  }

  // edit review
  editReview(id: number, data = {}) {
    return this.httpClient.put(`${this.apiUrl}${id}/`, data, httpOptions);
  }

  // delete review
  deleteReview(id: number) {
    return this.httpClient.delete(`${this.apiUrl}delete/${id}/`, httpOptions);
  }

  // create review
  createReview(data = {}) {
    return this.httpClient.post(`${this.apiUrl}create/`, data, httpOptions);
  }
}
