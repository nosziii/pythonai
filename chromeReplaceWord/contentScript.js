const replaceWords = async () => {
    // Beállítások betöltése
    const settings = await loadSettings();
  
    if (!settings.wordToReplace || !settings.replacementWord) {
      return;
    }
  
    // Szavak kicserélése
    const elements = document.getElementsByTagName('*');
    for (let i = 0; i < elements.length; i++) {
      const element = elements[i];
      for (let j = 0; j < element.childNodes.length; j++) {
        const node = element.childNodes[j];
        if (node.nodeType === 3) {
          const text = node.nodeValue;
          const replacedText = text.split(settings.wordToReplace).join(settings.replacementWord);
          if (replacedText !== text) {
            element.replaceChild(document.createTextNode(replacedText), node);
          }
        }
      }
    }
  };
  
  const loadSettings = () => {
    return new Promise((resolve, reject) => {
      chrome.storage.sync.get(['wordToReplace', 'replacementWord'], (result) => {
        resolve(result);
      });
    });
  };
  
  // A szavak kicserélése a betöltött oldalon
  replaceWords();
  