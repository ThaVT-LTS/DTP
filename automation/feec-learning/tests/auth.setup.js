import { test as setup, expect } from '@playwright/test';

const authFile = 'playwright/.auth/user.json';

setup('Đăng nhập và lưu phiên làm việc', async ({ page }) => {
  const { E2E_USER, E2E_PASSWORD } = process.env;
  if (!E2E_USER || !E2E_PASSWORD) throw new Error('Thiếu E2E_USER / E2E_PASSWORD trong .env');

  await page.goto('/auth/login');
  await page.getByRole('textbox', { name: 'メールアドレス / ユーザーID' }).fill(E2E_USER);
  await page.getByRole('textbox', { name: 'パスワード' }).fill(E2E_PASSWORD);
  await page.getByRole('button', { name: 'ログイン', exact: true }).click();
  await expect(page).toHaveURL(/projects/, { timeout: 15000 });

  await page.context().storageState({ path: authFile });
});
