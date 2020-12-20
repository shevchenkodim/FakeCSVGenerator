utils = {
    axios_post(_url, _body = {}) {
        let headers = {
            "X-CSRFToken": this.data.contactCSRF,
        }
        return axios({
            method: 'POST',
            url: _url,
            data: _body,
            headers: headers
        })
    },
    axios_get(_url) {
        return axios({
            method: 'GET',
            url: _url
        })
    },
}
