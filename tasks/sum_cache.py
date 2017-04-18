import time


class SumCache:
    def __init__(self, cache_limit=50):
        self.cache_limit = cache_limit
        self.cache = {}
        self.real_execs = 0
        self.cache_execs = 0

    def add_to_cache(self, key, value):
        cache_size = len(self.cache)
        if cache_size == self.cache_limit:
            sorted_cache = sorted(self.cache.items(), key=lambda x: x[1]['num'])
            min_key = sorted_cache[0]
            print(min_key)
            self.cache.pop(min_key[0])
        self.cache[key] = value

    def get_sum(self, *args):
        """Return summ of all elements, if result is in cache returns it from cache"""
        key = args
        if key in self.cache:
            result = self.cache[key]['sum']
            self.cache[key]['num'] += 1
            self.cache_execs += 1
        else:
            start_time = time.time()
            result = sum(key)
            result_time = time.time() - start_time
            self.add_to_cache(key, {'sum': result, 'time': result_time, 'num': 0})
            self.real_execs += 1
        return result

    def save_results(self, filename):
        """Saves cache to file"""
        sorted_cache = sorted(self.cache.items(), key=lambda x: x[1]['num'], reverse=True)
        with open(filename, 'a') as f:
            f.write(str(sorted_cache))

    def show_results(self):
        """Show 5 most popular queries"""
        print("Real counts -", self.real_execs)
        print("Cache counts -", self.cache_execs)
        times = [x['time'] for x in self.cache.values()]
        max_time = max(times)
        print("The most long query -", max_time)


a = SumCache(cache_limit=10)

a.get_sum(10, 15, 20)
a.get_sum(10, 15, 20)
a.get_sum(10, 15, 20)
a.get_sum(10, 15, 20)
a.get_sum(10, 15, 20)
a.get_sum(10, 15, 20)
a.get_sum(10, 15, 20)
a.get_sum(10, 15, 20)
a.get_sum(10, 15, 20)
a.get_sum(10, 15, 30)
a.get_sum(10, 15, 30)
a.get_sum(10, 15, 30)
a.get_sum(10, 15, 30)
a.get_sum(10, 15, 30)
a.get_sum(10, 15, 40)
a.get_sum(10, 15, 40)
a.get_sum(10, 15, 40)
a.get_sum(10, 15, 40)
a.get_sum(10, 15, 40)
a.get_sum(10, 15, 40)
a.get_sum(10, 15, 40)
a.get_sum(10, 15, 40)
a.get_sum(10, 15, 40)
a.get_sum(10, 15, 40)
a.show_results()

a.save_results('/tmp/test_cache')
