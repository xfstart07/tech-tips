package main

import (
	"net/http"
	"net/url"
	"os"
)

func main() {
	trans := os.Args[1]

	query := url.Values{}
	query.Add("sentence", trans)

	req, err := http.PostForm("http://www.weixinote.com/api/translates", query)

	if err != nil {
		os.Exit(1)
	}

	if req.StatusCode == 200 {
		os.Exit(0)
	} else {
		os.Exit(1)
	}

}
