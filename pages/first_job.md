---
layout: default
title: First Job
order: 4
---

First, create a file called `wordcount.py` in your current folder with
this as the contents:

{% highlight python %}
{% include first_job/wordcount.py %}
{% endhighlight %}

And second, create a file called `words.txt` in your current folder with
this as the contents:

{% highlight text %}
{% include first_job/words.txt %}
{% endhighlight %}

Finally, lets run the job:

{% highlight bash %}
{% include first_job/run.sh %}
{% endhighlight %}

Check the output, you should get something like:

```bash
...
"words" 35
...
```

Exercises
---------

 * Find the distribution of word length counts.
 * How many times does `Vim` show up in the text?
