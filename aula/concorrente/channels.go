package main

import (
	"fmt"
	"time"
)

func enviarMensagem(canal chan string, mensagem string, delay time.Duration) {
	time.Sleep(delay)
	canal <- mensagem
}

func main() {
	canal1 := make(chan string)
	canal2 := make(chan string)

	go enviarMensagem(canal1, "Mensagem 1", 2*time.Second)
	go enviarMensagem(canal2, "Mensagem 2", 1*time.Second)

	for i := 0; i < 2; i++ {
		select {
			case mensagem1 := <-canal1:
				fmt.Println("Recebida a mensagem 1:", mensagem1)
			case mensagem2 := <-canal2:
				fmt.Println("Recebida a mensagem 2:", mensagem2)
		}
	}
}