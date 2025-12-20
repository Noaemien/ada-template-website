---
layout: default
title: Analysis and Insights
---

# Analysis and Insights

With the World Cup of Hubs concluded and a champion crowned, we can now step back from the tournament narrative and examine the data more closely.

This page lifts the curtain on the **raw scores**, the **individual metrics**, and the structural properties that determined success. Unlike the tournament stages, results here are no longer normalized or hidden, we now analyze hubs on an absolute scale.

---

## Raw Hub Scores

First the **final composite score** assigned to each hub.

This is a complex metric constructed using meticulously balanced weights for normalized features to best capture all aspects affecting the navigation quality:
- **Popularity**, reflecting how often a hub is encountered and reused by players.
- **Versatility**, measuring semantic breadth and category coverage.
- **Efficiency**, capturing if a hub supports or slows down successful navigation.
- **Global visibility**, derived from external Wikipedia pageview statistics.

Each component is normalized independently prior to aggregation, to ensure that no single metric dominates due to scale effects.

<div style="width:100%; overflow-x:auto;">
  <iframe
    src="{{ '/_plots/analysis_plots/raw_scores_table.html' | relative_url }}"
    style="width:100%; height:720px; border:0;"
    loading="lazy">
  </iframe>
</div>


Inspection of the raw scores reveal a few consistent patterns:
- Highly visited or globally famous pages do not necessarily achieve high composite scores.
- Strong overall performance typically arises from balanced domination across multiple metrics, rather than extreme values in a single dimension.
- Several hubs with moderate popularity achieve high rankings due to strong efficiency or versatility.

So to better understand how that is let's go deeper into each metric.

---

## Metric 1: Popularity

This is the where we separate the cool kids from the others. Popularity quantifies player interaction frequency of a given hub during navigation.

The metric integrates multiple behavioral signals:
- Total appearances in both finished and unfinished games.
- Repeated visits within the same game session indicating a feeling of safe haven.
- Successful continuation after backtracking.
- Penalties associated with dead-end behavior due to the lack of encouragement to continue.

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/popularity_dropdown.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

A logarithmic transformation is applied to raw counts to reduce the influence of extreme outliers.

As a result, the popularity score reflects if a page is attractive enough to make the player keep going.

---

## Metric 2: Versatility

Versatility measures the conceptial connectivity of a hub by quantifying how many distinct topical regions it connects.

To get this score a hierarchial expansion from Wikipedia category annotations was utilized:
- Each article contributes its own categories.
- Categories are expanded through their parent articles to capture the hierarchical relations
- Categories of linked neighbors are utilized to evaluate its reach beyond the itself.

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/versatility_plot.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

<div style="width:100%; margin-top:14px;">
  <iframe
    src="{{ '/_plots/analysis_plots/versatility_coverage.html' | relative_url }}"
    style="width:100%; height:560px; border:0;"
    loading="lazy">
  </iframe>
</div>

Therefore versitality captures not only the topic diversity but goes further into linked categories to better identify topical connections.

Hubs with high versatility tend to link otherwise distant thematic regions, offering multiple plausible navigation paths even when their raw popularity is limited. Meaning this is specially important for players who want to take shortcuts.

---

## Metric 3: Efficiency

The last but not least the efficiency. Here the a hubs participation to successful and timely navigation is materialized.

It combines three behavioral indicators:
- The success rate of games in which the hub appears.
- The frequency of immediate backtracking following the hub.
- The average game duration associated with its usage.

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/efficiency_vs_success.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

Metrics where lower values indicate better performance (backtracking frequency and duration) are inverted and normalized prior to aggregation.

So using this we are able to separate the hubs that appear out of pure attraction due to popularity from the ones that help with mindfull pathfinding aimed at reaching the final goal.


---

## How could have a gambler win ?

At the start of the tournament, predictions were based only on the *famousness* of hubs.

The best gamblers often called **sharks** on betting apps could have approached Wikipedia not as a collection of articles, but as a **graph**.

Their strategy relied on a central concept from network science:

### Betweenness Centrality

Betweenness centrality measures how often a node lies on the shortest paths between other nodes.

In the context of Wikispeedia, this means:
- how often a page acts as a **mandatory passage point**,
- how frequently it connects unrelated navigation paths,
- and how difficult it is to bypass.

<!-- Placeholder: Visualization of betweenness centrality in the Wikispeedia graph -->

By ranking pages according to betweenness centrality, these gamblers were able to **isolate structurally critical hubs** long before the tournament began.

These hubs:
- consistently performed well across metrics,
- survived normalization and seeding,
- and dominated in knockout scenarios.

They didn’t guess.  
They calculated.

---

## Were the Sharks right ?

When comparing prediction accuracy:
- popularity explains **visibility**,
- versatility explains **flexibility**,
- effectiveness explains **victory**.

Structural metrics, especially betweenness centrality, capture all three.

In the end, the sharks didn’t just predict the winner : they predicted the *type* of hub that could win.

---

## What This Tells Us About Wikipedia Navigation
...

---

**Thank you for following us through our World Cup of Hubs ! We hope you enjoyed it !**

[Back to the menu](ada-template-website/index)
