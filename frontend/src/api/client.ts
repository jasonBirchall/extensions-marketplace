import axios from 'axios';
import type { Extension, Review, ModerationFlag } from '../types';

// base url for the django api
const API_BASE_URL = 'http://localhost:8000/api';

// create an axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// api functions
export const extensionsApi = {
  // GET /api/extensions/
  list: async () => {
    const response = await apiClient.get<Extension[]>('/extensions/');
    return response.data.results;
  },

  // GET /api/extensions/:id/
  get: async (id: number) => {
    const response = await apiClient.get<Extension[]>(`/extensions/${id}/`);
    return response.data;
  },

  // GET /api/extensions/pending/
  getPending: async () => {
    const response = await apiClient.get<Extension[]>('/extensions/pending/');
    return response.data;
  },

  // POST /api/extensions
  create: async (data: FormData) => {
    const response = await apiClient.post<Extension[]>('/extensions/', data, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },
}

export const reviewsApi = {
  list: async () => {
    const response = await apiClient.get<Review[]>('/reviews/');
    return response.data;
  },

  create: async (review: Partial<Review>) => {
    const response = await apiClient.post<Review>('/reviews/', review);
    return response.data;
  },
};

export const flagsApi = {
  list: async () => {
    const response = await apiClient.get<ModerationFlag[]>('/flags/');
    return response.data;
  },
};
