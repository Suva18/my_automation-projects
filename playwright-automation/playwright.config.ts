import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30000,
  expect: {
    timeout: 5000
  },
  fullyParallel: true,
  retries: 1,
  reporter: [['html', { outputFolder: 'playwright-report', open: 'never' }]],
  projects: [
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'], headless: true },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'], headless: true },
    },
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'], headless: true },
    },
    {
        name: 'chrome',
        use: { ...devices['Desktop Chrome'], headless: true },
    },
    {
        name: 'edge',
        use: { ...devices['Desktop Edge'], headless: true },
    },
  ],
  use: {
    headless: true,
    actionTimeout: 0,
    trace: 'on-first-retry',
  },
});
