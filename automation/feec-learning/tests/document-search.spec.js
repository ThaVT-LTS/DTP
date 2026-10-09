import { test, expect } from '@playwright/test';
import { SearchPage } from '../pages/SearchPage.js';
import { DOCUMENTS_URL } from '../fixtures/testdata.js';

test.describe('Documents · Tìm kiếm', { tag: ['@legacy', '@documents', '@search'] }, () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(DOCUMENTS_URL);
  });

  test('LEARN-DOC-SEARCH-001 · Từ khóa hợp lệ trả về kết quả', async ({ page }) => {
    const search = new SearchPage(page);
    await search.searchFor('1');
    await expect(search.resultRows).not.toHaveCount(0);
  });

  test('LEARN-DOC-SEARCH-002 · Từ khóa không tồn tại thì không có kết quả', async ({ page }) => {
    const search = new SearchPage(page);
    await search.searchFor('1ABC1ABC');
    await expect(search.resultRows).toHaveCount(0);
  });

  test('LEARN-DOC-SEARCH-003 · Hiện icon clear sau khi nhập từ khóa', async ({ page }) => {
    const search = new SearchPage(page);
    await expect(search.clearIcon).not.toBeVisible();
    await search.searchBox.fill('1');
    await expect(search.clearIcon).toBeVisible();
  });
});
