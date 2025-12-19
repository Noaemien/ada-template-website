---
layout: default
title: Betting Floor
---

# The Betting Floor

What is a World Cup without high stakes?

Before the first match is played, predictions are already circulating.  
Since the outcome of the tournament is uncertain, and the Wikispeedia navigation data is not publicly accessible, bets must be placed under imperfect information.

On the betting floor, one group sets the odds.  
Another decides whether to trust them.

---


## The Bookmakers : Setting the Odds

To do so, the bookmakers scrapped the whole wikipedia website to extract a graph architecture from it. (they unfortunately do not have access at the Wikispeedia players game data so they cannot predict perfectly the outcome of the competition)
To estimate the importance of a node to build a graph we usually use centrality measure. Bookmakers here mainly relied on Betweenness and Katz centrality measures.
Here are the 64 most important nodes using those measures.hidden at this stage of the competition.

From those two mesures we can extract 2 visual graphs of the wikipedia architecture

<!-- Placeholder: maybe how we turn pageviews into odds -->

## The Odds Board

Based on those two metrics, Bookmakers will now give an odd for every Node so player can put their money on their favourite choice depending on their predictions. These odds reflect **expectations**, not outcomes.

### Strategy: Selective Normalization
To account for a bookmaker's margin and filter out the "long tail" of 4,000 competitors, we calculate the total market weight based only on the **Top 64** performers. 

This creates in the same time an **overround** for the bookmakers and simplify the calculations: since we divide individual scores by a smaller total sum, the implied probabilities will sum to more than 100% across the entire dataset, effectively lowering the odds.

#### The Mathematical Model
1. **Composite Score ($S_i$):**
   $$S_i = \frac{C_{B,i} + C_{K,i}}{2}$$

2. **Top-100 Reference Sum ($\Sigma_{top}$):**
   $$\Sigma_{top} = \sum_{j=1}^{100} S_j$$

3. **Modified Probability ($P'_i$):**
   $$P'_i = \frac{S_i}{\Sigma_{top}}$$

4. **Final Bookmaker Odds ($O_i$):**
   $$O_i = \frac{1}{P'_i}$$

this are the odds measured with this technique :

| Rank | Article           | Odds      |
|:----:|:-----------------|:---------:|
| 1    | United States     | 7.11      |
| 2    | United Kingdom    | 15.79     |
| 3    | England           | 20.65     |
| 4    | Europe            | 24.80     |
| 5    | Africa            | 27.65     |
| 6    | Germany           | 34.48     |
| 7    | World War II      | 43.18     |
| 8    | 19th century      | 45.15     |
| 9    | London            | 45.61     |
| 10   | English language  | 47.67     |

While selective normalization establishes a bookmaker's margin, treating Betweenness and Katz scores as direct probabilities is mathematically flawed for 1v1 strength data. Centrality measures relative structural influence, not win frequency. To resolve this, we implement a Bradley-Terry inspired model: by applying an exponential transformation to the scores, we convert raw "ability" into "winning potential." This transition is crucial because it accounts for the non-linear nature of competition, where elite performers possess a disproportionate advantage that a simple linear model would fail to capture

## Bradley-Terry Inspired Odds Model
Since **Betweenness** and **Katz** are measures of 1v1 strength (centrality) rather than direct win probabilities, we treat them as **Ability Scores** ($\lambda$). 

To convert these scores into betting odds for a multi-competitor field, we use an exponential transformation. This ensures that the difference in strength between two competitors is reflected proportionally in the odds.

#### The Mathematical Model
1. **Ability Score ($\lambda_i$):**
   A weighted average of the centrality metrics:
   $$\lambda_i = \frac{C_{B,i} + C_{K,i}}{2}$$

2. **Winning Potential ($W_i$):**
   We use the exponential function to ensure all potentials are positive and to amplify the gap between elite and average competitors:
   $$W_i = e^{\beta \cdot \lambda_i}$$
   *(Where $\beta$ is a scaling factor. A higher $\beta$ makes the "favorites" stronger).*

3. **Normalization (Top-100 Margin):**
   We calculate the total potential based on the top 100 competitors to create the bookmaker's margin:
   $$\Omega_{top} = \sum_{j=1}^{100} W_j$$

4. **Implied Probability and Odds:**
   $$P_i = \frac{W_i}{\Omega_{top}} \quad \text{and} \quad \text{Odds}_i = \frac{1}{P_i}$$

### Problem : 
The bookmaker doesnt know the insights of the real competition so he cannot know how to adjust beta. That is why he employs a "Market Anchor" strategy. Rather than guessing the internal skill distribution (β), the model is back-calculated by forcing the top-ranked favorite’s winning odds to exactly 8.00. By then dividing all odds by eight to create a "Top 8" market, the favorite is naturally positioned at 1.00 (100% implied probability). This approach effectively standardizes the risk profile: it treats the structural leader as a certainty for the Top 8 while allowing the exponential scaling to dictate the decreasing probabilities for the rest of the field in a mathematically consistent way.
In addition, trying to guess the top8 is deffinitely funnier for the gamblers !

# Betting area

Now you step onto the betting floor.

As a **gambler**, you only have access to public information:  
what you know, what your intuition suggest you, and what the odds suggest.

Will you trust global fame?  
Or will you go for a promising outsider and go against the bookmakers ?  

<p>Select your own favourite hub 8 articles: (you have 80$ and must bet 10$ on each article you think will be in the top 8 of the world cup of hubs)</p>

<div class="container" id="optionsContainer"></div>
<button onclick="saveSelection()">Save</button>

<h3>Your selections:</h3>
<ul id="selectionList"></ul>

<script>
// List of articles with their odds
const articles = [
  { name: "United_States", odd: 1.00 },
  { name: "United_Kingdom", odd: 3.36 },
  { name: "Europe", odd: 4.34 },
  { name: "England", odd: 5.09 },
  { name: "France", odd: 5.23 },
  { name: "Germany", odd: 5.75 },
  { name: "World_War_II", odd: 6.07 },
  { name: "Africa", odd: 6.99 },
  { name: "English_language", odd: 7.01 },
  { name: "India", odd: 7.32 },
  { name: "Japan", odd: 7.44 },
  { name: "London", odd: 7.61 },
  { name: "Australia", odd: 7.88 },
  { name: "Canada", odd: 8.03 },
  { name: "Russia", odd: 8.05 },
  { name: "Italy", odd: 8.20 },
  { name: "Spain", odd: 8.28 },
  { name: "China", odd: 8.35 },
  { name: "Latin", odd: 9.26 },
  { name: "World_War_I", odd: 9.51 },
  { name: "19th_century", odd: 9.62 },
  { name: "Asia", odd: 9.70 },
  { name: "United_Nations", odd: 9.74 },
  { name: "North_America", odd: 9.76 },
  { name: "Animal", odd: 9.80 },
  { name: "Time_zone", odd: 9.89 },
  { name: "Earth", odd: 9.95 },
  { name: "Netherlands", odd: 9.99 },
  { name: "Scientific_classification", odd: 10.01 },
  { name: "Islam", odd: 10.14 },
  { name: "Scotland", odd: 10.23 },
  { name: "Christianity", odd: 10.36 },
  { name: "Egypt", odd: 10.36 },
  { name: "Paris", odd: 10.43 },
  { name: "20th_century", odd: 10.49 },
  { name: "French_language", odd: 10.52 },
  { name: "Soviet_Union", odd: 10.54 },
  { name: "Currency", odd: 10.57 },
  { name: "List_of_countries_by_system_of_government", odd: 10.59 },
  { name: "Atlantic_Ocean", odd: 10.60 },
  { name: "Portugal", odd: 10.62 },
  { name: "South_Africa", odd: 10.63 },
  { name: "People's_Republic_of_China", odd: 10.69 },
  { name: "Sweden", odd: 10.76 },
  { name: "New_Zealand", odd: 10.77 },
  { name: "Ireland", odd: 10.81 },
  { name: "European_Union", odd: 10.90 },
  { name: "New_York_City", odd: 11.08 },
  { name: "Poland", odd: 11.09 },
  { name: "Agriculture", odd: 11.26 },
  { name: "Greece", odd: 11.37 },
  { name: "Turkey", odd: 11.40 },
  { name: "Jew", odd: 11.40 },
  { name: "South_America", odd: 11.41 },
  { name: "Middle_Ages", odd: 11.44 },
  { name: "Mexico", odd: 11.49 },
  { name: "Bird", odd: 11.52 },
  { name: "Argentina", odd: 11.53 },
  { name: "Israel", odd: 11.53 },
  { name: "Roman_Catholic_Church", odd: 11.54 },
  { name: "Brazil", odd: 11.58 },
  { name: "California", odd: 11.58 },
  { name: "Water", odd: 11.65 },
  { name: "Belgium", odd: 11.67 }
];

// Generate checkboxes
const container = document.getElementById("optionsContainer");
articles.forEach(article => {
  const div = document.createElement("div");
  div.className = "option";
  div.innerHTML = `
    <label>
      <input type="checkbox" value="${article.name}" data-odd="${article.odd}" onclick="limitSelection(this)">
      ${article.name.replace(/_/g, ' ')} - ${article.odd.toFixed(2)}
    </label>
  `;
  container.appendChild(div);
});

// Limit to 8 selections
function limitSelection(checkbox) {
  const checked = document.querySelectorAll('#optionsContainer input:checked');
  if (checked.length > 8) {
    alert("You can select up to 8 articles only!");
    checkbox.checked = false;
  }
}

// Save selections
function saveSelection() {
  const selected = Array.from(document.querySelectorAll('#optionsContainer input:checked'))
                        .map(input => `${input.value.replace(/_/g, ' ')} - ${parseFloat(input.dataset.odd).toFixed(2)}`);
  const list = document.getElementById("selectionList");
  list.innerHTML = "";
  selected.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item;
    list.appendChild(li);
  });

  console.log("Selections saved:", selected);
}
</script>

<style>
.container { display: flex; flex-wrap: wrap; max-width: 800px; }
.option { width: 250px; margin-bottom: 5px; }
button { margin-top: 20px; padding: 8px 20px; font-size: 16px; cursor: pointer; }
h3 { margin-top: 30px; }
ul { margin-top: 10px; }
</style>


---

### Now, let's explore some betting strategies

We always assume you have 80 $ and bet 10 $ on each of 8 articles.

#### Strategy 1 – Follow the bookmakers

If someone simply follows the odds given by the bookmakers on the real competition, they would win on:

- **United States** (1.00)
- **United Kingdom** (3.36)
- **World War II** (6.07)

Total return:

- `10 × (1.00 + 3.36 + 6.07) = 10 × 10.43 = 104.3 $`
- Profit: `104.3 $ − 80 $ = 24.3 $`

#### Strategy 2 – Perfectly predict the Top 8 hubs

If someone predicted the 8 best hubs (including one article not even offered by the bookmakers):

- Bettable picks from the list:  
  **United States, Russia, South Africa, United Kingdom, Israel, China, Germany**
- Plus **Adolf Hitler**, who was **not** proposed by the bookmakers (so no bet could be placed on it)

The return from the 7 bettable winners would be:

- `10 × (1.00 + 8.05 + 10.63 + 3.36 + 11.53 + 8.35 + 5.75) = 486.7 $`
- Profit: `486.7 $ − 80 $ = 406.7 $`

This highlights how much value there was in “underdogs” and in articles that the bookmaker did not even list.

#### Strategy 3 – Use global popularity

Now consider a different idea: pick the top 8 most popular pages on Wikipedia over the last 10 years.  
These are **not** the same as the nodes favored by the Wikipedia link architecture, so the overlap with the bookmaker’s list is limited.

| Article            |
|--------------------|
| United States      |
| Wikipedia          |
| India              |
| Google             |
| World War II       |
| Adolf Hitler       |
| United Kingdom     |
| Barack Obama       |
| World War I        |
| Michael Jordan     |
| Winston Churchill  |
| China              |
| Elvis Presley      |
| Canada             |
| Australia          |

From the bookmaker’s offered list, a player using this strategy would select:

- **United States, India, World War II, United Kingdom, World War I, China, Canada, Australia**

Among these, the actual winners are:

- **United States** (1.00)
- **India** (7.32)
- **World War II** (6.07)
- **United Kingdom** (3.36)
- **China** (8.35)

Total return:

- `10 × (1.00 + 7.32 + 6.07 + 3.36 + 8.35) = 261 $`
- Profit: `261 $ − 80 $ = 181 $`

This strategy clearly outperforms the one directly following the bookmakers’ odds. It shows that using **page popularity** can be more reliable for predicting players’ behavior than relying only on the **graph architecture**.

Since the Wikispeedia database is built from **all** players, it would be interesting to organize a second “World Cup of Hubs” but this time based only on the **best players**. In that setting, we might expect the bookmakers’ graph-based strategy to perform better, because top players are more likely to choose **efficient links** rather than links that simply sound familiar.

---

## The Team Choices

Our group also tried to find their own strategy before looking at this project:

Noa : Spain, Austalia, Portugal, Italy, Earth, London, Islam, Latin 

Tolga : United_states, England, China, World_war_I, Earth, United_kindgom, Europe, Turkey

Antoine : Oiseau, XXe siècle, langue anglaise, Seconde Guerre mondiale, Organisation des Nations unies, liste des pays par système de gouvernement, animal, classification scientifique

Max : États-Unis, Australie, Seconde Guerre mondiale, France, Brésil, monnaie, eau, classification scientifique

Julien : États-Unis, XXe siècle, Angleterre, agriculture, Seconde Guerre mondiale, christianisme, Amérique du Nord, République populaire de Chine

<!-- Placeholder: Everybody explain why they chose there hub -->




Noa : - -> - 80$ + 0$ = - 80$

Tolga : United_States, China, United_Kingdom -> -80$ + 1* 10$ + 8.35* 10$ + 3.36* 10$ = 47.10$

Antoine : - -> - 80$ + 0$ = - 80$

Max : United_States -> -80$ + 1* 10$ = -70$

Julien : United_States, China -> -80$ + 1* 10$ + 8.35* 10$ = 13.5$

this shows that based on no serious strategy, humans perform pretty badly on this type of gamble. Did you do better ? 


As the tournament goes on, we will track how your pick perform and see whether human intuition can keep up with the data.

---

<!-- MathJax loader to render LaTeX formulas on this page -->
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']]
    }
  };
</script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

## The Tournament Is About to Begin

With bets placed and expectations set, it is time to know the rules of the competition and the strucutre of the competion before letting the hubs fight.

**Discover how the World Cup of Hubs is designed.**  
[Structure of the Tournament](https://noaemien.github.io/ada-template-website/tournament-structure/)
