package main

import (
	"fmt"
	"time"
)

func trabalho(nome string) {
	fmt.Println("Trabalho", nome, "iniciado")
	time.Sleep(2 * time.Second)
	fmt.Println("Trabalho", nome, "finalizado")
}

func main() {
	go trabalho("Goroutine 1")
	go trabalho("Goroutine 2")
	go trabalho("Goroutine 3")
	go trabalho("Goroutine 4")

	time.Sleep(3 * time.Second)

	fmt.Println("Todos os trabalhos foram finalizados")
}