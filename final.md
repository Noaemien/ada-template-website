---
layout: default
title: The Grand Final
---

# The Grand Final

After weeks of competition, countless matchups, and relentless eliminations, the World Cup of Hubs reaches its final moment.

Two hubs remain : United_States VS United_Kingdom

Both have survived the group stage, the repechage or direct qualification, and three knockout rounds. Each followed a different path, faced different opponents, and proved its strength under pressure.

---

## The Final Match, And the Champion Is…

The Grand Final is decided in a single, decisive confrontation.

The two hubs are evaluated head-to-head using the same scoring framework as in previous rounds. All metrics are applied consistently, and only relative performance matters.


<!-- Placeholder: Final match result visualization (e.g., bar chart or radar plot) -->


🏆 **Champion: United_States**

This hub is crowned the **World Cup of Wikipedia Hubs champion**.

<!-- Placeholder: Champion highlight figure or celebratory graphic -->

---

## Final Results

The tournament concludes with a final ranking of the top competitors.

**Top 1 : United_States**  
**Top 2 : United_Kingdom**  
**Top 4 : South_Africa**
**Top 4 : Germany**  
**Top 8 : Israel**  
**Top 8 : Adolf_Hitler**
**Top 8 : Russia**  
**Top 8 : China**  

---

## Looking Back at the Tournament : Which betting strategy was the best ?

Now the part you have been waiting for : Did you win some money ?

We always assume players have 80 $ and bet 10 $ on each of 8 articles.

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
 
  **United States, Russia, South Africa, United Kingdom, Israel, China, Germany, Adolf Hitler**

The return from the 7 bettable winners would be:

- `10 × (1.00 + 8.05 + 10.63 + 3.36 + 11.53 + 8.35 + 5.75) = 486.7 $`
- Profit: `486.7 $ − 80 $ = 406.7 $`

Note to mention that Adolf Hitler was not even proposed by the bookmakers, showing that the bookmakers could'nt predict the competition well and that the graph analysis alone is not sufficient enough to estimate wikispeedia's players behaviors.
Underdogs that were not proposed to bet on is part of the game (that's one way how bookmakers can make money)

#### Strategy 3 – Use global popularity

Picking the top 8 most popular pages on Wikipedia over the last 10 years.  
We realize that these are **not** the same as the nodes favored by the Wikipedia link architecture, so the overlap with the bookmaker’s list is limited : Indeed, we need to go up to the 15th most visited page of Wikipedia to find 8 articles that are also porposed by the bookmakers.

| Article by popularity on the real world wikipedia           |
|--------------------|
| 1. United States      |
| 2. Wikipedia          |
| 3. India              |
| 4. Google             |
| 5. World War II       |
| 6. Adolf Hitler       |
| 7. United Kingdom     |
| 8. Barack Obama       |
| 9. World War I        |
| 10. Michael Jordan     |
| 11. Winston Churchill  |
| 12. China              |
| 13. Elvis Presley      |
| 14. Canada             |
| 15. Australia          |

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


#### Strategy 4 : Human Intuition

Let's see how much money our group made...

Noa : - -> - 80\$ + 0\$ = - 80\$

Tolga : United_States, China, United_Kingdom -> -80\$ + 1* 10\$ + 8.35* 10\$ + 3.36* 10\$ = 47.10\$

Antoine : - -> - 80\$ + 0\$ = - 80\$

Max : United_States -> -80\$ + 1* 10\$ = -70\$

Julien : United_States, China -> -80\$ + 1* 10\$ + 8.35* 10\$ = 13.5\$

this shows that based on no serious strategy, humans perform pretty badly on this type of gamble. Did you do better ? Lets see :

#### Strategy 5 : YOUR BET

Below you can see the 8 contenders you selected on the betting floor and how they compare to the actual final Top 8.

<div id="yourBetSummary"></div>

<script>
(function () {
  const winners = [
    "United_States",
    "United_Kingdom",
    "South_Africa",
    "Germany",
    "Israel",
    "Adolf_Hitler",
    "Russia",
    "China"
  ];

  const summaryEl = document.getElementById("yourBetSummary");
  if (!summaryEl) return;

  let stored = null;
  try {
    stored = JSON.parse(localStorage.getItem("wc_hubs_bet") || "null");
  } catch (e) {
    stored = null;
  }

  if (!Array.isArray(stored) || stored.length !== 8) {
    summaryEl.innerHTML = "<p><em>No saved bet found. Go back to the betting floor, place your 8 bets, then return here.</em></p>";
    return;
  }

  const winningPicks = stored.filter(p => winners.includes(p.name));
  const sumOdds = winningPicks.reduce((sum, p) => {
    const odd = typeof p.odd === "number" ? p.odd : parseFloat(p.odd);
    return sum + (isNaN(odd) ? 0 : odd);
  }, 0);

  const stake = 80;
  const betPerArticle = 10;
  const totalReturn = betPerArticle * sumOdds;
  const profit = totalReturn - stake;

  const listItems = stored.map(p => {
    const isWinner = winners.includes(p.name);
    const label = p.name.replace(/_/g, " ");
    return `<li>${label} — odd_top8: ${p.odd.toFixed(2)} ${isWinner ? "(in final Top 8)" : ""}</li>`;
  }).join("");

  summaryEl.innerHTML = `
    <p>Your 8 selected hubs:</p>
    <ul>${listItems}</ul>
    <p>Number of your hubs that reached the final Top 8: <strong>${winningPicks.length}</strong></p>
    <p>Sum of the odds of your hubs that are in the final Top 8: <strong>${sumOdds.toFixed(2)}</strong></p>
    <p>Since you bet ${betPerArticle} on each hub (total stake ${stake}), your total return would be <strong>${totalReturn.toFixed(2)}</strong> and your profit <strong>${profit.toFixed(2)}</strong>.</p>
  `;
})();
</script>

---

## Analysis and Insights

With the champion crowned, it is time to step back and analyze what truly determined success.

**Dive into the data and understand the results.**  
[Explore the Analysis](ada-template-website/analysis)
