import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Cliente } from './cliente.model';

@Injectable({
  providedIn: 'root'
})
export class ClientesApiService {
  private readonly baseUrl = '/api/clientes/';

  constructor(private readonly http: HttpClient) {}

  list(todos: boolean): Observable<Cliente[]> {
    const url = todos ? `${this.baseUrl}?todos=1` : this.baseUrl;
    return this.http.get<Cliente[]>(url);
  }

  updateAtivo(clienteId: number, ativo: boolean): Observable<Cliente> {
    return this.http.patch<Cliente>(`${this.baseUrl}${clienteId}/`, { ativo });
  }
}
