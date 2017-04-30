
/* uri = 'http://bloodclinicserver.herokuapp.com/api' */
uri = 'http://localhost:5000/api'
date = new Date()
payload = {'date': date}
headers = new Headers({'Content-Type': 'application/json'})
fetch(uri, {
  method: 'POST',
  body: JSON.stringify(payload),
  headers: headers
}).then((response) =>
  response.json()).then(json => console.log(json))
