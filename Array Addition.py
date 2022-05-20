def ArrayAdditionI(arr):

  b=0
  for i in (arrLength-1):
    if (arr[i]>arr[i+1]):
      b=arr[i]
    else:
      b=arr[i+1]

  for i in (arrLength-1):
    if(b==arr[i]):
      arr.remove(arr[i])
      print(arr)

  s=0
  for i in (arrLength-1):
    for j in (arrLength-2):
      s=arr[i]+arr[j]
      if(s==b):
          print("True")
          break;
      else:
          print("False")

  return arr
