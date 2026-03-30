import numpy as np
import pandas
import faker
a = np.arange(15).reshape(3,5)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)


fake = faker.Faker()
print(fake.name())