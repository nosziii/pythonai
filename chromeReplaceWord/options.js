document.getElementById('saveButton').addEventListener('click', saveSettings);
document.addEventListener('DOMContentLoaded', loadSettings);

async function saveSettings() {
  const wordToReplace = document.getElementById('wordToReplace').value;
  const replacementWord = document.getElementById('replacementWord').value;

  await chrome.storage.sync.set({ wordToReplace, replacementWord });

  alert('A beállítások sikeresen mentve!');
}

function loadSettings() {
  chrome.storage.sync.get(['wordToReplace', 'replacementWord'], (result) => {
    document.getElementById('wordToReplace').value = result.wordToReplace || '';
    document.getElementById('replacementWord').value = result.replacementWord || '';
  });
}
