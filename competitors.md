---
layout: default
title: The Competitors
---


# The Competitors

The World Cup of Hubs brings together a selected group of Wikipedia articles that play a central role in Wikispeedia navigation.

Each competitor represents a **hub**: a page that repeatedly appears in successful navigation paths and acts as a key transition point between topics.

This page introduces how these competitors were identified and what kind of profiles they represent.  
Their strengths, weaknesses, and odds of winning will be explored next.

---

## From Thousands of Pages to a Select Few

Wikispeedia contains thousands of Wikipedia articles that appear in real player paths.  
Not all of them are suitable competitors.

We can have a look at the composition of the Wikispeedia database: 

{% include_relative _plots/articles_overview.html %}

The purpose of a World Cup is to make the best compete, and not everyone at the same time. Have a look below at some of the most "niche" articles, which we could not define as a hub.

| Page | Popularity |
| ---- | ---------- |
|                          Comet_White-Ortiz-Bolelli |0.00163|  
|  Six-party_talks_concerning_North_Korea's_nucle... |0.00131|
|                                       Harrier_Hawk |0.00120|
|                                Long-billed_Vulture |0.00098|
|                                      PSR_B1620-26c |0.00076|
|                                 HIV_AIDS_in_Africa |0.00065|
|                       GNU_Linux_naming_controversy |0.00043|
|                                  LANSA_Cuzco_Crash |0.00032|
|                                         Newshounds |0.00021|
|                                     Arp2_3_complex |0.00000|

To address this issue and define and select hubs, we used an external dataset: Wikipedia Pageviews. The selection is based on the most visited Wikipedia pages from 2016 to 2024 to avoid any contender that would have been popular just because of a short peak.

We crossed all the most visited pages and took the 64 most consistent pages during these 8 years, so we got the "base" of Wikipedia for our hubs. But the fame of a page does not imply that it will be a good hub. Let's have a look at our contenders’ selection!

{% include_relative _plots/hub_reduction.html %}

We kept the bests of the bests to evaluate them into the competition.
---

## What Kind of Pages Compete?

The selected hubs are not all alike. They naturally fall into different archetypes:

- **Global concepts**, such as countries or continents  
- **Scientific foundations**, like core disciplines or theories  
- **Historical events**, key moments that changed the world   
- **Famous persons**, like scientists or presidents

Our contenders come from many different types of categories, but in the end, they will all be judged with the same recipe: who is the best hub.

{% include_relative _plots/top64_hubs.html %}

---

In the graph above we introduce a new metric: Volatility. Volatility is a measure of how much a hub's popularity changes year after year. Low volatility means the hub stays consistently important. High volatility means the hub's importance rises and falls with time. Obviously, here, it makes sense that FIFA World Cup is more volatile as the interest rises every four years. 

## Some surprising qualifications

Some of the hubs qualified are obvious selections, like one of the biggest, the United States page, but as we can see below, we also have some surprising qualifications.
 
| Contestant             | Popularity  | Volatility  |
| ---------------------- | ----------  | ----------  |
| Arnold Schwarzenegger  | 0.67        | 0.0022      |
| Periodic Table         | 0.58        | 0.0043      |
| Adolf Hitler           | 0.90        | 0.0008      |
| Tupac Shakur           | 0.52        | 0.0032      |

Some of these surprising qualifications might hide the underdog story of the competition! 
At this stage, we intentionally avoid ranking competitors or revealing any performance metrics.  
The goal is to understand **who is in the tournament**, not **who is expected to win**.

---

## What Comes Next

With the competitors introduced, the tournament atmosphere begins to build.

Before the first match is played, predictions will be made.  
 **Let's step to the betting floor and choose your contender!**  

<div class="change-page-button-wrapper">
  <a href="/ada-template-website/betting-floor" class="change-page-button">
    Go to next chapter : The Betting Floor
  </a>
</div>