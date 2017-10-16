import itertools
import matplotlib.pyplot as plt

# Taken from https://docs.python.org/3/library/itertools.html#itertools-recipes
def partition(pred, iterable):
    'Use a predicate to partition entries into false entries and true entries'
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = itertools.tee(iterable)
    return filter(lambda x: not pred(x), t1), filter(pred, t2)

def pretty_plot(X, *Ys, **kwargs):
    items = kwargs.iteritems()
    our_keywords = ['title', 'xlabel', 'ylabel']
    (passthrough, ourkws) = partition(lambda x: x[0] in our_keywords, items)
    passthrough = dict(passthrough)
    ours = dict(ourkws)
    fig = plt.figure(**passthrough)
    for (y, label) in Ys:
        plt.plot(X, y, label=label)
    if 'title' in ours:
        plt.title(ours['title'])
    if 'xlabel' in ours:
        plt.xlabel(ours['xlabel'])
    if 'ylabel' in ours:
        plt.ylabel(ours['ylabel'])
    plt.legend(loc=0)
    return fig
