import { client } from "$lib/openapi";

export const load= async () => {
    client.setConfig({baseUrl: "/api/v1"})
}