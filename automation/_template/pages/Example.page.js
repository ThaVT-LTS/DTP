// Mẫu Page Object: mỗi màn một class; locator khai báo ở constructor, thao tác là phương thức.
// Locator lấy từ nhãn nguyên văn trong test basis (rules/automation.md rule 3).
export class ExamplePage {
  constructor(page) {
    this.page = page;
    // this.searchBox = page.getByRole('textbox', { name: /…/ });
  }
}
