package main

import ("fmt"
		"os"
		"strconv"
)

func main() {
	arg := os.Args[1]

	n, err := strconv.Atoi(arg)
	if err == nil {
		for i:=1;i<=n;i++{
			for j:=1;j<=i;j++{
				fmt.Print("*")
			}
			fmt.Print("\n")
		}
	}else{
		fmt.Println("argument error")
	}
	
}