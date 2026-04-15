export interface Cliente {
  id: number;
  nome: string;
  email: string;
  tipo: 'PF' | 'PJ' | 'VIP';
  ativo: boolean;
  criado_em: string;
}
