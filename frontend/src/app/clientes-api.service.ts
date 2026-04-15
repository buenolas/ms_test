import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Cliente, PaginatedResponse } from './cliente.model';

// Serviço Angular para interagir com a API de clientes, fornecendo métodos para listar clientes e atualizar o status ativo/inativo dos clientes
@Injectable({
  providedIn: 'root'
})
// Classe do serviço ClientesApiService, contendo métodos para listar clientes e atualizar o status ativo/inativo dos clientes, utilizando o HttpClient para fazer requisições à API
export class ClientesApiService {
  private readonly baseUrl = '/api/clientes/';

  constructor(private readonly http: HttpClient) {}
  // Método para listar clientes, aceitando um parâmetro para indicar se deve listar todos os clientes ou apenas os ativos, e retornando um Observable com a resposta paginada da API
  list(todos: boolean): Observable<PaginatedResponse<Cliente>> {
    // Se o parâmetro 'todos' for verdadeiro, adiciona um query parameter para listar todos os clientes; caso contrário, lista apenas os clientes ativos
    const url = todos ? `${this.baseUrl}?todos=1` : this.baseUrl;
    return this.http.get<PaginatedResponse<Cliente>>(url);
  }
  // Método para atualizar o status ativo/inativo de um cliente, aceitando o ID do cliente e o novo status, e retornando um Observable com a resposta da API
  updateAtivo(clienteId: number, ativo: boolean): Observable<Cliente> {
    return this.http.patch<Cliente>(`${this.baseUrl}${clienteId}/`, { ativo });
  }
}

// Separa acesso à API da UI (boa prática de organização e manutenção).