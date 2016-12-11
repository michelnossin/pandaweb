Client = require("jsonrpc-node").HTTP.Client;
client = new Client(3001, "localhost");

client.call("search_text", ["hallo"], function(err, result){
  console.log("the result is: " + result)
})
