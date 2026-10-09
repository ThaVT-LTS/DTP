export class SearchPage {
  constructor(page) {
    this.page = page;
    this.searchBox = page.getByRole('textbox', { name: /検索/ });
    this.searchButton = page.getByRole('button', { name: '検索', exact: true });
    this.clearIcon = page.getByRole('button', { name: '検索文字をクリア' });
    this.resultRows = page.locator('tbody tr');
  }

  async searchFor(keyword) {
    await this.searchBox.fill(keyword);
    await this.searchButton.click();
    // Không dùng networkidle: trang này luôn có request nền nên không bao giờ "idle".
    // Kết quả được chờ bằng web-first assertion ở test.
    await this.page.waitForLoadState('domcontentloaded');
  }
}
