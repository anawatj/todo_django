package main

import ("fmt"
		"os"
		"strconv"
)

func main() {
	arg := os.Args[1]

	n, err := strconv.Atoi(arg)
	if err == nil {
		count := n //* 2 - 1;

		for i:=1; i<=count; i++{
			for j:=1; j<=count; j++{
				if j==i || j==count - i + 1{
					fmt.Print("*");
				}else{
					fmt.Print(" ");
				}
			}
	
			fmt.Print("\n");
		}
	}else{
		fmt.Println("argument error")
	}
	
}