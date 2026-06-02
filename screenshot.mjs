import puppeteer from 'puppeteer';
import { mkdir, readdir } from 'fs/promises';
import { join } from 'path';

const url = process.argv[2] || 'http://localhost:3000';
const label = process.argv[3] || '';
const dir = './temporary screenshots';

await mkdir(dir, { recursive: true });
const files = await readdir(dir);
const n = files.filter(f => f.startsWith('screenshot-')).length + 1;
const name = label ? `screenshot-${n}-${label}.png` : `screenshot-${n}.png`;

const browser = await puppeteer.launch({
  executablePath: 'C:/Users/konra/.cache/puppeteer/chrome/win64-146.0.7680.153/chrome-win64/chrome.exe',
  headless: true,
});
const page = await browser.newPage();

if (label === 'mobile') {
  await page.setViewport({ width: 390, height: 844 });
} else {
  await page.setViewport({ width: 1440, height: 900 });
}

await page.goto(url, { waitUntil: 'networkidle0', timeout: 15000 });
await page.screenshot({ path: join(dir, name), fullPage: true });
await browser.close();
console.log(`Saved: ${join(dir, name)}`);
