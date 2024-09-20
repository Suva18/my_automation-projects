// tests/pageContent.spec.ts
import { test, expect } from '@playwright/test';

test('verify page content', async ({ page }) => {
  await page.goto('https://example.com');
  const content = await page.textContent('h1');
  expect(content).toBe('Example Domain');
});
