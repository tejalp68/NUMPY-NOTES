import numpy as hey

# -----------------------------

arr = hey.array([10,30,40])
print(arr)

# -----------------------------

arr1 = hey.array([[10,20,30],[20,30,40]])
print(arr1)

# -----------------------------

arr3 = hey.array([[[10,20,30],[20,30,40]]])
print(arr3)

# -----------------------------

print(arr3.dtype) #returns the data type 
print(arr3.ndim)   # returns the dimension of array
print(arr1.shape)   # returns (rows , columns)
print(arr.size)     # returns tOtal elements
print(arr1.size)
print(arr3.size)

# -----------------------------

hey.zeros((3,3))

# -----------------------------

hey.ones((2,2))

# -----------------------------

hey.eye((3))

# -----------------------------

hey.eye((5))

# -----------------------------

hey.arange(0,10,2)

# -----------------------------

hey.linspace(0,1,5)

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
arr2 = hey.array([[1,2],[5,6]])

arr = hey.concatenate([arr1,arr2] ,axis=1)
print(arr)

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
arr2 = hey.array([[1,2],[5,6]])
arr3 = arr1 + arr2
print(arr3)

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
arr2 = hey.array([[1,2],[5,6]])
arr3 = arr1 - arr2
print(arr3)

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
arr2 = hey.array([[1,2],[5,6]])
arr3 = arr1 * arr2
print(arr3)

# -----------------------------

arr =hey.array([1,5,3,4,9,6,8,6])
hey.mean(arr)

# -----------------------------

hey.median(arr)

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
arr2 = hey.array([[1,2],[5,6]])
print(hey.concatenate([arr1,arr2]))

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
arr2 = hey.array([[1,2],[5,6]])
print(hey.concatenate([arr1,arr2],axis=1))

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
arr2 = hey.array([[1,2],[5,6]])
print(hey.hstack([arr1,arr2]))           #horizontal concatenation

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
arr2 = hey.array([[1,2],[5,6]])
print(hey.vstack([arr1,arr2]))            #Vertical concatenation

# -----------------------------

## Splitting values
arr =hey.array([1,5,3,4,9,6,8,6])
print(hey.array_split(arr,4))

# -----------------------------

## Adding and Removing in Array

# -----------------------------

arr =hey.array([1,5,3,4,9,6,8,6])
hey.append(arr ,56)

# -----------------------------

arr ## DOES not nodify array

# -----------------------------

hey.insert(arr,1,10)
#does not modify also

# -----------------------------

print(arr)

# -----------------------------

hey.delete(arr,[2])

# -----------------------------

print(arr)

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
hey.insert(arr1,2 ,[80,90])

# -----------------------------

arr1 = hey.array([[30,40],[50,60]])
hey.insert(arr1,1 ,[80,90],axis=1)

# -----------------------------

hey.delete(arr1,[2])

# -----------------------------

Fall=hey.array([2,9,6,4,10,33,17])
print(hey.sort(Fall))

# -----------------------------

Fall=hey.array([[2,9,6,4],[10,33,17,15]])
print(hey.sort(Fall))

# -----------------------------

#Search values
fall=hey.array([2,9,6,4,10,33,16])
s=hey.where(fall == 10)
print(s)

# -----------------------------

d = hey.where(fall % 2 == 0)
print(d)

# -----------------------------

old = hey.array([20,40,60,30,80])

fa = [True ,False ,True,False,True]
new =old[fa]
print(new)

# -----------------------------

a = hey.array([20,50,60,90,40,60])
print(hey.sum(a))
print(hey.min(a))
print(hey.max(a))
print(hey.size(a))
print(hey.std(a))
print(hey.var(a))