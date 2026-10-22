import { Routes } from '@angular/router';
import { HomeComponent } from '../pages/home/home.component';
import { CourseDetailsComponent } from '../pages/course-details/course-details.component';


export const routes: Routes = [
  { path: '', component: HomeComponent },

  {
    path: 'courses',
    loadComponent: () =>
      import('../pages/courses/courses.component').then(m => m.CoursesComponent)
  },

  {
    path: 'courses/:slug',
    loadComponent: () =>
      import('../pages/course-details/course-details.component').then(
        m => m.CourseDetailsComponent
      )
  },
  {
    path: 'books',
    loadComponent: () =>
      import('../pages/books/books.component').then(m => m.BooksComponent)
  },

  {
    path: 'about',
    loadComponent: () =>
      import('../pages/about/about.component').then(m => m.AboutComponent)
  },

  {
    path: 'register',
    loadComponent: () =>
      import('../pages/register/register.component').then(m => m.RegisterComponent)
  },


  { path: '**', redirectTo: '' }
];

