import { expect } from '@playwright/test';
import { SearchPage } from './SearchPage.js';

export class DocumentBasic extends SearchPage {
  constructor(page) {
    super(page);
    this.createButton = page.getByRole('button', { name: '新規' });
    this.createFolderItem = page.getByText('新しいフォルダを作成', { exact: true });
    this.nameInput = page.getByPlaceholder('ファイル名を入力');
    this.saveButton = page.getByRole('button', { name: '保存' });
    this.renameItem = page.getByText('名前を変更');
  }

  folderByName(name) {
    return this.page.locator(`[title="${name}"]`);
  }

  async openCreateFolderDialog() {
    await this.createButton.click();
    await this.createFolderItem.click();
  }

  async createFolder(name) {
    await this.openCreateFolderDialog();
    await this.nameInput.fill(name);
    await this.saveButton.click();
    return name;
  }

  async searchFolder(keyword) {
    await this.searchBox.fill(keyword);
    await expect(this.searchBox).toHaveValue(keyword);
    await this.searchButton.click();
  }

  async renameFolder(folderName, newName) {
    const row = this.resultRows.filter({ has: this.folderByName(folderName) });
    await expect(async () => {
      await row.getByRole('button', { name: 'その他' }).click();
      await expect(this.renameItem).toBeVisible({ timeout: 2000 });
    }).toPass({ timeout: 15000 });
    await this.renameItem.click();
    await this.nameInput.fill(newName);
    await this.saveButton.click();
  }
}
