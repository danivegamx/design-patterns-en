/**
 Design Patterns v1

 Design -> Creational -> Builder Pattern
 JavaScript
 Daniel Vega Ceja, 2015
**/

function testBuilderPattern() { // Testing the final built object.
  var shop = new Director(); // Call the 'shop'.
  var carBuilder = new CarBuilder(); // Instance the constructor.
  var car = shop.construct(carBuilder); // Build the car.

  car.doSomething(); // Test the parts.
}

// This is the 'shop' for the car. It's the participant in charge of build the car step by step.
function Director() {
  this.construct = function(builder) { // Call the builder step by step.
    builder.step1();
    builder.step2();
    return builder.getFinal(); // Return final built object.
  }
}

// This function acts as the builder per se.
function CarBuilder() {
  this.car = null;
  this.step1 = function() {
    this.car = new Car();
  }
  this.step2 = function() {
    this.car.addParts();
  }
  this.getFinal = function() {
    return this.car;
  }
}

// This function builds the complex sub-systems for the final object.
function Car() {
  this.doors = 0;

  this.addParts = function() {
    this.doors = 4;
  }

  // Final action for the testing functionality.
  this.doSomething = function() {
    console.log("I have "+this.doors+" doors.");
  }
}

// Call the pattern.
testBuilderPattern();
