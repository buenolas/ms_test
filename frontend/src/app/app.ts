import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { Cliente } from './cliente.model';
import { ClientesApiService } from './clientes-api.service';

// Componente principal da aplicação Angular, responsável por exibir a lista de clientes e permitir a alternância do status ativo/inativo dos clientes
@Component({
  selector: 'app-root',
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
// Classe do componente App, contendo a lógica para carregar os clientes e alternar o status ativo/inativo dos clientes
export class App {
  clientes: Cliente[] = [];
  mostrarTodos = false;
  carregando = false;
  erro = '';

  constructor(private readonly clientesApi: ClientesApiService) {
    this.carregarClientes();
  }
  // Método para carregar a lista de clientes, definindo o estado de carregamento e tratamento de erros
  carregarClientes(): void {
    this.carregando = true;
    this.erro = '';
    // Chama a API para obter a lista de clientes, atualizando o estado de carregamento e tratando erros caso a requisição falhe
    this.clientesApi.list(this.mostrarTodos).subscribe({
      next: (response) => {
        this.clientes = response.results;
        this.carregando = false;
      },
      error: () => {
        this.erro = 'Não foi possível carregar os clientes.';
        this.carregando = false;
      }
    });
  }
  // Método para alternar o status ativo/inativo de um cliente, fazendo uma chamada à API e recarregando a lista de clientes após a atualização
  alternarAtivo(cliente: Cliente): void {
    this.erro = '';
    // Chama a API para atualizar o status ativo/inativo do cliente e recarrega a lista de clientes após a atualização, tratando erros caso a atualização falhe
    this.clientesApi.updateAtivo(cliente.id, !cliente.ativo).subscribe({
      next: () => this.carregarClientes(),
      error: () => {
        this.erro = 'Não foi possível atualizar o status do cliente.';
      }
    });
  }
}
