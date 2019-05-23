import numpy as np

a = np.arange(0,12)
a.shape = 3,4
print("a",a)
a.tofile("a.bin")

b = np.fromfile("a.bin",dtype=np.float)
print("b",b)

b = np.fromfile("a.bin",dtype=np.int32)
print("b",b)
b.shape=3,4
print("b",b)

np.save("a.npy",a)
c = np.load("a.npy")
print("c",c)

a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0,1.0,0.1)
c = np.sin(b)

np.savez("result.npz",a,b,sin_array=c)
r = np.load("result.npz")
print("r['arr_0']",r["arr_0"]) 
print("r['arr_1']",r["arr_1"])
print("r['sin_array']",r["sin_array"])

a = np.arange(0,12,0.5).reshape(4,-1)
np.savetxt("a.txt", a)
c = np.loadtxt("a.txt")
print("c",c)
np.savetxt("a.txt",a,fmt="%d",delimiter=",")
c = np.loadtxt("a.txt",delimiter=",")
print("c",c)

a = np.arange(8)
b = np.add.accumulate(a)
c = a + b
print("a",a)
print("b",b)
print("c",c)
f = open("result.npy","wb")
np.save(f,a)
np.save(f,b)
np.save(f,c)
f.close()
f = open("result.npy","rb")
c = np.load(f)
print("c",c)
c = np.load(f)
print("c",c)
c = np.load(f)
print("c",c)

