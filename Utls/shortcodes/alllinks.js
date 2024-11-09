/*
OBSIDIAN SHORTCODE: group-links-by-month-year.js
Description: Reads a JSON file containing links and outputs Markdown that lists the links grouped by month and year.
Usage: [[group-links-by-month-year path/to/file.json]]
*/

const fs = require('fs');
const path = require('path');

module.exports = async (params, el) => {
  const jsonFile = params[0];
  const jsonPath = path.join(app.vault.configDir, jsonFile);

  try {
    const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    const linksByMonth = groupLinksByMonth(data.links);

    let output = '';
    for (const [monthYear, links] of Object.entries(linksByMonth)) {
      output += `\n## ${monthYear}\n\n`;
      links.forEach(link => {
        output += `- [${link.text}](${link.href})\n`;
      });
    }

    el.createEl('pre', { text: output.trim() });
  } catch (err) {
    el.createEl('span', { text: `Error: ${err.message}` });
  }
};

function groupLinksByMonth(links) {
  const linksByMonth = {};
  links.forEach(link => {
    const [year, month] = link.date.split('-').slice(0, 2);
    const monthYear = `${year}-${month}`;
    if (!linksByMonth[monthYear]) {
      linksByMonth[monthYear] = [];
    }
    linksByMonth[monthYear].push(link);
  });
  return linksByMonth;
}