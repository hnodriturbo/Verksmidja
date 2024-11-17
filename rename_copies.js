const fs = require('fs');
const path = require('path');

// Define the root directory to process (current folder where the script is located)
const rootFolder = __dirname;

// Function to recursively process files and folders
function processFolder(folderPath) {
  const items = fs.readdirSync(folderPath, { withFileTypes: true });

  for (const item of items) {
    const fullPath = path.join(folderPath, item.name);

    if (item.isDirectory()) {
      // Recursively process subfolders
      processFolder(fullPath);
    } else if (item.isFile()) {
      // Check for " - Copy" and "_- Copy" patterns
      /*       const copyPatterns = [
        { regex: / - Copy(\.[^.]*)$/, replacement: '$1' }, // Handles " - Copy"
        { regex: /_- Copy(\.[^.]*)$/, replacement: '$1' }, // Handles "_- Copy"
      ]; */
      const copyPatterns = [
        { regex: / - Copy(\.[^.]*)?$/, replacement: '$1' }, // Matches " - Copy" (with or without an extension)
        { regex: /_- Copy(\.[^.]*)?$/, replacement: '$1' }, // Matches "_- Copy" (with or without an extension)
      ];
      let renamed = false;

      for (const pattern of copyPatterns) {
        if (pattern.regex.test(item.name)) {
          const newName = item.name.replace(pattern.regex, pattern.replacement);
          const newPath = path.join(folderPath, newName);

          if (fs.existsSync(newPath)) {
            // Conflict detected: Rename to " - MyCopy"
            const myCopyName = item.name
              .replace(/ - Copy/, ' - MyCopy')
              .replace(/_- Copy/, ' - MyCopy');
            const myCopyPath = path.join(folderPath, myCopyName);
            fs.renameSync(fullPath, myCopyPath);
            console.log(
              `Renamed to avoid conflict: ${item.name} -> ${myCopyName}`
            );
          } else {
            // Rename to the original name
            fs.renameSync(fullPath, newPath);
            console.log(`Renamed: ${item.name} -> ${newName}`);
          }

          renamed = true;
          break; // Stop checking other patterns for this file
        }
      }

      if (!renamed) {
        console.log(`Skipped: ${item.name}`);
      }
    }
  }
}

// Start the processing
try {
  console.log(`Starting to process folder: ${rootFolder}`);
  processFolder(rootFolder);
  console.log('Renaming complete!');
} catch (error) {
  console.error('An error occurred:', error);
}
