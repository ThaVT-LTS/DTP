import { test, expect } from '@playwright/test';
import { DocumentBasic } from '../pages/DocumentBasic.js';
import { DOCUMENTS_URL, uniqueName } from '../fixtures/testdata.js';

// Lưu ý: chưa có bước dọn dữ liệu (xoá folder sau test) vì luồng xoá chưa được xác nhận.
// Mỗi lần chạy tạo folder tên duy nhất nên không trùng dữ liệu cũ.
test.describe('Documents · Tạo, tìm, sửa tên folder', { tag: ['@legacy', '@documents', '@folder'] }, () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(DOCUMENTS_URL);
  });

  test('LEARN-DOC-FOLDER-001 · Tạo folder', async ({ page }) => {
    const doc = new DocumentBasic(page);
    await doc.openCreateFolderDialog();
    await expect(page.getByText('フォルダを作成', { exact: true })).toBeVisible();
    await expect(doc.nameInput).toBeVisible();

    const name = uniqueName('FOLDER');
    await doc.nameInput.fill(name);
    await doc.saveButton.click();
    await expect(doc.folderByName(name)).toBeVisible();
  });

  test('LEARN-DOC-FOLDER-002 · Tìm folder đã tạo', async ({ page }) => {
    const doc = new DocumentBasic(page);
    const name = await doc.createFolder(uniqueName('FOLDER'));
    await expect(doc.folderByName(name)).toBeVisible();

    await doc.searchFolder(name);
    await expect(doc.folderByName(name)).toBeVisible();
  });

  test('LEARN-DOC-FOLDER-003 · Sửa tên folder đã tạo', async ({ page }) => {
    const doc = new DocumentBasic(page);
    const name = await doc.createFolder(uniqueName('FOLDER'));
    await expect(doc.folderByName(name)).toBeVisible();

    await doc.searchFolder(name);
    await expect(doc.folderByName(name)).toBeVisible();

    const newName = uniqueName('RENAMED');
    await doc.renameFolder(name, newName);
    await expect(doc.folderByName(newName)).toBeVisible();
  });
});
