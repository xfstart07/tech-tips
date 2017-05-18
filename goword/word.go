package main

import (
	"net/http"
	"net/url"
	"os"
)

func main() {
	word := os.Args[1]

	query := url.Values{}
	query.Add("word", word)

	req, err := http.PostForm("http://www.weixinote.com/api/glossaries", query)

	if err != nil {
		os.Exit(1)
	}

	if req.StatusCode == 200 {
		os.Exit(0)
	} else {
		os.Exit(1)
	}

}
