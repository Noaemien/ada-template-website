---
layout: default
title: Analysis and Insights
---

# Analysis and Insights

With the World Cup of Hubs concluded and a champion crowned, we can now step back from the tournament narrative and examine the data more closely.

This page lifts the curtain on the **raw scores**, the **individual metrics**, and the structural properties that determined success. Unlike the tournament stages, results here are no longer normalized or hidden, we now analyze hubs on an absolute scale.

---

## Raw Hub Scores

We begin by looking at the **final composite scores** computed for each hub.

These scores combine popularity, versatility, and effectiveness into a single measure of navigation quality, using the best-performing aggregation strategy identified during experimentation.

<!-- Placeholder: Table showing raw hub scores and global ranking -->

Several patterns immediately emerge:

---

## Metric 1 : Popularity

Popularity measures how often a hub is encountered and reused by players.

Looking at raw popularity scores reveals:...

<!-- Placeholder: Popularity distribution plot -->

---

## Metric 2 : Versatility

Versatility captures how broadly a hub connects different areas of Wikipedia.

Highly versatile hubs:...

<!-- Placeholder: Versatility plot or category-coverage visualization -->

---

## Metric 3 : Effectiveness

Effectiveness measures whether a hub actually helps players reach their targets.

It reflects:
- success vs failure rates,
- dead-end behavior,
- and navigation speed.

<!-- Placeholder: Effectiveness vs success rate visualization -->

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

[Back to the menu](ada-template-website/index/)
