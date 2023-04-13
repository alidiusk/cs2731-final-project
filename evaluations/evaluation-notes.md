# Human Evaluation Best Practices Notes

* From: [Best practices for the human evaluation of automatically generated text](https://aclanthology.org/W19-8643.pdf)
    * Name dropped by prof
* Also consult [The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations](https://aclanthology.org/W19-8648.pdf)

## Overview of Current Work

* Intrinsic vs extrinsic
    * Intrinsic -- aim to evaluate properties of system's output, e.g. by asking about fluency of
      system's output in a questionnaire
    * Extrinsic -- aim to evaluate the impact of system by investigating to what degree the system
      achieves the overarching task for which it was developed
    * Extrinsic argued to be more useful, but rarer -- requires that system be embedded in its use
      case (thus it must have one), which can be difficult
* Text quality
    * Popular (primary) evaluation measure but difficult to assess as text quality criteria differs
      across tasks
    * Fluency vs naturalness vs quality ... etc.
        * Often overlap between these categories
    * No standard evaluation model and significant variety in naming conventions
* Sample size and demographics
    * Not relevant for us.
* Design
    * Median of 100 items used but with broad range from 2 to 5,400
    * Few papers provide detailed report of evaluation study design
* Number of questions and types of scales
    * Wide range of rating methods used to measure criteria (e.g. text quality)
    * Most popular is 5-point Likert scale, but preference ratings are a close second
        * Other types are much less common
    * Number of ratings to measure a single criterion?
* Statistics and data analysis
    * Minority of papers report 1+ statistical analyses for human evaluation to determine if findings
      are statistically significant
    * Types of statistical analyses vary greatly
    * Many papers do not report their hypotheses OR do not perform a statistical test

## Best Practices

* Mostly restricted to intrinsic evaluation
* Text quality and criteria
    * Lots of variance in guidance
    * Should use separate, clear criteria and weight them
* Sample size, demographics and agreement
    * Expert- vs reader-focused -- Largely N/A for us
    * Evaluator agreement
        * Inter-Annotator Agreement (IAA) scores
            * Present IAA statistics with confidence intervals
            * Issue -- narrower confidence intervals expected with large samples (>= 1000 comparisons)
              which is rare...
        * Low IAA can be highly informative
        * Report percentage agreement
    * Sample size
        * For expert-focused evaluations, should use 3+ annotators
* Number of questions and types of scales
    * Should use a 7-point Likert scale
        * Maximizes reliability, validity, and discriminative power
    * Ranking-based methods (combined with continuous scales) are preferred, but can have problems
    * Multi-item scales have much higher predictive validity
        * May be able to improve reliability of Likert scales to that of ranking-based methods but
          this has not been empirically tested
        * Use of multiple-item scales vs. single-item scales affects the type of statistical testing
          needed
        * TODO See Amidei et al., 2019
* Design
    * Randomizing order of examples should be sufficient
    * Correlation when participants shown all text criterions at once instead of one at a time
* Statistics and data analysis
    * ... TODO review later
* Tabulated Summary
    * Always conduct human evaluation when possible
    * Use separate criteria rather than overall quality assessment. Properly define criteria that
      are used in the evaluation
    * Sampling -- N/A
    * Annotation -- N/A
    * Measurement -- use multiple item 7-point (preferably) Likert scales
    * Design -- Use random ordering + report
    * Statistics -- TODO
