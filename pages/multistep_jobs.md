---
layout: default
title: Multistep Jobs
order: 6
---

Multistep jobs are required when you need to do more mapping and reducing...

For this section, we are going to be counting the animal that was seen the most
during a scientific observation that has the ngram `at` in the animals name
(I suck at examples...).

We will see a few new concepts:

 * multistep jobs
 * `command` steps
 * `pre_filters`

Setup
-----

First, create a file called `multistep.py` in your current folder with
this as the contents:

{% highlight python %}
{% include multistep_job/multistep.py %}
{% endhighlight %}

And second, create a file called `animals.txt` in your current folder with
this as the contents (these will be the observational counts of animals that
were seen):

{% highlight text %}
{% include multistep_job/animals.txt %}
{% endhighlight %}

Finally, lets run the job:

{% highlight bash %}
$ {% include multistep_job/run.sh %}
{% endhighlight %}

Check the output, you should get something like:

```bash
...
20      "bat"
...
```

Exercises
---------

 * How can you use just python (not shell commands) to filter out animals with `at` in them?
 * Use mrjob counters to find the counts of all animals, not just the max.
