object  Test extends App {
  val n = args(0).toIntOption match {
    case Some(data)=>data
    case None => 0
  }
 val primes = (1 to n).toList.filter{s=>Prime.isPrime(s)}.toSeq.mkString(",")

  println(s"prime number =  ${primes}")
}
object  Prime {
  def isPrime(num:Int):Boolean = (num > 1) && !(2 to scala.math.sqrt(num).toInt).exists(x =>num % x == 0)
}
