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

We can have a look to the composition of the Wikispeedia database : 

<!-- Placeholder: Overview of number of articles appearing in the dataset -->
{% include_relative _plots/articles_overview.html %}

<!-- Placeholder: Show some articles that appears the less and why we need to select becausse some are irrelevant -->
The purpose of a World Cup is to make compete the bests, and not everyone at the same time. Have a look below to some of the most "niche" articles, which we could not define as a hub.

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

The address this issue to define and select hubs, we did a selection based on an external dataset : Wipedia Pageviews. The selection is based on the most visited Wikipedia page from 2016 to 2024 to avoid any contender that would have been popular just because of a peak at a moment.
We crossed all the most visted pages and took the 64 more consistent pages during these 8 years, so we got the "base" of Wikipedia for our hubs. But the fame of a page does not imply that it will be a good hub. Let's have a look to our contenders selection !

<!-- Placeholder: Figure showing the reduction from all pages to qualified hubs -->
{% include_relative _plots/hub_reduction.html %}

We kept the bests of the bests to evaluate them into the competition.
---

## What Kind of Pages Compete?

The selected hubs are not all alike. They naturally fall into different archetypes:

- **Global concepts**, such as countries or continents  
- **Scientific foundations**, like core disciplines or theories  
- **Historical events**, some moments that changed the world   
- **Famous persons**, like scientists or presidents

Our contenders come from many different types of categories, but at the end, they will all be judged with the same recipe : who is the best hub.

<!-- Placeholder: Bar chart or table showing distribution of selected hubs -->
{% include_relative _plots/top64_hubs.html %}

<!-- Placeholder:Analysis in genenral of the selection -->
---

## Some surprising qualifications

Some of the hubs qualified are obvious selection like one of the biggest, the United States page, but as we can see below, we have some surprising qualifications too.
<!-- Placeholder: Show the most unexpected qualifications) -->

| Contestant            | Popularity  | Volatility  |
| ----------            | ----------  | ----------  |
| Arnold Schwartznegger | 0.67        | 0.0022      |
| Periodic Table        | 0.58        | 0.0043      |
| Adolph Hitler         | 0.90        | 0.0008      |
| Tupak Shakur          | 0.52        | 0.0032      |

Some of this surprising qualifications might hîde the underdog story of the competition ! 
At this stage, we intentionally avoid ranking competitors or revealing any performance metrics.  
The goal is to understand **who is in the tournament**, not **who is expected to win**.

---

## What Comes Next

With the competitors introduced, the tournament atmosphere begins to build.

Before the first match is played, predictions will be made.  
 **Let's step to the betting floor and choose your contender !**  

<div class="change-page-button-wrapper">
  <a href="/ada-template-website/betting-floor" class="change-page-button">
    Go to next chapter : The Betting Floor
  </a>
</div>