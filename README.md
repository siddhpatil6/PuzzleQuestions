# LogicalQuestion

<h2>Reverse String with minimum iteration </h2>

```
fun reverseString(strReverseString:String){
   val charArray =  strReverseString.toCharArray();
   println(charArray.joinToString()); 
   for(i in 0 until charArray.size/2){
       val temp = charArray[i];
       charArray[i] = charArray [charArray.size - i - 1]
       charArray [charArray.size - i - 1] = temp
   }
   println(charArray.joinToString())
}
fun main() {
    reverseString("Siddhant")  // Output: "Method of A"
}
```

<h1> Find index's of array who have sum of it is target number that is 9</h1>
//Input = [2,7,11, 15, 3, 9, 29]
//Target = 9
//Output = [0,1]

```
fun findIndices(nums: IntArray, target: Int): IntArray {
            var result = HashMap<Int,Int>()
    nums.forEachIndexed{ index, values ->
        var complements = target - values
        if(result.containsKey(complements)){
            return intArrayOf(result[complements]!!,index)
        }
        result[values] = index
    }
    throw IllegalArgumentException("No two sum solution")
}

fun main() {
    val nums = intArrayOf(2, 9, 7, 11, 15, 3, 29)
   	val target = 9
    val result = findIndices(nums,target)
    println("${result}")
    println("Output = [${result[0]}, ${result[1]!!}]")
}
```

<h1>Write Higher Order Function </h1>

```
fun addOperation(a:Int,b:Int,func:(Int,Int)->Int):Int{
    return func(a,b)
}


fun main() {
    var result = addOperation(10,5) {a,b -> a+b}
    println(result)
}
```
