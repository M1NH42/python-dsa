# data = [0] * 8
# print(len(data))
# print(type(data))

# print(data)

# data[2] += 1
# print(data)

# data_ = [2] * 8
# print(data_)
# print()

# data = data_.extend(data)

# print(data)

# print(data.extend(data_))

primes = [2, 3, 5, 7, 11, 13, 17, 19]

extras = [23, 29, 31]

primes.extend(extras)

print(primes[9])