package main

import (
	"github.com/labstack/gommon/log"
	"net/http"
)
const message = "hello wodfrld"
func main() {
	mux:= http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type","text/plain; charset=utf-8")
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(message))
	})
	err := http.ListenAndServe(":8080", mux)
	if err!= nil {
		log.Fatal("Server failt to start: %v", err)
	}
}