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

To do so, the bookmakers scraped the whole Wikipedia website to extract a graph architecture from it (they unfortunately do not have access to the Wikispeedia players’ game data, so they cannot perfectly predict the outcome of the competition).
To estimate the importance of a node over a network, we usually use centrality measures, a central concept from network science. Bookmakers decided to mainly rely on a combination of **Betweenness** and **Katz** **centrality** measures.

### Betweenness Centrality

Betweenness centrality measures how often a node lies on the shortest paths between other nodes.

In the context of Wikispeedia, this reflects:

* How often a page acts as a mandatory passage point or bottleneck.
* How frequently it bridges otherwise unrelated navigation paths.
* The extent to which a page is difficult to bypass when trying to reach a destination efficiently.

By ranking pages according to betweenness centrality, we are able to isolate structurally critical hubs identifying the "bridges" that players are almost forced to cross.

### Katz Centrality

Katz centrality measures a node's influence by taking into account the total number of walks between it and all other nodes, weighting shorter paths more heavily than longer ones.

In the context of Wikispeedia, this means:

* Evaluating a page’s importance based not just on its immediate links, but on its entire reach across the network.
* Recognizing pages that are "close" to a large number of other pages, even if they aren't on the absolute shortest path.
* Accounting for the recursive influence of a node, where being linked to by other important nodes increases its own value.

By utilizing Katz centrality, they could identify "hidden gems": pages that might not be the most obvious hubs but possess a high degree of connectivity to various niche clusters. This allow to predict which pages would serve as the most effective "launching pads" to reach obscure target topics.

### Visual representation

For illustration, we can extract visual graphs of the **Wikipedia network** architecture. Here are the 100 most important nodes using the Betweenness centrality measure.

{% include_relative _plots/centrality_graph.html %}

## The Odds Board

Based on those two metrics, bookmakers now give an odd for every node so players can put their money on their favourite choice depending on their predictions. These odds reflect **expectations**, not outcomes.

### Selective Normalization
To account for a bookmaker's margin and filter out the "long tail" of approximately 4,000 competitors, we calculate the total market weight based only on the **Top 64** performers. 

This simultaneously creates an **overround** for the bookmakers and simplifies the calculations: since we divide individual scores by a smaller total sum, the implied probabilities will sum to more than 100% across the entire dataset, effectively lowering the odds.

#### The Mathematical Model
1. **Composite Score ($S_i$):**
   $$S_i = \frac{C_{B,i} + C_{K,i}}{2}$$

2. **Top-64 Reference Sum ($\Sigma_{top}$):**
   $$\Sigma_{top} = \sum_{j=1}^{64} S_j$$

3. **Modified Probability ($P'_i$):**
   $$P'_i = \frac{S_i}{\Sigma_{top}}$$

4. **Final Bookmaker Odds ($O_i$):**
   $$O_i = \frac{1}{P'_i}$$

These are the odds measured with this technique:

| Rank | Article           | Odds      | Betweenness | Katz     |
|:----:|:-----------------|:---------:|:-----------:|:--------:|
| 1    | United States     | 12.79     | 1.000000    | 1.000000 |
| 2    | United Kingdom    | 22.84     | 0.450465    | 0.669473 |
| 3    | Europe            | 27.41     | 0.286870    | 0.646332 |
| 4    | England           | 31.32     | 0.344380    | 0.472381 |
| 5    | France            | 32.08     | 0.127557    | 0.669898 |
| 6    | Germany           | 35.08     | 0.206276    | 0.522925 |
| 7    | World War II      | 37.08     | 0.164731    | 0.525182 |
| 8    | Africa            | 43.63     | 0.257244    | 0.329054 |
| 9    | English language  | 43.78     | 0.149230    | 0.435025 |
| 10   | India             | 46.24     | 0.119631    | 0.433570 |

This approach is fundamentally flawed. The resulting odds are far too high; a major favorite like the United States would have odds of 12.79, leading to catastrophic losses for bookmakers. The core issue is treating **Betweenness and Katz** scores as direct probabilities. These metrics measure relative structural influence within a network rather than win frequency or intrinsic strength in a 1v1 matchup

To resolve this, we implement a Bradley-Terry inspired model: by applying an exponential transformation to the scores, we convert raw "ability" into "winning potential." This transition is crucial because it accounts for the non-linear nature of competition, where elite performers possess a disproportionate advantage that a simple linear model would fail to capture.

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

3. **Normalization (Top-64 Margin):**
   We calculate the total potential based on the top 64 competitors to create the bookmaker's margin:
   $$\Omega_{top} = \sum_{j=1}^{64} W_j$$

4. **Implied Probability and Odds:**
   $$P_i = \frac{W_i}{\Omega_{top}} \quad \text{and} \quad \text{Odds}_i = \frac{1}{P_i}$$

#### Problem :
The bookmaker doesn’t know the insights of the real competition, so he cannot know how to adjust β. That is why he employs a "Market Anchor" strategy. Rather than guessing the internal skill distribution (β), the model is back-calculated by forcing the top-ranked favorite’s winning odds to exactly 8.00. By then dividing all odds by eight to create a "Top 8" market, the favorite is naturally positioned at 1.00 (100% implied probability). This approach effectively standardizes the risk profile: it treats the structural leader as a certainty for the Top 8 while allowing the exponential scaling to dictate the decreasing probabilities for the rest of the field in a mathematically consistent way.

In addition, trying to guess the Top 8 is definitely more fun for the gamblers!

# Betting area

Now you step onto the betting floor.

As a **gambler**, you only have access to public information:  
what you know, what your intuition suggests to you, and what the odds suggest.

Will you trust global fame?  
Or will you go for a promising outsider and go against the bookmakers?  

<p>Select your own favourite 8 hub articles: (you have 80\$ and must bet 10\$ on each article you think will be in the top 8 of the World Cup of Hubs)</p>

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

// Generate table with checkboxes
const container = document.getElementById("optionsContainer");
const table = document.createElement("table");
table.className = "options-table";

const thead = document.createElement("thead");
thead.innerHTML = `
  <tr>
    <th>article</th>
    <th>odd of finishing in top 8</th>
  </tr>
`;
table.appendChild(thead);

const tbody = document.createElement("tbody");
articles.forEach(article => {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td>
      <label>
        <input type="checkbox" value="${article.name}" data-odd="${article.odd}" onclick="limitSelection(this)">
        ${article.name.replace(/_/g, ' ')}
      </label>
    </td>
    <td>${article.odd.toFixed(2)}</td>
  `;
  tbody.appendChild(tr);
});
table.appendChild(tbody);
container.appendChild(table);

// Restore previous selection from localStorage (if any)
(function restoreSelectionFromStorage() {
  let raw = null;
  try {
    raw = localStorage.getItem('wc_hubs_bet');
  } catch (e) {
    return;
  }
  if (!raw) return;

  let stored = null;
  try {
    stored = JSON.parse(raw);
  } catch (e) {
    console.warn('Could not parse wc_hubs_bet from localStorage', e);
    return;
  }
  if (!Array.isArray(stored) || stored.length === 0) return;

  const inputsByName = {};
  document
    .querySelectorAll('#optionsContainer input[type="checkbox"]')
    .forEach(cb => { inputsByName[cb.value] = cb; });

  const list = document.getElementById("selectionList");
  list.innerHTML = "";
  let restoredCount = 0;

  stored.forEach(item => {
    const cb = inputsByName[item.name];
    if (!cb) return;
    cb.checked = true;
    restoredCount += 1;
    const odd = typeof item.odd === "number" ? item.odd : parseFloat(item.odd);
    const text = `${cb.value.replace(/_/g, ' ')} - ${isNaN(odd) ? "" : odd.toFixed(2)}`;
    const li = document.createElement("li");
    li.textContent = text;
    list.appendChild(li);
  });

  console.log(`Restored ${restoredCount} selections from localStorage.`);
})();

// Limit to exactly 8 selections
function limitSelection(checkbox) {
  const checked = document.querySelectorAll('#optionsContainer input:checked');
  if (checked.length > 8) {
    alert("You can only select 8 contenders for the top 8 !");
    checkbox.checked = false;
  }
}

// Save selections
function saveSelection() {
  const checkedInputs = Array.from(document.querySelectorAll('#optionsContainer input:checked'));
  if (checkedInputs.length !== 8) {
    alert("You must select 8 contenders for the top 8 !");
    return;
  }

  const selected = checkedInputs
    .map(input => `${input.value.replace(/_/g, ' ')} - ${parseFloat(input.dataset.odd).toFixed(2)}`);
  const list = document.getElementById("selectionList");
  list.innerHTML = "";
  selected.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item;
    list.appendChild(li);
  });

  // Store raw data (slug + numeric odd) so the final page can reuse it
  const payload = checkedInputs.map(input => ({
    name: input.value,
    odd: parseFloat(input.dataset.odd)
  }));
  try {
    localStorage.setItem('wc_hubs_bet', JSON.stringify(payload));
  } catch (e) {
    console.warn('Could not store bet selection in localStorage', e);
  }

  console.log("Selections saved:", selected);
}

</script>

<!-- MathJax loader to render LaTeX formulas on this page -->
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']],
      processEscapes: true
    }
  };
</script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
---

### Now, let's see some betting strategies example

We always assume you have `80$` and bet `10$` on each of 8 articles.

#### Strategy 1 : Follow the bookmakers

What if someone simply follows the odds given by the bookmakers on the real competition?

#### Strategy 2 : Perfectly predict the Top 8 hubs

What if someone predicted the 8 best hubs, how much money could they win?

#### Strategy 3 : Use global popularity

Now consider a different idea: pick the top 8 most popular pages on Wikipedia over the last 10 years. How do you think this would perform?

#### Strategy 4 : Human Intuition

Our group also tried to make their own guesses before looking at this project:

**Noa** : Spain, Australia, Portugal, Italy, Earth, London, Islam, Latin  
**Tolga** : United_States, England, China, World_War_I, Earth, United_Kingdom, Europe, Turkey  
**Antoine** : Bird, 20th_century, English_language, World_War_II, United_Nations, List_of_countries_by_system_of_government, Animal, Scientific_classification  
**Max** : United_States, England, World_War_II, English_language, Animal, 20th_century, Agriculture, Water  
**Julien** : United_States, 20th_century, England, Agriculture, World_War_II, Christianity, North_America, People's_Republic_of_China

#### Strategy 5 : Your Prediction

We will track how **Your pick** performs and see whether human intuition can keep up with the data.

---

We will look back at those strategies at the end of the competition and see which one is the best, and the worst...


## The Tournament Is About to Begin

With bets placed and expectations set, it is time to know the rules of the competition and the structure of the competition before letting the hubs fight.

**Discover how the World Cup of Hubs is designed.**  

<div class="change-page-button-wrapper">
  <a href="/ada-template-website/tournament-structure" class="change-page-button">
    Go to next chapter : Structure of the Tournament
  </a>
</div>