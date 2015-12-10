/**
 Design Patterns v1

 Design -> Creational -> Adapter
 JavaScript
 Daniel Vega Ceja, 2015
**/

function AdapteeShiping() { // Existent, previous.
  this.request = function(origin, destination, weight) {
    this.origin = origin;
    this.destination = destination;
    this.weight = weight;
    this.total = weight * 100;
    return "Old -> From "+this.origin+" to "+this.destination+" is $ "+this.total+".00";
  }
}

function TargetShiping() { // New, improved
  this.login = function(credentials) {
    console.log("Logged in... Welcome. " + credentials)
  };
  this.setOrigin = function(origin) {
    this.origin = origin;
  };
  this.setDestination = function(destination) {
    this.destination = destination;
  };
  this.calculate = function(weight) {
    total = weight * 100;
    return total;
  }
}

// Adapter -> Returning a request (just as the Adaptee).
function ShippingAdapter(credentials) {
  var targetShipping = new TargetShiping();

  targetShipping.login(credentials);

  return {
    request: function(origin, destination, weight){
      targetShipping.setOrigin(origin);
      targetShipping.setDestination(destination);
      return "New -> From "+origin+" to "+destination+" is $ "+targetShipping.calculate(weight);+".00";
    }
  }
}

// Client to call the adapter.
function Client() {
  this.run = function() {
    var oldInterface = new AdapteeShiping();
    var cost = oldInterface.request("Guadalajara, MX", "San Antonio, TX", 80);
    console.log(cost);

    var mycred = "user/pass";
    var adapter = new ShippingAdapter(mycred);
    var newCost = adapter.request("Zamora, MX", "Austin, TX", 90);
    console.log(newCost);
  }
}

// Implementation

var client = new Client();
client.run();
