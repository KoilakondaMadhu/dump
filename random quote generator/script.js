const quoteContainer = document.querySelector('.quote');
const newQuoteButton = document.getElementById('new-quote-btn');

async function fetchRandomQuote() {
  try {
    const response = await fetch('https://type.fit/api/quotes');
    const data = await response.json();
    const randomIndex = Math.floor(Math.random() * data.length);
    const randomQuote = data[randomIndex];
    displayQuote(randomQuote.text, randomQuote.author);
  } catch (error) {
    console.error('Error fetching quote:', error);
  }
}

function displayQuote(text, author) {
  const quoteText = document.createElement('p');
  quoteText.textContent = `"${text}"`;
  const quoteAuthor = document.createElement('p');
  quoteAuthor.textContent = `- ${author || 'Unknown'}`;
  
  // Clear previous quote
  quoteContainer.innerHTML = '';
  
  quoteContainer.appendChild(quoteText);
  quoteContainer.appendChild(quoteAuthor);
}

// Initial quote load
fetchRandomQuote();

// Add event listener to the "New Quote" button
newQuoteButton.addEventListener('click', fetchRandomQuote);
