import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, NgForm } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';


type Mode = 'form' | 'preview' | 'done';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  mode: Mode = 'form';

  formData: any = {
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    passwordConfirm: '',
    level: '',
    categories: [] as string[],
    courses: [] as string[]
  };

  submitting = false;
  submitError = '';
  categoryLabels: Record<string, string> = {
    programming: 'Προγραμματισμός',
    networks: 'Δίκτυα',
    security: 'Ασφάλεια',
    data: 'Δεδομένα'
  };

  courseLabels: Record<string, string> = {
    'java': 'Προγραμματισμός με Java',
    'python-intro': 'Εισαγωγή στον Προγραμματισμό με Python',
    'cpp': 'Προγραμματισμός Υπολογιστών με C++',
    'computer-networks': 'Δίκτυα Υπολογιστών',
    'communication-networks': 'Δίκτυα Επικοινωνιών',
    'network-security': 'Ασφάλεια Δικτύων',
    'cyber-security': 'Κυβερνοασφάλεια',
    'databases': 'Βάσεις Δεδομένων'
  };

  getCategoryNames(): string[] {
    return this.formData.categories.map((c: string) => this.categoryLabels[c] || c);
  }

  getCourseNames(): string[] {
    return this.formData.courses.map((c: string) => this.courseLabels[c] || c);
  }

  constructor(
    private api: ApiService,
    private router: Router,
    private cdr: ChangeDetectorRef
  ) { }

  // Συλλογή επιλογών checkbox
  onCategoryChange(event: Event, value: string) {
    const checked = (event.target as HTMLInputElement).checked;
    this.toggleInArray(this.formData.categories, value, checked);
  }

  onCourseChange(event: Event, value: string) {
    const checked = (event.target as HTMLInputElement).checked;
    this.toggleInArray(this.formData.courses, value, checked);
  }

  private toggleInArray(arr: string[], value: string, add: boolean) {
    const idx = arr.indexOf(value);
    if (add && idx === -1) {
      arr.push(value);
    } else if (!add && idx !== -1) {
      arr.splice(idx, 1);
    }
  }

  // Προεπισκόπηση στοιχείων
  showPreview(form: NgForm) {
    if (form.invalid || this.formData.password !== this.formData.passwordConfirm) {
      if (this.formData.password !== this.formData.passwordConfirm) {
        form.controls['passwordConfirm']?.setErrors({ mismatch: true });
      }
      form.control.markAllAsTouched();
      return;
    }
    console.log('Preview click', form);
    this.mode = 'preview';
  }

  backToForm() {
    this.mode = 'form';
  }

  // Υποβολή
  submitRegistration() {
    this.submitting = true;
    this.submitError = '';

    const payload = { ...this.formData };
    delete payload.passwordConfirm;

    this.api.registerStudent(payload).subscribe({
      next: () => {
        this.submitting = false;
        this.mode = 'done';
        this.cdr.markForCheck();

        // Μετά από λίγο γύρνα στην αρχική
        setTimeout(() => {
          this.router.navigate(['/']);
        }, 3000); // 3 δευτερόλεπτα
      },

      error: (err) => {
        console.error('Registration API error:', err);
        this.submitting = false;
        this.submitError = 'Προέκυψε σφάλμα κατά την υποβολή. Δοκίμασε ξανά.';
      }
    });
  }
}
