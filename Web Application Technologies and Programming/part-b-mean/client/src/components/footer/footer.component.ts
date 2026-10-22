import { Component } from '@angular/core';

@Component({
  selector: 'app-footer',
  standalone: true,
  template: `
    <footer class="site-footer">
      <div class="container footer-inner">
        <p>© CS4All Academy</p>
        <p>Πλατφόρμα e-learning για μαθήματα Πληροφορικής.</p>
      </div>
    </footer>
  `,
  styles: []
})
export class FooterComponent {}
