const fs = require('fs');
const path = require('path');
function findRepository(filePath, workspacePath) {
 if (!filePath) return workspacePath;
 let dir = path.dirname(filePath);
 while (true) {
  if (fs.existsSync(path.join(dir, '.git'))) return dir;
  const parent = path.dirname(dir);
  if (parent === dir) break;
  dir = parent;
 }
 return workspacePath;
}
module.exports = { findRepository };
