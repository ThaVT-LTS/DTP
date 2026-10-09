import { test, expect } from '@playwright/test';

test('LEARN-LOGIN-001 · Đăng nhập và mở trang Projects', { tag: ['@legacy', '@login'] }, async ({ page }) => {
  await page.goto('/auth/login');
  await page.getByRole('textbox', { name: 'メールアドレス / ユーザーID' }).fill(process.env.E2E_USER);
  await page.getByRole('textbox', { name: 'パスワード' }).fill(process.env.E2E_PASSWORD);
  await page.getByRole('button', { name: 'ログイン', exact: true }).click();
  await expect(page).toHaveURL(/projects/);
});
