import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { Cliente } from './cliente.model';
import { ClientesApiService } from './clientes-api.service';


@Component({
  selector: 'app-root',
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  clientes: Cliente[] = [];
  mostrarTodos = false;
  carregando = false;
  erro = '';

  constructor(private readonly clientesApi: ClientesApiService) {
    this.carregarClientes();
  }

  carregarClientes(): void {
    this.carregando = true;
    this.erro = '';

    this.clientesApi.list(this.mostrarTodos).subscribe({
      next: (clientes) => {
        this.clientes = clientes;
        this.carregando = false;
      },
      error: () => {
        this.erro = 'Não foi possível carregar os clientes.';
        this.carregando = false;
      }
    });
  }

  alternarAtivo(cliente: Cliente): void {
    this.erro = '';

    this.clientesApi.updateAtivo(cliente.id, !cliente.ativo).subscribe({
      next: () => this.carregarClientes(),
      error: () => {
        this.erro = 'Não foi possível atualizar o status do cliente.';
      }
    });
  }
}
