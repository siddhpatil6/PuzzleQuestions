# LogicalQuestion

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
