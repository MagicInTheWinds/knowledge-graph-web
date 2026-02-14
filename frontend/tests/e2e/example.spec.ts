import { test, expect } from '@playwright/test';

test('homepage has correct title', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/Create Next App/);
});

test('health check api connectivity', async ({ request }) => {
  // Assuming backend is running locally
  const response = await request.get('/api/health');
  expect(response.ok()).toBeTruthy();
  const json = await response.json();
  expect(json).toEqual({ status: 'ok', service: 'knowledge-graph-api' });
});