import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { App } from './app/app';

// Ponto de entrada da aplicação Angular, onde o componente principal App é bootstrapped com a configuração global definida em appConfig
bootstrapApplication(App, appConfig)
  .catch((err) => console.error(err));
