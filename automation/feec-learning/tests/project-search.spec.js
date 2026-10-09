import { test, expect } from '@playwright/test';
import { SearchPage } from '../pages/SearchPage.js';
import { PROJECTS_URL, EXISTING_PROJECT_KEYWORD } from '../fixtures/testdata.js';

test.describe('Projects · Tìm kiếm', { tag: ['@legacy', '@projects', '@search'] }, () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(PROJECTS_URL);
  });

  test('LEARN-PRJ-SEARCH-001 · Từ khóa hợp lệ trả về kết quả', async ({ page }) => {
    const search = new SearchPage(page);
    await search.searchFor(EXISTING_PROJECT_KEYWORD);
    await expect(search.resultRows).not.toHaveCount(0);
  });

  // Bản cũ assert not.toHaveCount(0) trái với tên test. Không đoán kết quả mong đợi: chờ người dùng xác nhận.
  test.fixme('LEARN-PRJ-SEARCH-002 · Từ khóa không tồn tại (Q-AUTO-01: màn Projects hiển thị gì khi không có kết quả?)', async ({ page }) => {
    const search = new SearchPage(page);
    await search.searchFor('1ABC1ABC');
    // TODO(Q-AUTO-01): assert theo hành vi đúng sau khi được xác nhận.
  });

  test('LEARN-PRJ-SEARCH-003 · Hiện icon clear sau khi nhập từ khóa', async ({ page }) => {
    const search = new SearchPage(page);
    await expect(search.clearIcon).not.toBeVisible();
    await search.searchBox.fill('1');
    await expect(search.clearIcon).toBeVisible();
  });

  test('LEARN-PRJ-SEARCH-004 · Placeholder ô tìm kiếm chứa 検索', async ({ page }) => {
    const search = new SearchPage(page);
    await expect(search.searchBox).toHaveAttribute('placeholder', /検索/);
  });
});
