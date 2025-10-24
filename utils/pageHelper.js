class PageHelper {
    constructor(page) {
        this.page = page;
    }

    async scrollToTextInContainer(containerSelector, text) {
        const element = this.page.locator(`${containerSelector} >> text=${text}`);
        await element.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
    }
}

module.exports = PageHelper;