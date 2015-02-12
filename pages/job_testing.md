---
layout: default
title: Job Testing
order: 5
---

In the same folder as before, create a file called `test_wordcount.py`:

{% highlight python %}
{% include first_job/test_wordcount.py %}
{% endhighlight %}

You will also need the `wordcount.py` file from the last exercise for this to
work properly.

Now run the test:

{% highlight bash %}
$ {% include first_job/python_tests.sh %}
{% endhighlight %}

```bash
test_word_count_mapper (__main__.TestWordCount) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
```

Exercises
---------

 * Write the test that properly sums word lengths (the reducer).
