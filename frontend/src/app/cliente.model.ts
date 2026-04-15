export interface Cliente {
  id: number;
  nome: string;
  email: string;
  tipo: 'PF' | 'PJ' | 'VIP';
  ativo: boolean;
  criado_em: string;
}

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}
