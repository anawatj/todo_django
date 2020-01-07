package main

import ("fmt"
		"os"
		"strconv"
)

func main() {
	arg := os.Args[1]

	n, err := strconv.Atoi(arg)
	if err == nil {
		stars := 1;
		spaces := n - 1;
		
		for i:=1; i<n*2; i++{
			if i%2==1{
				for j:=1; j<=spaces; j++{
					fmt.Print(" ");	
				}				
				for j:=1; j<stars*2; j++{
					
						fmt.Print("*")		
					
					
				}
				fmt.Print("\n")
				
				if i<n{
					spaces--;
					stars++;
				}else{
					spaces++;
					stars--;
				}	
			}

		}
	}else{
		fmt.Println("argument error")
	}
	
}