import { writable } from 'svelte/store';

export const isAuthenticated = writable(false);
export const control = writable(false);
export const org = writable(false);