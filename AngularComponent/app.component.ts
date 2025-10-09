import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  num1: number | null = null;
  num2: number | null = null;
  resultado: number | null = null;

  multiplicar() {
    const n1 = Number((document.getElementById('num1') as HTMLInputElement).value);
    const n2 = Number((document.getElementById('num2') as HTMLInputElement).value);
    this.resultado = n1 * n2;
  }
}
