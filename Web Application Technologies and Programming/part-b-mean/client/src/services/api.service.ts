import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ApiService {

  private readonly API_BASE = '/api';

  constructor(private http: HttpClient) { }

  // GET /api/courses
  getCourses(filters?: { category?: string; level?: string; q?: string }): Observable<any> {
    let params = new HttpParams();

    if (filters?.category) {
      params = params.set('category', filters.category);
    }
    if (filters?.level) {
      params = params.set('level', filters.level);
    }
    if (filters?.q) {
      params = params.set('q', filters.q);
    }

    const url = `${this.API_BASE}/courses`;
    return this.http.get<any>(url, { params });
  }

  // GET /api/courses/:slugOrId
  getCourse(slugOrId: string): Observable<any> {
    const url = `${this.API_BASE}/courses/${encodeURIComponent(slugOrId)}`;
    return this.http.get<any>(url);
  }

  // registerStudent
  registerStudent(data: any): Observable<any> {
    return this.http.post<any>(`${this.API_BASE}/enrollments`, data);
  }


}
