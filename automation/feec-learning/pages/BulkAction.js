export class BulkAction {
  constructor(page) {
    this.page = page;
    this.trashButton = page.getByRole('button', { name: '削除' });
    this.confirmDelete = page.getByRole('button', { name: 'ごみ箱に移動' });
    this.downloadButton = page.getByRole('button', { name: 'ダウンロード' });
    this.moveButton = page.getByRole('button', { name: '移動' });
  }

  async checkRow(fileName) {
    const row = this.page.locator('tbody tr').filter({ hasText: fileName });
    await row.getByRole('checkbox').check();
  }

  async checkFirstRows(count) {
    const rows = this.page.locator('tbody tr');
    await rows.first().waitFor();
    for (let i = 0; i < count; i++) await rows.nth(i).getByRole('checkbox').check();
  }

  async download() {
    await this.downloadButton.click();
  }

  async moveBulkAction() {
    await this.moveButton.click();
  }

  async moveToTrash() {
    await this.trashButton.click();
    await this.confirmDelete.click();
  }

  async selectDestinationFolder(folderName) {
    await this.page.getByRole('dialog').getByText(folderName, { exact: true }).click();
  }

  async confirmMove() {
    await this.page.getByRole('dialog').getByRole('button', { name: '移動' }).click();
  }
}
