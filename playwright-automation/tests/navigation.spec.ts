// tests/navigation.spec.ts
import { test, expect } from '@playwright/test';

test('verify navigation', async ({ page }) => {
  await page.goto('https://example.com');
  await page.click('a'); // Assuming there is a link to click
  await expect(page).toHaveURL('https://www.iana.org/domains/reserved');
});
