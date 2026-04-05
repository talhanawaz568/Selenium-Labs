const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    // 1. Launch browser with Cloud-friendly arguments
    const browser = await puppeteer.launch({
        headless: "new",
        args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
    });

    const page = await browser.newPage();

    // 2. Define the path to your local HTML file
    const filePath = `file://${path.join(__dirname, 'index.html')}`;
    console.log(`Loading: ${filePath}`);
    await page.goto(filePath);

    // 3. Select a radio button
    // Selector: input with name 'fruit' and value 'banana'
    await page.click('input[name="fruit"][value="banana"]');
    console.log('Action: Selected radio "Banana"');

    // 4. Select checkboxes
    await page.click('input[name="hobbies"][value="reading"]');
    await page.click('input[name="hobbies"][value="travelling"]');
    console.log('Action: Selected checkboxes "Reading" and "Travelling"');

    // 5. Validation: Gather the state of all checked inputs
    const selectedValues = await page.evaluate(() => {
        const checkedElements = Array.from(document.querySelectorAll('input:checked'));
        return checkedElements.map(el => `${el.type}: ${el.value}`);
    });

    console.log('\n--- Lab Verification ---');
    console.log('Currently checked items:', selectedValues.join(', '));
    console.log('------------------------\n');

    // 6. Close the browser
    await browser.close();
    console.log('Browser closed.');
})();
