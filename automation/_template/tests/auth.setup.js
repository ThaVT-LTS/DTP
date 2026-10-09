import { test as setup, expect } from '@playwright/test';

const authFile = 'playwright/.auth/user.json';

setup('Đăng nhập và lưu phiên làm việc', async ({ page }) => {
  const { E2E_USER, E2E_PASSWORD } = process.env;
  if (!E2E_USER || !E2E_PASSWORD) throw new Error('Thiếu E2E_USER / E2E_PASSWORD trong .env');

  await page.goto('/login'); // TODO: đường dẫn trang đăng nhập của dự án
  // TODO: điền tên đăng nhập, mật khẩu, bấm nút đăng nhập bằng locator theo nhãn
  // await expect(page).toHaveURL(/…/);

  await page.context().storageState({ path: authFile });
});
