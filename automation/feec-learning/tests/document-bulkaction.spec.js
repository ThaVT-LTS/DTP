import { test, expect } from '@playwright/test';
import { BulkAction } from '../pages/BulkAction.js';
import { DOCUMENTS_URL } from '../fixtures/testdata.js';

test.describe('Documents · Thao tác hàng loạt', { tag: ['@legacy', '@documents', '@bulk'] }, () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(DOCUMENTS_URL);
  });

  test('LEARN-DOC-BULK-001 · Tải 2 dòng đã chọn', async ({ page }) => {
    const bulk = new BulkAction(page);
    await bulk.checkFirstRows(2);
    await bulk.download();
    await expect(page.getByText('2件のファイルもしくはフォルダのダウンロードを開始しました。')).toBeVisible();
  });

  // Hai test dưới đã bị comment ở bản cũ; chuyển thành fixme để còn truy vết.
  // Cần dữ liệu tự tạo trong test (hiện đang dùng file có sẵn, sẽ bị mất sau khi chạy).
  test.fixme('LEARN-DOC-BULK-002 · Di chuyển 2 dòng vào folder A (cần dữ liệu tự tạo)', async ({ page }) => {
    const bulk = new BulkAction(page);
    await bulk.checkRow('25_03_18 (8).txt');
    await bulk.checkRow('25_03_18 (7).txt');
    await bulk.moveBulkAction();
    await bulk.selectDestinationFolder('A');
    await bulk.confirmMove();
    await expect(page.locator('tbody tr').filter({ hasText: '25_03_18 (8).txt' })).toHaveCount(0);
  });

  test.fixme('LEARN-DOC-BULK-003 · Xoá 2 dòng đã chọn thì biến mất khỏi bảng (cần dữ liệu tự tạo)', async ({ page }) => {
    const bulk = new BulkAction(page);
    await bulk.checkRow('25_03_18 (5).txt');
    await bulk.checkRow('25_03_18 (2).txt');
    await bulk.moveToTrash();
    await expect(page.locator('tbody tr').filter({ hasText: '25_03_18 (5).txt' })).toHaveCount(0);
    await expect(page.locator('tbody tr').filter({ hasText: '25_03_18 (2).txt' })).toHaveCount(0);
  });
});
