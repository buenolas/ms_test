import { TestBed } from '@angular/core/testing';
import { App } from './app';


// Testes unitários para o componente principal da aplicação Angular, garantindo que ele seja criado corretamente e renderize o título da página
describe('App', () => {
  // Configura o ambiente de teste para o componente App antes de cada teste, importando o componente e compilando os componentes necessários
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
    }).compileComponents();
  });

  // Testa se o componente App é criado corretamente
  it('should create the app', () => {
    const fixture = TestBed.createComponent(App);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });
  // Testa se o título da página é renderizado corretamente no template do componente App
  it('should render page title', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h1')?.textContent).toContain('Clientes');
  });
});

// Garante sanidade mínima do frontend e evita regressão trivial.