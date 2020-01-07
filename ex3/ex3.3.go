package main

import ("fmt"
		"os"
		"strconv"
)

func main() {
	arg := os.Args[1]

	n, err := strconv.Atoi(arg)
	if err == nil {
	//	count := n //* 2 - 1;

		for i:=1; i<=n; i++{

			for j:=i; j<n; j++{
				fmt.Print(" ");
			}
	

			for j:=1; j<=(2*i-1); j++{
		
				if  j==1 || j==(2*i-1){
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