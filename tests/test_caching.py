from hermes_langlib.caching import InMemoryCache, SingletonCache, cached

cache = SingletonCache(InMemoryCache)


@cached(cache)
def function(a, b):
    return sum([i ** (a * b) for i in range(a * b)])


def test_cache():
    assert function(4, 6) == 723063651171830833064388900999244
    assert function(4, 6) == 723063651171830833064388900999244
