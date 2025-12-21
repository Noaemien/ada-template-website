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
- Repeated visits within the same game session.
- Successful continuation after backtracking.
- Penalties associated with dead-end behavior due to the lack of encouragement to continue.

Here are the leaders in each category of most appearance, continuation after backtrack and dead end penalties.

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/popularity_dropdown.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

This analysis shows that popularity is not one concept but a composit one. Which is visible through different articles leading different types of popularities, except a few overall dominant ones. The most visited property shows the familiarity of the users of this topic while the continuing after backtracking captures a feeling of being saved. 

So after confirming these properties capture different behaviours, points from each one were combined to create a complex final popularity score. Creating the following distribution:

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/popularity_distribution.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

The observed distribution that is not just skewed but structurally unequal proves the users preferential attachment towards some articles. Showing that just raw popularity is not informative for ranking quality. This proves the reason why a normalisation using a logarithmic transformation is necessary in creating a meaningful global score metric.

---

## Metric 2: Versatility

Versatility measures the conceptial connectivity of a hub by quantifying how many distinct topical regions it connects. Making them specially important for pathfinding shortcuts.

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

Versitality shows a broader and less extreme distribution compared to popularity. Still being dominated by a few global hubs but there is also a emerging subset of smaller hubs that are acting like conceptual bridges.

<div style="width:100%; margin-top:14px;">
  <iframe
    src="{{ '/_plots/analysis_plots/versatility_coverage.html' | relative_url }}"
    style="width:100%; height:560px; border:0;"
    loading="lazy">
  </iframe>
</div>

Therefore versitality captures not only the topic diversity but goes further into linked categories to better identify topical connections. Thanks to this property, multiple plausible navigation paths within the limited depth are offered. This is the case sometimes even the raw popularity of the articles is not as high. Pointing towards a complementaryquality between these metrics. 

---

## Metric 3: Efficiency

The last but not least the efficiency. Here the a hubs participation to successful and timely navigation is materialized.

It combines three behavioral indicators:
- The success rate of games in which the hub appears.
- The frequency of immediate backtracking following the hub.
- The average game duration associated with its usage.

We can first have a look at the best hubs ranked by efficiency amongst all the articles : 
<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/efficiency_top_hubs.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

**Efficiency is not about Fame**

One interesting result is that many of the most efficient hubs are **not very famous pages**. Some of them are quite niche and do not appear often in popularity rankings, yet they still help players navigate much better than expected.

This shows that efficiency measures something **different from popularity and versatility**. A page can be well known and widely visited, but still slow players down or send them in the wrong direction. On the other hand, some less popular pages give clear guidance, avoid dead ends, and help players reach their goal faster.

By including efficiency in the final score, we reward pages for being *useful*, not just famous. This allows smaller or more specialized pages to stand out when they play an important role in navigation. It confirms that good hubs are not only those everyone knows, but also those that quietly help users move in the right direction.


Then we can deep more into the efficiencyy-success relation.

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/efficiency_vs_success.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

The efficiency-success analysis showed that many high success pages still induce long paths, repeated backtracking, or high dead-end rates. These are unecessary navigational costs that are not acceptable in Wikispeedia. With a correct penalizaiton of these hidden costs a complex efficiency property that cannot be reduced to popularity or success frequency alone is produced.

For better calculations metrics where lower values indicate better performance (backtracking frequency and duration) are inverted and normalized prior to aggregation.

So using this we are able to separate the hubs that appear out of pure attraction due to popularity from the ones that help with mindfull pathfinding aimed at reaching the final goal.

The parallel coordinates plot below breaks the efficiency score into its three metrics.

Each line represents one hub. By following a line from left to right, we can see *how* a hub achieves its efficiency. Some hubs perform well because they consistently appear in successful games. Others stand out by strongly reducing dead ends or shortening navigation paths. A smaller number manage to balance all three dimensions at once.

Rather than pointing to a single “best” formula for efficiency, this visualization reveals **different efficiency profiles**: fast but risky hubs, safe but slow ones, and rare hubs that combine speed, safety, and success.

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/efficiency_decomposition_top_50.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

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

<div class="change-page-button-wrapper">
  <a href="/ada-template-website/index" class="change-page-button">
    Back to the menu
  </a>
</div>

