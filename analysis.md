---
layout: default
title: Analysis and Insights
---

# Analysis and Insights

With the World Cup of Hubs concluded and a champion crowned, we can now step back from the tournament narrative and examine the data more closely.

This page lifts the curtain on the **raw scores**, the **individual metrics**, and the structural properties that determined success. Unlike the tournament stages, results here are no longer normalized or hidden: we now analyze hubs on an absolute scale.

---

## Raw Hub Scores

First, the **final composite score** assigned to each hub.

This is a complex metric constructed using meticulously balanced weights for normalized features to best capture all aspects affecting navigation quality:
- **Popularity**, reflecting how often a hub is encountered and reused by players.
- **Versatility**, measuring semantic breadth and category coverage.
- **Efficiency**, capturing whether a hub supports or slows down successful navigation.

Each component is normalized independently prior to aggregation, to ensure that no single metric dominates due to scale effects.

<div style="width:100%; overflow-x:auto;">
  <iframe
    src="{{ '/_plots/analysis_plots/raw_scores_table.html' | relative_url }}"
    style="width:100%; height:720px; border:0;"
    loading="lazy">
  </iframe>
</div>

Inspection of the raw scores reveals a few consistent patterns:
- Highly visited or globally famous pages do not necessarily achieve high composite scores.
- Strong overall performance typically arises from balanced domination across multiple metrics, rather than extreme values in a single dimension.
- Several hubs with moderate popularity achieve high rankings due to strong efficiency or versatility.

To better understand how this happens, let's go deeper into each metric.

---

## Metric 1: Popularity

This is where we separate the cool kids from the others. Popularity quantifies the frequency of player interaction with a given hub during navigation.

The metric integrates multiple behavioral signals:
- Total appearances in both finished and unfinished games.
- Repeated visits within the same game session.
- Successful continuation after backtracking.
- Penalties associated with dead-end behavior due to the lack of encouragement to continue.

Here are the leaders in each category of most appearances, continuation after backtracking, and dead-end penalties.

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/popularity_dropdown.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

This analysis shows that popularity is not a single concept but a composite one. Except for a few overall dominant articles, different leaders emerge for each sub-popularity metric. This proves that treating popularity as just a pure “number of clicks” would not be logical and highlights the importance of our carefully designed first complex metric.

Each sub-category reflects a different kind of attraction for players. For example, the *most visited* property reflects familiarity with a topic, while *continuation after backtracking* captures how promising the article feels when a player decides to “save” the run and try again from it.

After confirming that these properties capture different behaviors, points from each one were combined to create a complex final popularity score, leading to the following distribution:

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/popularity_distribution.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

The observed distribution is not just skewed but structurally unequal, which proves users’ preferential attachment towards some articles. This shows that raw popularity alone is not informative for ranking quality. It further validates the necessity of a logarithmic transformation for normalization to later create a meaningful global score.

---

## Metric 2: Versatility

Versatility measures the **conceptual connectivity** of a hub by quantifying how many distinct topical regions it connects, making these hubs especially important for pathfinding shortcuts.

To get this score, a hierarchical expansion from Wikipedia category annotations was utilized:
- Each article contributes its own categories.
- Categories are expanded through their parent articles to capture hierarchical relations.
- Categories of linked neighbors are used to evaluate its reach beyond itself.

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/versatility_plot.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

Versatility shows a broader and less extreme distribution compared to popularity. It is still dominated by a few global hubs, but there is also an emerging subset of smaller hubs acting as conceptual bridges.

<div style="width:100%; margin-top:14px;">
  <iframe
    src="{{ '/_plots/analysis_plots/versatility_coverage.html' | relative_url }}"
    style="width:100%; height:560px; border:0;"
    loading="lazy">
  </iframe>
</div>

Therefore, versatility captures not only topic diversity but also the network of linked categories, to better identify topical connections. Thanks to this property, multiple plausible navigation paths within limited depth are offered, sometimes even when the raw popularity of the articles is not very high. This points to a **complementary quality** between popularity and versatility.

---

## Metric 3: Efficiency

Last but not least, **efficiency**. Here, a hub’s contribution to successful and timely navigation is quantified.

It combines three behavioral indicators:
- The success rate of games in which the hub appears.
- The frequency of immediate backtracking following the hub.
- The average game duration associated with its usage.

We can first look at the best hubs ranked by efficiency amongst all the articles:

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/efficiency_top_hubs.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

**Efficiency is not about fame**

Many of the most efficient hubs are **not very famous pages**. Some are quite niche and do not appear often in popularity rankings, yet they still help players navigate much better than expected.

This shows that efficiency measures something **different from popularity and versatility**. A page can be well known and widely visited but still slow players down or send them in the wrong direction. On the other hand, some less popular pages give clear guidance, avoid dead ends, and help players reach their goal faster.

By including efficiency in the final score, we reward pages for being *useful*, not just famous. This allows smaller or more specialized pages to stand out when they play an important role in navigation. It confirms that good hubs are not only those everyone knows, but also those that quietly help users move in the right direction.

Then we can dig deeper into the efficiency–success relationship.

<div style="width:100%;">
  <iframe
    src="{{ '/_plots/analysis_plots/efficiency_vs_success.html' | relative_url }}"
    style="width:100%; height:520px; border:0;"
    loading="lazy">
  </iframe>
</div>

The efficiency-success analysis shows that many high-success pages still induce long paths, repeated backtracking, or high dead-end rates. These are unnecessary navigational costs that are not acceptable in Wikispeedia. With a correct penalization of these hidden costs, we obtain a complex efficiency property that cannot be reduced to popularity or success frequency alone.

For better calculations, metrics where lower values indicate better performance (backtracking frequency and duration) are inverted and normalized prior to aggregation.

Using this, we are able to separate hubs that appear out of pure attraction (due to popularity) from those that help with mindful pathfinding aimed at reaching the final goal.

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

## All three metrics in a single plot

To look at the correlation between popularity, versatility, and efficiency we propose a final 3D plot. This helps show how high up the United States was as a hub and lets us see where other hubs lacked strength. 

{% include_relative _plots/3d_metrics.html %}

---

**Thank you for following us through our World Cup of Hubs! We hope you enjoyed it!**

Since the Wikispeedia game database is built from all players, the **next edition** of the “World Cup of Hubs” will be based only on the **best players**. In that setting, we might expect the bookmakers’ predictions to be more accurate, because top players are more likely to choose **efficient links** rather than links that simply sound familiar or intuitive to them.

<div class="change-page-button-wrapper">
  <a href="/ada-template-website/index" class="change-page-button">
    Back to the menu
  </a>
</div>

