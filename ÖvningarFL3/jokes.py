import random, numpy as np

programming_jokes = np.array([
  "Why don't programmers like nature? It has too many bugs.",
  "Why did the CSS developer go to therapy? To get rid of his margins.",
  "How do you comfort a JavaScript developer? You console them.",
  "Why did the CSS developer leave the restaurant? Because it had no class.",
  "Why did the JavaScript developer go missing? Because he didn't know when to return.",
  "Why did the HTML tag go to the party? Because it wanted to break the line.",
  "Why do JavaScript developers wear glasses? Because they don't C#.",
  "Why don't programmers like to use inline styles? Because they want to be classy.",
  "Why did the CSS selector break up with the HTML element? It found someone more specific.",
  "Why did the CSS developer apply for a job? They wanted to get a position.",
])

print(np.random.choice(programming_jokes, size=2, replace=False))
