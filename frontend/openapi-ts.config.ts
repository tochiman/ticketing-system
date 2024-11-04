import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
  client: '@hey-api/client-fetch',
  input: 'http://backend:8080/openapi.json',
  output: 'src/lib/openapi',
  plugins: [
    '@hey-api/schemas',
    '@hey-api/types',
    {
      asClass: true,
      name: '@hey-api/services',
    },
  ]
});